import joblib

def load_model():
    model = joblib.load('path/to/your/model.pkl')
    return model

def predict(data):
    model = load_model()
    prediction = model.predict(data)
    return prediction
