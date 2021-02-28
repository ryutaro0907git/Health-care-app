from collections import defaultdict

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split



class Preprocssor(object):
    def __init__(self, dataframe, target_name):
        self.dataframe = dataframe
        self.target_name = target_name
        
        self.columns = dataframe.columns
        
        self.d = defaultdict(LabelEncoder)
        
    def get_ready(self, standraize=True):
        label_encoded_df = self.my_encoder(self.dataframe)
        nonnal_df = self.my_fillna(label_encoded_df)
        y = self.get_target(nonnal_df)
        X = self.my_col_dropper(nonnal_df, self.target_name)
        
        X_train, X_test, y_train, y_test = self.my_splitter(X, y)
        
        if standraize:
            X_train = self.standaraizer(X_train)
            x_test = self.standaraizer(X_test)
        

        return X_train, X_test, y_train, y_test
    
    def get_dataframe(self, standraize=True):
        label_encoded_df = self.my_encoder(self.dataframe)
        df = self.standaraizer(label_encoded_df)
        
        return df 
        
    def my_encoder(self, df):
        encoded_df = df.apply(lambda x: self.d[x.name].fit_transform(x))
        
        return encoded_df
    
    def my_decoder(self, encoded_df):
        # Inverse the encoded
        origianl_df = encoded_df.apply(lambda x: self.d[x.name].inverse_transform(x))

    def my_col_dropper(self, df, name_of_col):
        df = df.drop(name_of_col, axis=1)
        
        return df
        
    def standaraizer(self, df): 
        scaler = StandardScaler().fit(df) 
        rescaled_data = scaler.transform(df)

        return rescaled_data
    
    def my_splitter(self, x, y, test_size=None, random_state=None):
        X_train, X_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.3, random_state=1)
        
        return  X_train, X_test, y_train, y_test
    
    def my_fillna(self, df):
        df = df.apply(lambda x: x.fillna(x.mean()),axis=1)
        
        return df 
    
    def get_target(self, df):
        y = df[self.target_name]
        
        return y 
 
#  
