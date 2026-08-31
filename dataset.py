# Sample data extraction file which generate a classification dataset using sklearn.datasets
from sklearn.datasets import make_classification
import pandas as pd
import os

def extract_data():
    if not os.path.exists("data"):                  #if data folder does'nt exists
        os.mkdir("data")                            # Create data directory 
    
    append_mode = os.path.isfile("data/train.csv")  #if file data/train.csv exits, then append data

    num_datasets = 10 if not append_mode else 1     #if not append_mode means if data not present, then num_dataset=10, else 1

    for _ in range(num_datasets):                   # Loop run num_datasets times (10 or 1)
        X, y = make_classification(n_samples=10000, n_features=10, n_informative=8, n_redundant=2, n_classes=2, random_state=42)
        # n_samples(Generate Rows), n_features (Generate Columns), n_informative (out of 10 features 8 are informative to detemine target)
        # n_classes (values may be 0 or 1) , random_state (should be same data)

        df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])]) 
        # Convert X into pandas data frames 
        # (x.shapte[1] means (rows, columns) ==> (10000,10)  
        # so x.shape[1] = 10 
        # feature_0, feature_1, feature_2..... feature_9

        df['target'] = y                            # It creates a new column name "target"
        
        train_data = df.iloc[:8000]
        test_data = df.iloc[8000:]
        
        train_data.to_csv("data/train.csv", mode="a", header=not append_mode, index=False)
        test_data.to_csv("data/test.csv", mode="a", header=not append_mode, index=False)

    print("Extracted data from source successfully")

if __name__ == "__main__":
    extract_data()