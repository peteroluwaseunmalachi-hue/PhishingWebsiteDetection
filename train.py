import pandas as pd
from scipy.io import arff
from sklearn.ensemble import RandomForestClassifier
import pickle

print("Loading dataset...")

# 1. Load the ARFF file
data, meta = arff.loadarff('Training Dataset.arff')
df = pd.DataFrame(data)

# 2. Convert data to integers
for col in df.columns:
    df[col] = df[col].astype(int)

# 3. Separate features and target
X = df.iloc[:, :-1] 
y = df.iloc[:, -1]  

print("Training the model... (this might take a few seconds)")

# 4. Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 5. Save the model
with open('phishing_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained successfully and saved as 'phishing_model.pkl'!")