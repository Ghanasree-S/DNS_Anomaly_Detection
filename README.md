# DNS_Anomaly_Detection

## 🚨 Detecting Malicious DNS Traffic using Machine Learning

This project detects anomalies in DNS traffic using the **CIRA-CIC-IDS2017** dataset. It classifies DNS flows as **Benign** or **Anomalous** using a trained **Random Forest** classifier. The project includes a **Flask-based web interface** for uploading DNS log CSV files and viewing predictions.

---

## ⚙️ Features

- **Dataset Loader**: Loads and merges multiple DNS CSV files.
- **Data Cleaning**: Handles NaNs, infinite values, and whitespace issues.
- **Binary Classification**: Detects anomalies by labeling flows as Benign (`1`) or Anomalous (`0`).
- **Model Training**: Trains a `RandomForestClassifier` using `scikit-learn`.
- **Flask Web App**: Upload DNS logs and view prediction results in the browser.
- **Confidence Score**: Displays anomaly probability for each predicted row.

---

## 📦 Prerequisites

Ensure the following libraries are installed:

```bash
pip install -r requirements.txt
```
## 🧠 How It Works

- **Text Extraction**: Loads and concatenates all CSVs from the `CIRA-CIC-IDS2017` folder.
- **Data Cleaning**: Removes nulls and infinities, cleans column names.
- **Label Encoding**: Maps `'BENIGN'` label to `1`, all others to `0`.
- **Model Training**: Fits a balanced `RandomForestClassifier`.
- **Prediction**: Samples 20 random rows from the uploaded file, predicts, and shows:
  - `Normal` or `Anomaly`
  - Anomaly probability

---

## 🌐 API Endpoints

| Endpoint   | Method | Description                            |
|------------|--------|----------------------------------------|
| `/`        | GET    | Homepage to upload DNS CSV files       |
| `/upload`  | POST   | Handles file uploads and shows results |

---

## 🧪 Example Usage

1. Upload a `.csv` file containing DNS logs from the UI.
2. The app will:
   - Clean the data
   - Sample 20 rows
   - Predict whether each row is `Normal` or `Anomalous`
3. View results in a styled HTML table with prediction confidence.

---

## 📁 Dataset

The model is trained on the **CIRA-CIC-IDS2017** dataset, which contains real-world DNS logs from benign and attack scenarios.  
It includes attacks like **DDoS**, **PortScan**, and **Botnet** activity.

> ⚠️ *Due to file size, consider testing with smaller CSVs during development.*

---

## ✅ Conclusion

This project offers a practical tool to detect DNS anomalies using machine learning.  
It's ideal for **cybersecurity students**, **researchers**, and **analysts** looking to identify malicious behavior in network traffic using a web-based ML solution.
