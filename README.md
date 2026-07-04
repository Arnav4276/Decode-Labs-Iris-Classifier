# 🌸 IRIS // ML Classification Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A dedicated, full-stack machine learning pipeline built to analyze CSV datasets like the classic Iris Benchmark Dataset. This project bridges a robust Python/Scikit-Learn backend with a modern, terminal-inspired frontend dashboard, allowing users to upload datasets, trigger classification algorithms, and view performance metrics in real-time.

*Developed as part of the DecodeLabs Data Science & Machine Learning Internship (Project 2).*

---

## ✨ Key Features & Architecture

* **Algorithmic Engine:** Utilizes the **K-Nearest Neighbors (KNN)** algorithm (K=5) to classify species or categories based on numerical features.
* **Dynamic Data Processing:** Automatically handles missing IDs, drops non-numerical columns, and splits data into training/testing sets (80/20 split).
* **Data Preprocessing:** Implements `StandardScaler` to normalize feature variance and enforce strict matrix shapes for mathematical stability.
* **RESTful API Bridge:** A lightweight Flask backend that receives file uploads, executes the Scikit-Learn pipeline, and serves analytical results via JSON payloads.
* **Reactive UI/UX:** A custom HTML/CSS/JS frontend featuring a sleek, dark-mode, cyberpunk terminal aesthetic that displays Dataset Insights, Accuracy, F1-Scores, Precision, Recall, and a dynamic Confusion Matrix.
* **Separation of Concerns:** Clean architecture ensuring the frontend interface and backend ML brain operate independently (connected via CORS).

---

## 🛠️ Tech Stack

**Backend:**

* Python 3.8+
* Flask & Flask-CORS
* Scikit-Learn
* Pandas
* NumPy

**Frontend:**

* HTML5
* CSS3 (Custom Glassmorphism/Terminal UI)
* Vanilla JavaScript (Fetch API)

---

## 🗂️ Project Structure

```text
📁 Decode-Labs-Iris-Classifier/
│
├── 📁 backend/
│   ├── app.py               # Flask server and API endpoint routing
│   └── ml_pipeline.py       # Core Scikit-Learn logic and model evaluation
│
├── 📁 frontend/
│   ├── index.html           # Structure and terminal interface UI
│   ├── style.css            # Dark-mode, cyberpunk glassmorphism styling
│   └── script.js            # Fetch API logic and DOM manipulation
│
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

Follow these instructions to get the project running locally.

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Decode-Labs-Iris-Classifier.git
   cd Decode-Labs-Iris-Classifier
   ```

2. **Set up the backend:**

   Navigate to the backend folder and install the required Python packages. It is recommended to use a virtual environment.

   ```bash
   cd backend
   pip install flask flask-cors pandas numpy scikit-learn
   ```

3. **Run the Flask server:**

   ```bash
   python app.py
   ```

   > The server will start running at `http://127.0.0.1:5000`

4. **Launch the frontend:**
   Open a new terminal or file explorer. Navigate to the `frontend` folder and open `index.html` directly in any modern web browser.
   *(Alternatively, you can use a tool like Live Server in VS Code).*

---

## 🎮 Usage Guide

1. Open the frontend dashboard (`index.html`) in your browser.
2. Click on **"Upload CSV file"** and select a formatted dataset (e.g., `iris.csv`).
   * *Note: The target classification label must be the last column in the CSV.*
3. Click the **"INITIALIZE ANALYSIS"** button.
4. The dashboard will display a loading spinner while the backend processes the file.
5. View the real-time results in the dashboard cards:
   * **Dataset Overview**: Total samples, features, and target class distribution.
   * **Model Performance**: Accuracy, F1 Score, Precision, and Recall.
   * **Confusion Matrix**: A dynamically generated grid showing true vs. predicted classifications.

---

## 📡 API Reference

The backend exposes a single endpoint for dataset analysis:

* **URL:** `/analyze`
* **Method:** `POST`
* **Body:** `multipart/form-data` with a key `dataset` containing the CSV file.
* **Success Response:**
  * **Code:** 200 OK
  * **Content:**
  
    ```json
    {
      "status": "success",
      "data": {
        "eda": { "total_rows": 150, "total_features": 4, "class_distribution": {"Iris-setosa": 50, ...} },
        "metrics": { "accuracy": 1.0, "f1_score": 1.0, "precision": 1.0, "recall": 1.0 },
        "confusion_matrix": [[...], [...]]
      }
    }
    ```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

This project is licensed under the MIT License.
