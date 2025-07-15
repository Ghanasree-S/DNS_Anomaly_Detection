import pandas as pd
import glob
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load all CSV files from the directory
csv_files = glob.glob(r"/CIRA-CIC-IDS2017/*.csv")

# Check if files were found
if len(csv_files) == 0:
    print("No CSV files found in the specified folder.")
else:
    print(f"Found {len(csv_files)} CSV files.")

# Concatenate all CSV files into a single DataFrame
df_list = []
for file in csv_files:
    df = pd.read_csv(file)
    # Strip leading and trailing spaces from column names
    df.columns = df.columns.str.strip()
    df_list.append(df)

# Combine all DataFrames into one
if df_list:
    df_combined = pd.concat(df_list, ignore_index=True)
    print("DataFrames successfully concatenated.")
else:
    print("No DataFrames to concatenate.")
    exit()  # Exit if there is no data

# Print columns after cleaning up whitespace
print("Columns in the dataset:")
print(df_combined.columns)

# Handle missing or infinite values
df_combined.replace([float('inf'), float('-inf')], float('nan'), inplace=True)
df_combined.dropna(inplace=True)

# Verify that there are no more missing values
print(f"Missing values after cleaning: {df_combined.isna().sum().sum()}")

# Check if 'Label' column exists
if 'Label' not in df_combined.columns:
    print("The 'Label' column is missing from the dataset.")
    exit()  # Exit if 'Label' is not present

# Check the unique values in the 'Label' column
print("Unique values in 'Label' column:")
print(df_combined['Label'].unique())

# Create a binary 'Label_Bot' column: 1 for 'Bot' and 0 for others
df_combined['Label_BENIGN'] = df_combined['Label'].apply(lambda x: 1 if x == 'BENIGN' else 0)

# Extract features (all columns except 'Label' and 'Label_Bot')
X = df_combined.drop(columns=['Label', 'Label_BENIGN'])

# Extract target labels (use 'Label_Bot' column as the target)
y = df_combined['Label_BENIGN']

# Split data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model (Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')

# Train the model
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the trained model to a file (optional but useful for future use)
joblib.dump(model, 'dns_anomaly_detection_model.pkl')  # Saves model to current directory