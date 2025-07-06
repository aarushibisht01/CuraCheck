from backend.app import app, load_and_train_model

# Initialize model for Vercel
load_and_train_model()

# Vercel serverless function handler
def handler(request):
    # Return the Flask app for serverless execution
    return app
