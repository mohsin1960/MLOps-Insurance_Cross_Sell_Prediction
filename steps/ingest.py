import pandas as pd
import yaml

class Ingestion:  
    def __init__(self):  # CONSTRUCTOR: It call every time when create object of that class
        self.config = self.load_config()
        # load_config() is a method of class Ingestion which is loading config.yaml
        # means  config = config.yaml 

    def load_config(self):  ######## Load Config METHOD 
        with open("config.yml", "r") as file:
            return yaml.safe_load(file)
            ###### Read the yaml file and convert it into python object 

    def load_data(self):  ####### Load Data METHOD
        train_data_path = self.config['data']['train_path']
        test_data_path = self.config['data']['test_path']
        train_data = pd.read_csv(train_data_path)
        test_data = pd.read_csv(test_data_path)
        return train_data, test_data