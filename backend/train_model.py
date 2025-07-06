"""
Standalone script to train and save the CuraCheck model
Run this script to create a saved model file that can be loaded quickly by the API
"""

import numpy as np
import pandas as pd
import os
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings('ignore')

def train_and_save_model():
    """Train the model and save it to a file"""
    
    print("🏋️ Training CuraCheck Disease Prediction Model...")
    print("-" * 50)
    
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        training_path = os.path.join(script_dir, 'source', 'Training.csv')
        
        print(f"📁 Loading training data from: {training_path}")
        
        # Load training data
        disease_dataset_training = pd.read_csv(training_path)
        print(f"✅ Loaded dataset with shape: {disease_dataset_training.shape}")
        
        # Clean data
        train_data = disease_dataset_training.copy()
        unnamed_cols = [col for col in train_data.columns if 'Unnamed' in col]
        if unnamed_cols:
            print(f"🧹 Removing unnamed columns: {unnamed_cols}")
            train_data = train_data.drop(unnamed_cols, axis=1)
        
        # Prepare features and target
        x_train = train_data.drop(['prognosis'], axis=1)
        y_train = train_data['prognosis']
        
        feature_names = x_train.columns.tolist()
        
        print(f"📊 Features: {len(feature_names)}")
        print(f"📊 Diseases: {len(y_train.unique())}")
        print(f"📊 Training samples: {len(x_train)}")
        
        print("\n⚙️ Training K-Nearest Neighbors model with GridSearch...")
        print("This may take several minutes...")
        
        # Train model with GridSearch
        clf_knn = KNeighborsClassifier()
        parameters_knn = {
            'n_neighbors': [1, 3, 5, 7, 9, 11], 
            'metric': ['euclidean', 'manhattan', 'chebyshev']
        }
        
        grid_clf_knn = GridSearchCV(
            clf_knn, 
            parameters_knn, 
            cv=6, 
            n_jobs=-1,
            verbose=1
        )
        
        grid_clf_knn.fit(x_train, y_train)
        
        # Get the best model
        best_model = grid_clf_knn.best_estimator_
        
        print(f"\n✅ Training completed!")
        print(f"🏆 Best parameters: {grid_clf_knn.best_params_}")
        print(f"📈 Best cross-validation score: {grid_clf_knn.best_score_:.4f}")
        
        # Calculate training accuracy
        train_accuracy = best_model.score(x_train, y_train)
        print(f"📈 Training accuracy: {train_accuracy:.4f}")
        
        # Create models directory
        models_dir = os.path.join(script_dir, 'models')
        os.makedirs(models_dir, exist_ok=True)
        
        # Save the model
        model_path = os.path.join(models_dir, 'curacheck_model.pkl')
        
        model_data = {
            'model': best_model,
            'feature_names': feature_names,
            'model_type': 'KNeighborsClassifier',
            'best_params': grid_clf_knn.best_params_,
            'best_score': grid_clf_knn.best_score_,
            'training_accuracy': train_accuracy,
            'diseases': list(y_train.unique()),
            'feature_count': len(feature_names)
        }
        
        print(f"\n💾 Saving model to: {model_path}")
        
        with open(model_path, 'wb') as f:
            pickle.dump(model_data, f)
        
        print("✅ Model saved successfully!")
        
        # Save model info as text file for reference
        info_path = os.path.join(models_dir, 'model_info.txt')
        with open(info_path, 'w') as f:
            f.write("CuraCheck Disease Prediction Model Information\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Model Type: {model_data['model_type']}\n")
            f.write(f"Features: {model_data['feature_count']}\n")
            f.write(f"Diseases: {len(model_data['diseases'])}\n")
            f.write(f"Best Parameters: {model_data['best_params']}\n")
            f.write(f"Cross-validation Score: {model_data['best_score']:.4f}\n")
            f.write(f"Training Accuracy: {model_data['training_accuracy']:.4f}\n\n")
            f.write("Diseases List:\n")
            for i, disease in enumerate(sorted(model_data['diseases']), 1):
                f.write(f"{i:2d}. {disease}\n")
        
        print(f"📄 Model info saved to: {info_path}")
        
        print("\n🎉 Model training and saving completed successfully!")
        print(f"You can now use the saved model in your API without retraining.")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = train_and_save_model()
    if success:
        print("\n✅ Success! Your model is ready to use.")
    else:
        print("\n❌ Failed to train and save model.")
    
    input("\nPress Enter to exit...")
