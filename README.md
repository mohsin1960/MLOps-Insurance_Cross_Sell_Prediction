

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
