import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
from datetime import datetime

from models import MyRegression, MyTrees
from preprocess import Preprocssor
from plot import Plot, MyXGboostResult


PROJECT_DIR = 'app/rob'

class MyModel(object):
    def __init__(self):
        self.data_dir = os.path.join(PROJECT_DIR, 'data')
        self.df = pd.read_csv(os.path.join(self.data_dir,'mydata.csv'))
        
        self.cols = self.df.columns.tolist()
        happiness = self.cols[-2]
        
        self.preprocesser = Preprocssor(self.df, happiness)
        self.preprocessed_data = self.preprocesser.get_dataframe()
        self.preprocessed_df = pd.DataFrame(self.preprocessed_data, columns=self.cols)
        
        
    def run_xgboost(self):
        X_train, X_test, y_train, y_test = self.preprocesser.get_ready(standraize=False)
        tree_model = MyTrees(X_train, X_test, y_train, y_test)
        
        model = tree_model.my_xgboost()
        ploter = MyXGboostResult(model)
        ploter.save_feature_importances()
        ploter.save_heatmap()
        
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    

    
            
   
   
   
   
   
   
