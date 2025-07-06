from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import numpy as np
import pandas as pd
import os
import pickle
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__, 
           template_folder='../frontend',
           static_folder='../frontend')

# Alternative path setup for different deployment environments
import sys
import os

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
frontend_dir = os.path.join(parent_dir, 'frontend')

# Update template and static folders
app.template_folder = frontend_dir
app.static_folder = frontend_dir

CORS(app)  # Enable CORS for frontend communication

# Global variables to store the trained model and feature names
model_knn = None
feature_names = None

def save_model(model, feature_names, model_path="models/curacheck_model.pkl"):
    """Save the trained model and feature names"""
    try:
        # Create models directory if it doesn't exist
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        model_data = {
            'model': model,
            'feature_names': feature_names,
            'model_type': 'KNeighborsClassifier'
        }
        
        with open(model_path, 'wb') as f:
            pickle.dump(model_data, f)
        
        print(f"✅ Model saved successfully at: {model_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error saving model: {str(e)}")
        return False

def load_saved_model(model_path="models/curacheck_model.pkl"):
    """Load a previously saved model"""
    try:
        if not os.path.exists(model_path):
            print(f"⚠️ No saved model found at: {model_path}")
            return None, None
        
        with open(model_path, 'rb') as f:
            model_data = pickle.load(f)
        
        model = model_data['model']
        feature_names = model_data['feature_names']
        
        print(f"✅ Model loaded successfully from: {model_path}")
        print(f"Features count: {len(feature_names)}")
        
        return model, feature_names
        
    except Exception as e:
        print(f"❌ Error loading saved model: {str(e)}")
        return None, None

def load_and_train_model():
    """Load data and train the model (or load from saved model)"""
    global model_knn, feature_names
    
    # First try to load a saved model
    print("🔍 Looking for saved model...")
    saved_model, saved_features = load_saved_model()
    
    if saved_model is not None and saved_features is not None:
        model_knn = saved_model
        feature_names = saved_features
        print("✅ Using saved model!")
        return True
    
    print("🏋️ No saved model found. Training new model...")
    
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        training_path = os.path.join(script_dir, 'source', 'Training.csv')
        
        # Load training data
        disease_dataset_training = pd.read_csv(training_path)
        
        # Clean data
        train_data = disease_dataset_training.copy()
        unnamed_cols = [col for col in train_data.columns if 'Unnamed' in col]
        if unnamed_cols:
            train_data = train_data.drop(unnamed_cols, axis=1)
        
        # Prepare features and target
        x_train = train_data.drop(['prognosis'], axis=1)
        y_train = train_data['prognosis']
        
        # Store feature names for validation
        feature_names = x_train.columns.tolist()
        
        print("⚙️ Training model... This may take a few minutes.")
        
        # Train model
        clf_knn = KNeighborsClassifier()
        parameters_knn = {'n_neighbors':[1,3,5,7,9,11], 'metric':['euclidean','manhattan','chebyshev']}
        grid_clf_knn = GridSearchCV(clf_knn, parameters_knn, cv=6, n_jobs=-1)
        grid_clf_knn.fit(x_train, y_train)
        
        model_knn = grid_clf_knn.best_estimator_
        
        print(f"✅ Model trained successfully!")
        print(f"Number of features: {len(feature_names)}")
        print(f"Best parameters: {grid_clf_knn.best_params_}")
        
        # Save the trained model
        print("💾 Saving trained model...")
        save_model(model_knn, feature_names)
        
        return True
        
    except Exception as e:
        print(f"❌ Error loading/training model: {str(e)}")
        return False

@app.route('/')
def home():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api')
def api_info():
    """API info endpoint"""
    return jsonify({
        "message": "CuraCheck API is running!",
        "endpoints": {
            "home": "/ (GET) - Main website",
            "predict": "/predict (POST)",
            "symptoms": "/symptoms (GET)",
            "health": "/health (GET)"
        }
    })

@app.route('/images/<path:filename>')
def serve_images(filename):
    """Serve image files"""
    return send_from_directory('../frontend/images', filename)

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, JS, etc.)"""
    return send_from_directory('../frontend', filename)

@app.route('/health')
def health_check():
    """Health check endpoint"""
    model_status = "loaded" if model_knn is not None else "not loaded"
    return jsonify({
        "status": "healthy",
        "model_status": model_status,
        "features_count": len(feature_names) if feature_names else 0
    })

@app.route('/symptoms')
def get_symptoms():
    """Get list of all symptoms/features"""
    if feature_names is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    return jsonify({
        "symptoms": feature_names,
        "count": len(feature_names)
    })

@app.route('/predict', methods=['POST'])
def predict_disease():
    """Predict disease based on symptoms array"""
    try:
        if model_knn is None:
            return jsonify({"error": "Model not loaded"}), 500
        
        # Get symptoms array from request
        data = request.get_json()
        
        if 'symptoms' not in data:
            return jsonify({"error": "Missing 'symptoms' field in request"}), 400
        
        symptoms_array = data['symptoms']
        
        # Validate input
        if not isinstance(symptoms_array, list):
            return jsonify({"error": "Symptoms must be a list"}), 400
        
        if len(symptoms_array) != len(feature_names):
            return jsonify({
                "error": f"Symptoms array must have {len(feature_names)} elements, got {len(symptoms_array)}"
            }), 400
        
        # Validate that all values are 0 or 1
        if not all(x in [0, 1] for x in symptoms_array):
            return jsonify({"error": "All symptom values must be 0 or 1"}), 400
        
        # Convert to numpy array and reshape for prediction
        symptoms_array = np.array(symptoms_array).reshape(1, -1)
        
        # Make prediction
        prediction = model_knn.predict(symptoms_array)[0]
        
        # Get prediction probability (confidence)
        try:
            probabilities = model_knn.predict_proba(symptoms_array)[0]
            max_prob = float(np.max(probabilities))
        except:
            max_prob = None
        
        # Count symptoms present
        symptoms_present = int(np.sum(symptoms_array))
        
        return jsonify({
            "prediction": prediction,
            "confidence": max_prob,
            "symptoms_present": symptoms_present,
            "total_symptoms": len(feature_names),
            "status": "success"
        })
        
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

@app.route('/retrain', methods=['POST'])
def retrain_model():
    """Force retrain the model (ignoring saved model)"""
    global model_knn, feature_names
    
    try:
        print("🔄 Force retraining model...")
        
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        training_path = os.path.join(script_dir, 'source', 'Training.csv')
        
        # Load training data
        disease_dataset_training = pd.read_csv(training_path)
        
        # Clean data
        train_data = disease_dataset_training.copy()
        unnamed_cols = [col for col in train_data.columns if 'Unnamed' in col]
        if unnamed_cols:
            train_data = train_data.drop(unnamed_cols, axis=1)
        
        # Prepare features and target
        x_train = train_data.drop(['prognosis'], axis=1)
        y_train = train_data['prognosis']
        
        # Store feature names for validation
        feature_names = x_train.columns.tolist()
        
        print("⚙️ Training model... This may take a few minutes.")
        
        # Train model
        clf_knn = KNeighborsClassifier()
        parameters_knn = {'n_neighbors':[1,3,5,7,9,11], 'metric':['euclidean','manhattan','chebyshev']}
        grid_clf_knn = GridSearchCV(clf_knn, parameters_knn, cv=6, n_jobs=-1)
        grid_clf_knn.fit(x_train, y_train)
        
        model_knn = grid_clf_knn.best_estimator_
        
        print(f"✅ Model retrained successfully!")
        print(f"Best parameters: {grid_clf_knn.best_params_}")
        
        # Save the newly trained model
        print("💾 Saving retrained model...")
        save_model(model_knn, feature_names)
        
        return jsonify({
            "message": "Model retrained successfully",
            "features_count": len(feature_names),
            "best_params": grid_clf_knn.best_params_,
            "status": "success"
        })
        
    except Exception as e:
        return jsonify({"error": f"Retraining failed: {str(e)}"}), 500

if __name__ == '__main__':
    print("Starting CuraCheck API...")
    
    # Load and train model on startup
    if load_and_train_model():
        print("✅ Model loaded successfully!")
        print("🚀 Starting Flask server...")
        
        # Use environment variable for port (Render requirement)
        import os
        port = int(os.environ.get('PORT', 5000))
        
        app.run(debug=False, host='0.0.0.0', port=port)
    else:
        print("❌ Failed to load model. Please check your data files.")

# For Vercel serverless deployment
def handler(event, context):
    """Vercel serverless function handler"""
    # Load model if not already loaded
    if model_knn is None:
        load_and_train_model()
    
    # Return the Flask app for serverless execution
    return app

# Initialize model for serverless environment
if not __name__ == '__main__':
    # This runs when imported as a module (Vercel)
    load_and_train_model()
