"""
Test script to verify saved model works correctly
"""

import pickle
import numpy as np
import os

def test_saved_model():
    """Test the saved model"""
    
    print("🧪 Testing Saved CuraCheck Model...")
    print("-" * 40)
    
    try:
        # Load the saved model
        script_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(script_dir, 'models', 'curacheck_model.pkl')
        
        if not os.path.exists(model_path):
            print("❌ No saved model found! Run train_model.py first.")
            return False
        
        print(f"📁 Loading model from: {model_path}")
        
        with open(model_path, 'rb') as f:
            model_data = pickle.load(f)
        
        model = model_data['model']
        feature_names = model_data['feature_names']
        
        print(f"✅ Model loaded successfully!")
        print(f"📊 Features: {len(feature_names)}")
        print(f"📊 Diseases: {len(model_data['diseases'])}")
        print(f"🏆 Best params: {model_data['best_params']}")
        print(f"📈 Training accuracy: {model_data['training_accuracy']:.4f}")
        
        # Test prediction with sample data
        print("\n🧪 Testing prediction...")
        
        # Create a sample symptoms array (all zeros except a few symptoms)
        sample_symptoms = [0] * len(feature_names)
        # Set some symptoms as present for testing
        sample_symptoms[0] = 1  # First symptom
        sample_symptoms[5] = 1  # Sixth symptom  
        sample_symptoms[10] = 1  # Eleventh symptom
        
        sample_array = np.array(sample_symptoms).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(sample_array)[0]
        
        print(f"✅ Sample prediction: {prediction}")
        print(f"📊 Symptoms present: {sum(sample_symptoms)}")
        
        # Test with different confidence levels if available
        try:
            probabilities = model.predict_proba(sample_array)[0]
            max_prob = float(np.max(probabilities))
            print(f"📊 Confidence: {max_prob:.4f}")
        except:
            print("📊 Confidence: Not available (KNN doesn't provide probabilities)")
        
        print("\n✅ Model test completed successfully!")
        return True
        
    except Exception as e:
        print(f"\n❌ Error testing model: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_saved_model()
    if success:
        print("\n🎉 Your saved model is working correctly!")
    else:
        print("\n❌ There was an issue with the saved model.")
    
    input("\nPress Enter to exit...")
