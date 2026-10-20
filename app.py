from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        features = []
        # Get the 30 features from the form
        for i in range(30):
            val = int(request.form.get(f'feature{i}'))
            features.append(val)
            
        # Make the prediction
        prediction = model.predict([features])[0]
        
        # Format the result
        if prediction == -1:
            result = "⚠️ PHISHING DETECTED (Malicious Website)"
            color = "red"
        else:
            result = "✅ SAFE (Legitimate Website)"
            color = "green"
            
        return render_template('index.html', result=result, color=color)

if __name__ == '__main__':
    app.run(debug=True)