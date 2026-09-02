import numpy as np
from sklearn.impute import SimpleImputer  # Imputer is filling missing values

class Cleaner:
    # CONSTRUCTOR: Run automatically, when create object from class "Cleaner"
    def __init__(self): 
        self.imputer = SimpleImputer(strategy='most_frequent', missing_values=np.nan)
        # "np.nan" means missing numerical values, Replance with NaN
        # "startegy='most_frequent'" is Replace each missing value with the most frequently occurring value in that column.
        # Let suppose => male, female, NaN, male, male  then  NaN replaced with "male" 

    def clean_data(self, data):
        data.drop(['id','SalesChannelID','VehicleAge','DaysSinceCreated'], axis=1, inplace=True)
        # Droping the specified columns 
        # axis "0" means dropping row and "1" means dropping columns 

        data['AnnualPremium'] = data['AnnualPremium'].str.replace('£', '').str.replace(',', '').astype(float)
        # Replacing string with Numerical values of Column "AnnualPremium"
        # "£12,00" => "12,00" => "1200" => 1200.0

        # Run loop for 2 columns "Gender" & "RegionID"
        for col in ['Gender', 'RegionID']:
             data[col] = self.imputer.fit_transform(data[[col]]).flatten()
            # "Fit_transform" studying the column 
            # "data[[col]]" read one column of above 2 
            # ".flatten()" convert 2D colunm into a single 
            # "imputer" filling the missing values 

        data['Age'] = data['Age'].fillna(data['Age'].median())
        # Filling the missing values by taking median of available values 

        data['HasDrivingLicense']= data['HasDrivingLicense'].fillna(1)
        # Filling the missing value with "1"

        data['Switch'] = data['Switch'].fillna(-1)
        # Filling "-1" means => Missing, Unknown, Not available

        data['PastAccident'] = data['PastAccident'].fillna("Unknown", inplace=False)
        # Filling the missing with "Unknown"


        ################# Removing Remove premium outliers ###############
        
        Q1 = data['AnnualPremium'].quantile(0.25)
        # Q1 means 25th percentile 

        Q3 = data['AnnualPremium'].quantile(0.75)
        # Q1 means 25th percentile 

        IQR = Q3 - Q1
        # Suppose Q1=20000 , Q2=40000
        # IQR = 40000 - 20000 = 20000

        upper_bound = Q3 + 1.5 * IQR
        # upper_bound = 40000 + 1.5 * 20000 = 70000

        data = data[data['AnnualPremium'] <= upper_bound]
        # This keeps values that are "AnnualPremium" <= upper_bound
        # Suppose AnnualPremium => 30000, 45000, 65000, 90000
        # Keep only 30000, 45000, 65000 but remove 90000
        
        return data