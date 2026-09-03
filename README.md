📦 Project Structure Documentation: Insurance Sell Prediction

This project is a Machine Learning pipeline designed to predict insurance sales. It follows a modular MLOps structure where each stage of the pipeline (Ingestion, Cleaning, Training, and Prediction) is isolated into its own class.

📁 Directory Layout

Insurance_Sell_Prediction/
├── data/               # Raw dataset storage
│   ├── train.csv       # Training data
│   └── test.csv        # Testing data
├── models/             # Saved model artifacts
│   └── model.pkl       # The trained pipeline (preprocessor + model)
├── steps/              # Pipeline stage implementations
│   ├── __init__.py     # Makes 'steps' a Python package
│   ├── ingest.py       # Data loading logic
│   ├── clean.py        # Data preprocessing & outlier removal
│   ├── train.py        # Model training & pipeline construction
│   └── predict.py      # Model evaluation & performance metrics
├── config.yaml         # Central configuration (paths, hyperparameters)
├── main.py             # Execution entry point (Orchestrator)
├── dataset.py          # Utility script to generate sample data
└── requirements.txt    # Project dependencies

🚀 Execution Flow (How it starts)

The project starts at main.py. It acts as the orchestrator that calls the different stages in a specific sequence:

1. main.py $\rightarrow$ steps/ingest.py:
   - Loads config.yaml.
   - Reads train.csv and test.csv from the data/ folder.
2. main.py $\rightarrow$ steps/clean.py:
   - Handles missing values (Imputation).
   - Cleans currency strings (e.g., removing '£').
   - Removes outliers using the Interquartile Range (IQR) method.
3. main.py $\rightarrow$ steps/train.py:
   - Creates a ColumnTransformer pipeline (Scaling & One-Hot Encoding).
   - Applies SMOTE to handle class imbalance.
   - Trains the selected model (Decision Tree, Random Forest, or Gradient Boosting).
   - Saves the entire pipeline as model.pkl in the models/ folder.
4. main.py $\rightarrow$ steps/predict.py:
   - Loads the saved model.pkl.
   - Predicts outcomes for the test set.
   - Calculates and prints Accuracy, ROC AUC, and a Classification Report.

🛠 Key Components

- Configuration-Driven: By changing config.yaml, you can switch models or change data paths without touching the code.
- Pipeline-Based: The project uses imblearn.pipeline.Pipeline, ensuring that preprocessing steps (scaling/encoding) are saved along with the model to prevent data leakage during prediction.
- Data Generation: dataset.py is a utility used to create synthetic classification data for testing the pipeline.

=======================================================================================================================================================


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
