import numpy as np 
import pandas as pd
from scipy import spatial
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import PolynomialFeatures
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn import metrics

class Models(object):
    def __init__(self, X_train, X_test, y_train, y_test): 
        self.x_train = X_train
        self.x_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        
    def model_estimator(self, y_test, pred):
      print(metrics.confusion_matrix(y_test, pred))
      print(metrics.classification_report(y_test, pred, digits=3))
      
class MyRegression(Models):        
    def __init__(self, X_train, X_test, y_train, y_test):
        super().__init__(X_train, X_test, y_train, y_test)
        
    def multiple_regressioness(self):
        est = sm.OLS(self.y_train, self.x_train).fit()
        return est.summary()
    
    def polynominal_regression(self):
        X_train = PolynomialFeatures(interaction_only=True).fit_transform(self.x_train).astype(int)
        clf = Perceptron(fit_intercept=False, max_iter=10, tol=None,
                shuffle=False).fit(X_train, self.y_train)
        X_test = PolynomialFeatures(interaction_only=True).fit_transform(self.x_test).astype(int)
        # pred = clf.predict(X)
        score = clf.score(X_test, self.y_test)
        
        return score 
    
class MyClassifier(Models):
    def __init__(self, X_train, X_test, y_train, y_test):
        super().__init__(X_train, X_test, y_train, y_test)
        
    # def my_svm(self, X, y):
        
    
class MyTrees(Models):
    def __init__(self, X_train, X_test, y_train, y_test):
        super().__init__(X_train, X_test, y_train, y_test)
        
    def my_xgboost(self, param=None, epochs=10):
        train = xgb.DMatrix(self.x_train, label=self.y_train)
        test = xgb.DMatrix(self.x_test, label=self.y_test)
        
        if param is None:
            param = {
            'max_depth': 4,
            'eta': 0.3,
            'objective': 'multi:softmax',
            'num_class':5}
            
        model = xgb.train(param, train, epochs)
        # predictions = model.predict(test)
        # score = accuracy_score(self.y_test, predictions) 
        
        return model
    
class MyClustering(Models):
    def __init__(self, X_train, X_test, y_train, y_test):
        super().__init__(X_train, X_test, y_train, y_test)
    
        # def kmeans_clustering(self, centroids)
    
    def ComputeDistance(self,a, b):
        genresA = a[1]
        genresB = b[1]
        genreDistance = spatial.distance.cosine(genresA, genresB)
        popularityA = a[2]
        popularityB = b[2]
        popularityDistance = abs(popularityA - popularityB)
        return genreDistance + popularityDistance
    
    
