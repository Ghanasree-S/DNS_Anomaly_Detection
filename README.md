\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\usepackage{hyperref}
\usepackage{longtable}
\geometry{margin=1in}
\title{DNS Anomaly Detection Project}
\author{Ghanasree S}
\date{}

\begin{document}

\maketitle

\section*{Overview}
This project focuses on detecting anomalies in DNS traffic using machine learning techniques. It leverages the CIRA-CIC-IDS2017 dataset and implements a Random Forest classifier to distinguish between benign and anomalous DNS queries. A Flask-based web application enables interactive CSV uploads and anomaly detection.

\section*{Features}
\begin{itemize}
    \item \textbf{Multi-CSV Loader:} Loads and merges DNS-related CSVs from the dataset.
    \item \textbf{Data Cleaning:} Replaces infinite values and removes rows with missing data.
    \item \textbf{Label Binarization:} Classifies traffic as \texttt{Benign} (1) or \texttt{Anomalous} (0).
    \item \textbf{Random Forest Model:} Trained on cleaned data for robust detection.
    \item \textbf{Web Interface:} Flask app allows file uploads and live predictions.
    \item \textbf{Result Display:} Shows predictions with anomaly probabilities in a table format.
\end{itemize}

\section*{Prerequisites}
Install the required packages via:
\begin{verbatim}
pip install -r requirements.txt
\end{verbatim}
Or manually:
\begin{verbatim}
pip install pandas numpy scikit-learn flask joblib
\end{verbatim}

\section*{Running the Project}
\begin{enumerate}
    \item Clone the repository:
    \begin{verbatim}
    git clone https://github.com/Ghanasree-S/DNS_Anomaly_Detection.git
    cd DNS_Anomaly_Detection
    \end{verbatim}
    
    \item Run the Flask app:
    \begin{verbatim}
    python app.py
    \end{verbatim}
    
    \item Open your browser and visit:
    \url{http://127.0.0.1:5000/}
\end{enumerate}

\section*{Model Training}
The \texttt{train.py} script:
\begin{itemize}
    \item Loads and merges DNS-related logs.
    \item Cleans the dataset.
    \item Converts the \texttt{Label} column into a binary class (\texttt{BENIGN} = 1, others = 0).
    \item Trains a Random Forest classifier.
    \item Saves the model as \texttt{dns\_anomaly\_detection\_model.pkl}.
\end{itemize}

\section*{Web App Functionality}
The \texttt{app.py} Flask script:
\begin{itemize}
    \item Accepts CSV uploads with DNS traffic.
    \item Randomly selects 20 rows for prediction.
    \item Predicts whether the traffic is normal or anomalous.
    \item Displays results in a table with probability scores.
\end{itemize}

\section*{Sample Output Table}
\begin{longtable}{|l|l|l|}
\hline
\textbf{Feature} & \textbf{Prediction} & \textbf{Anomaly Probability} \\
\hline
8.8.8.8, Port 53, ... & Anomaly & 0.87 \\
\hline
\end{longtable}

\section*{Dataset}
The model uses DNS-related traffic logs from the \textbf{CIRA-CIC-IDS2017} dataset, covering various days of normal and attack traffic.

\section*{Conclusion}
This project demonstrates how machine learning can be used to automatically detect DNS anomalies, assisting network security professionals in identifying potential threats in near real time.

\end{document}
