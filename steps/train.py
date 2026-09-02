import os
import joblib
import yaml
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline 
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier

class Trainer:
    def __init__(self):
        self.config = self.load_config()
        self.model_name = self.config['model']['name']
        self.model_params = self.config['model']['params']
        self.model_path = self.config['model']['store_path']
        self.pipeline = self.create_pipeline()

    ######### Load Method ##########
    def load_config(self):
        with open('config.yml', 'r') as config_file:
            return yaml.safe_load(config_file)

    ######### Pipeline Method ###########
    def create_pipeline(self):
        preprocessor = ColumnTransformer(transformers=[
            # Apply MinMaxScalar to "AnnualPremium" column, the transfomation name is "minmax"
            ('minmax', MinMaxScaler(), ['AnnualPremium']),

            # Apply StandardScalar to "Age" and "RegionID".
            ('standardize', StandardScaler(), ['Age','RegionID']),

            # Apply one-hot encoding to Categorical columns
            # handle_unknown useful when new catogories appear during pridiction
            ('onehot', OneHotEncoder(handle_unknown='ignore'), ['Gender', 'PastAccident']),
        ])

        # Creating SMOTE object 
        # SMOTE try to make the minority class equal in size to majority class
        smote = SMOTE(sampling_strategy=1.0)

        # This is the python dictionay that maps the names of config
        # file to actual python classes 
        # This is usefull, when need change, only change in config file.
        model_map = {
            'RandomForestClassifier': RandomForestClassifier,
            'DecisionTreeClassifier': DecisionTreeClassifier,
            'GradientBoostingClassifier': GradientBoostingClassifier
        }
    
        model_class = model_map[self.model_name]
        # ** means unpack the dictionary of parameters.
        model = model_class(**self.model_params)

        # Now Creating a pipeline 
        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('smote', smote),
            ('model', model)
        ])
        return pipeline

###### TRAINING PIPELINE #######   

#            Input Data
#                 │
#                 ▼
#       ┌───────────────────┐
#       │   Preprocessor    │
#       │                   │
#       │ AnnualPremium     │ → MinMaxScaler
#       │ Age, RegionID     │ → StandardScaler
#       │ Gender, Accident  │ → OneHotEncoder
#       └─────────┬─────────┘
#                 │
#                 ▼
#             ┌───────┐
#             │ SMOTE │
#             └───┬───┘
#                 │
#                 ▼
#             ┌────────┐
#             │ Model  │
#             └────────┘

    ######## Feature Extraction Method ########
    def feature_target_separator(self, data):

        # Take every row and every column except the last column 
        X = data.iloc[:, :-1]

        # Takes every row in the last column 
        y = data.iloc[:, -1]
        return X, y

    ######## Training Data Method #########
    def train_model(self, X_train, y_train):
        self.pipeline.fit(X_train, y_train)

    ######## Save pipeline Method ########
    def save_model(self):
        model_file_path = os.path.join(self.model_path, 'model.pkl')
        joblib.dump(self.pipeline, model_file_path)