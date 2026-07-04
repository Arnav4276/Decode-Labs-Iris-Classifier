import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score, precision_score, recall_score

def run_analysis(file_object):
    print("--- 🚀 INITIATING ADVANCED ML PIPELINE ---")
    
    # ==========================================
    # 1. INPUT & EDA (Exploratory Data Analysis)
    # ==========================================
    try:
        df = pd.read_csv(file_object)
    except Exception as e:
        raise ValueError(f"Could not read the CSV file. Error: {e}")

    # Clean IDs if they exist
    if 'Id' in df.columns:
        df = df.drop('Id', axis=1)
    elif 'id' in df.columns:
        df = df.drop('id', axis=1)

    X = df.iloc[:, :-1]  
    y = df.iloc[:, -1]   

    # Extract dynamic insights for the frontend dashboard
    dataset_insights = {
        "total_rows": int(df.shape[0]),
        "total_features": int(X.shape[1]),
        # Convert pandas value counts to a standard dictionary
        "class_distribution": y.value_counts().to_dict() 
    }

    # Automatically drop text columns
    X = X.select_dtypes(include=['number'])
    if X.shape[1] == 0:
        raise ValueError("No numerical features found! Ensure your CSV has valid numbers.")

    # ==========================================
    # 2. PROCESS: Splitting & Scaling
    # ==========================================
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=True)
    
    X_train_array = np.array(X_train)
    X_test_array = np.array(X_test)

    if X_train_array.ndim == 1:
        X_train_array = X_train_array.reshape(-1, 1)
        X_test_array = X_test_array.reshape(-1, 1)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_array) 
    X_test_scaled = scaler.transform(X_test_array)       

    # ==========================================
    # 3. PROCESS: The Algorithm (KNN)
    # ==========================================
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train_scaled, y_train)
    predictions = model.predict(X_test_scaled)

    # ==========================================
    # 4. OUTPUT: Extended Validation Metrics
    # ==========================================
    cm = confusion_matrix(y_test, predictions)
    
    # We use 'weighted' to handle imbalanced multi-class datasets safely
    metrics = {
        "f1_score": round(f1_score(y_test, predictions, average='weighted', zero_division=0), 4),
        "accuracy": round(accuracy_score(y_test, predictions), 4),
        "precision": round(precision_score(y_test, predictions, average='weighted', zero_division=0), 4),
        "recall": round(recall_score(y_test, predictions, average='weighted', zero_division=0), 4)
    }

    # Package everything into a massive JSON payload
    return {
        "eda": dataset_insights,
        "metrics": metrics,
        "confusion_matrix": cm.tolist() 
    }