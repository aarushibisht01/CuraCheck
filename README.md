# 🩺 CuraCheck - AI-Powered Health Diagnosis System

LIVE LINK: https://curacheck.onrender.com/

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.3.3-green.svg" alt="Flask">
  <img src="https://img.shields.io/badge/scikit--learn-1.3.0-orange.svg" alt="scikit-learn">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status">
</p>

<p align="center">
  <strong>Your smart health companion for early diagnosis using machine learning</strong>
</p>

---

## 🌟 Overview

CuraCheck is an intelligent health diagnosis system that uses machine learning to predict potential diseases based on symptoms. Built with Flask and scikit-learn, it provides a user-friendly web interface for symptom input and delivers accurate health predictions.

### ✨ Key Features

- 🤖 **AI-Powered Diagnosis**: Advanced K-Nearest Neighbors algorithm for accurate predictions
- 🎯 **132+ Symptoms**: Comprehensive symptom database for precise diagnosis
- 🌐 **Web Interface**: Beautiful, responsive frontend for easy interaction
- ⚡ **Real-time Predictions**: Instant health assessments with confidence scores
- 📊 **Model Persistence**: Trained models are saved and reused for efficiency
- 🔄 **Model Retraining**: API endpoint for updating the model with new data
- 🏥 **40+ Diseases**: Covers a wide range of medical conditions

## 🏗️ Architecture

```
CuraCheck/
├── 🎨 frontend/           # Web interface
│   ├── index.html         # Main webpage
│   ├── style.css          # Styling
│   ├── script.js          # Frontend logic
│   └── images/            # UI assets
├── 🧠 backend/            # AI engine
│   ├── app.py             # Flask API server
│   ├── source/            # Training data
│   │   ├── Training.csv   # 4,920+ training samples
│   │   └── Testing.csv    # Test dataset
│   └── models/            # Trained ML models
├── ☁️ api/                # Serverless deployment
└── 📋 Deployment configs  # Vercel, Heroku, Render
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/curacheck.git
   cd curacheck
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python backend/app.py
   ```

4. **Open your browser**
   ```
   http://localhost:5000
   ```

## 📱 How to Use

1. **Access the Web Interface**: Navigate to the homepage
2. **Select Symptoms**: Check all symptoms you're experiencing
3. **Get Diagnosis**: Click "Diagnose" for AI prediction
4. **View Results**: See predicted condition with confidence score
5. **Health Tips**: Browse general health recommendations

## 🔬 Machine Learning Model

### Algorithm: K-Nearest Neighbors (KNN)
- **Training Data**: 4,920+ medical records
- **Features**: 132 symptoms (binary: 0/1)
- **Hyperparameter Tuning**: GridSearchCV optimization
- **Cross-Validation**: 6-fold CV for robust training
- **Metrics**: Euclidean, Manhattan, Chebyshev distances

### Model Performance
- **Accuracy**: High precision on test dataset
- **Features**: 132 symptom indicators
- **Diseases**: 40+ medical conditions
- **Training Time**: ~2-3 minutes (with optimization)

## 🛠️ API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main web interface |
| `/api` | GET | API information |
| `/health` | GET | System health check |
| `/symptoms` | GET | List all available symptoms |
| `/predict` | POST | Disease prediction |
| `/retrain` | POST | Retrain the ML model |

### Example API Usage

```python
import requests

# Predict disease
response = requests.post('http://localhost:5000/predict', json={
    'symptoms': [1, 0, 1, 0, ...] # 132 binary values
})

result = response.json()
print(f"Prediction: {result['prediction']}")
print(f"Confidence: {result['confidence']}")
```

## 🌐 Deployment Options

### 1. Vercel (Serverless)
```bash
npm install -g vercel
vercel login
vercel
```

### 2. Heroku (Container)
```bash
heroku create your-app-name
git push heroku main
```

### 3. Render (Recommended)
1. Connect GitHub repository
2. Configure: `python backend/app.py`
3. Auto-deploy on push

### 4. Railway
- One-click deployment
- Auto-detects Python
- Free tier available

## ⚙️ Configuration

### Environment Variables
```bash
PORT=5000                    # Server port
PYTHONPATH=/var/task        # Python path (serverless)
```

### Model Configuration
```python
# KNN Parameters (auto-optimized)
n_neighbors: [1, 3, 5, 7, 9, 11]
metric: ['euclidean', 'manhattan', 'chebyshev']
cv: 6
```

## 🧪 Testing

Run the test suite:
```bash
python backend/test_model.py
```

Check model performance:
```bash
curl http://localhost:5000/health
```

## 📊 Dataset Information

- **Source**: Medical symptom-disease dataset
- **Size**: 4,920+ training samples
- **Features**: 132 symptoms (itching, skin_rash, fever, etc.)
- **Target**: 40+ diseases (Fungal infection, Allergy, GERD, etc.)
- **Format**: CSV with binary encoding

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔒 Disclaimer

⚠️ **Important**: CuraCheck is for educational and informational purposes only. It should not replace professional medical advice, diagnosis, or treatment. Always consult qualified healthcare providers for medical concerns.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Medical dataset contributors
- scikit-learn community
- Flask framework developers
- Open source healthcare initiatives

## 📈 Roadmap

- [ ] Mobile app development
- [ ] Real-time symptom tracking
- [ ] Integration with wearable devices
- [ ] Multi-language support
- [ ] Doctor consultation booking
- [ ] Medical history storage

---

<p align="center">
  <strong>🌟 If you found CuraCheck helpful, please star this repository! 🌟</strong>
</p>

<p align="center">
  Made with ❤️ for better healthcare accessibility
</p>
