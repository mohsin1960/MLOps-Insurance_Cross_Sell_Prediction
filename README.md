🛡️ Insurance Sell Prediction - MLOps Pipeline

Python (https://img.shields.io/badge/Python-3.8+-blue.svg) (https://www.python.org/)
Scikit-Learn (https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg) (https://scikit-learn.org/)
License (https://img.shields.io/badge/License-MIT-green.svg) (LICENSE)

An end-to-end Machine Learning pipeline designed to predict insurance sales behavior. This project implements a modular MLOps architecture, ensuring a clean separation between data ingestion, preprocessing, model training, and evaluation.

🚀 Project Overview

The goal of this project is to predict whether a customer will purchase insurance based on their demographic and behavioral data. The pipeline handles real-world data challenges such as class imbalance (using SMOTE) and data outliers (using IQR).

✨ Key Features

- Modular Architecture: Each stage of the ML lifecycle is encapsulated in its own class.
- Centralized Configuration: Model hyperparameters and file paths are managed via config.yaml.
- Robust Preprocessing:
  - Automated handling of missing values (Imputation).
  - Currency cleaning and type casting.
  - Outlier removal using the Interquartile Range (IQR) method.
- Imbalance Handling: Integrated SMOTE (Synthetic Minority Over-sampling Technique) to handle skewed target classes.
- Pipeline Serialization: Saves the entire preprocessing and model chain as a single .pkl file for easy deployment.

---

📁 Project Structure
<img width="515" height="288" alt="image" src="https://github.com/user-attachments/assets/383cd69f-b5da-41fe-b023-bd7173398d58" />



---

⚙️ Workflow Execution Flow

The pipeline is executed via main.py in the following sequence:

main.py $\rightarrow$ Ingest $\rightarrow$ Clean $\rightarrow$ Train $\rightarrow$ Predict

1. Ingestion: Loads raw CSV data based on paths defined in config.yaml.
2. Cleaning: Performs feature dropping, currency normalization, median filling for ages, and IQR-based outlier removal.
3. Training:
   - Builds a ColumnTransformer for Scaling and One-Hot Encoding.
   - Applies SMOTE to balance classes.
   - Fits the selected ML model.
   - Exports the finalized pipeline to models/model.pkl.
4. Prediction: Loads the saved model and evaluates it against the test set, outputting an Accuracy Score, ROC AUC, and a detailed Classification Report.

---

🛠️ Getting Started

Installation

1. Clone the repository:
git clone https://github.com/your-username/Insurance-Sell-Prediction.git
cd Insurance-Sell-Prediction
2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt

Usage

To run the complete pipeline:
python main.py

Configuration

You can change the model or hyperparameters without modifying the code by editing config.yaml:
model:
  name: GradientBoostingClassifier # Options: DecisionTreeClassifier, RandomForestClassifier, etc.
  params:
    max_depth: 5
    n_estimators: 100
  store_path: models/

---

📊 Model Evaluation

The pipeline supports multiple models. Based on testing, the GradientBoostingClassifier typically provides the best trade-off between Accuracy and ROC AUC for this imbalanced dataset.




These goals require balancing:

* Accuracy
* ROC AUC
* Precision
* Recall
* F1-Score

---

# 📈 Model Performance Comparison

| Metric                | 🌳 Decision Tree | 🚀 Gradient Boosting | 🌲 Random Forest | 🏆 Winner        |
| --------------------- | ---------------: | -------------------: | ---------------: | ---------------- |
| **Accuracy**          |       **0.8333** |               0.8306 |           0.6343 | 🌳 Decision Tree |
| **ROC AUC**           |           0.7148 |               0.7201 |       **0.7247** | 🌲 Random Forest |
| **Class 1 Recall**    |             0.56 |                 0.57 |         **0.84** | 🌲 Random Forest |
| **Class 1 Precision** |             0.37 |             **0.37** |             0.23 | 🌳 DT / 🚀 GB    |
| **Class 1 F1-Score**  |         **0.45** |             **0.45** |             0.36 | 🌳 DT / 🚀 GB    |

---

# 📌 Business Decision Matrix

| Business Objective                 | Recommended Model                     | Reason                                     |
| ---------------------------------- | ------------------------------------- | ------------------------------------------ |
| 🎯 Maximum overall accuracy        | **Decision Tree**                     | Highest accuracy: 83.33%                   |
| ⚖️ Balanced performance            | **Gradient Boosting**                 | Strong accuracy + balanced Class 1 metrics |
| 📈 Find maximum number of buyers   | **Random Forest**                     | Highest buyer recall: 84%                  |
| 💰 Generate more potential leads   | **Random Forest**                     | Minimizes missed buyers                    |
| 🔎 More reliable buyer predictions | **Decision Tree / Gradient Boosting** | Higher precision: 37%                      |
| 📊 Best discrimination / ranking   | **Random Forest**                     | Highest ROC AUC: 0.7247                    |

---

# 💡 Key Business Insight

The results demonstrate an important machine learning principle:

> **The model with the highest accuracy is not necessarily the best model for the business.**

For example:

```text
Decision Tree
Accuracy → 83.33%
Recall   → 56%
```
