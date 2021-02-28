import os 
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from xgboost import XGBClassifier

class Plot(object):
    def __init___(self, data_dir=None):
        if data_dir is None:
            self.data_dir = 'app/rob/data'
    
    def __save_result_plot(self, filename=''):
        save_dir = os.path.join(self.data_dir, 'result')
        if os.path.exists(save_dir) is False:
           os.mkdir(save_dir)
        plt.savefig(os.path.join(save_dir, filename))
        
    def save_heatmap(self, df):
        _ , ax = plt.subplots(figsize =(30, 30))
        colormap = sns.diverging_palette(220, 10, as_cmap = True)
    
        _ = sns.heatmap(
                df.corr(), 
                cmap = colormap,
                square=True, 
                cbar_kws={'shrink':.9}, 
                ax=ax,
                annot=True, 
                # linewidths=0.1, vmin=-0.8,vmax=0.8, linecolor='white',
                linewidths=0.1, vmin=-0.8,vmax=0.8, linecolor='white',
                annot_kws={'fontsize':12 }
   
                    )
    
        plt.title('Scores and correlation features', y=1, size=15)
        self.__save_result_plot('heatmap.jpg')

class MyXGboostResult(Plot):
    def __init__(self, model ,data_dir=None):
        if data_dir is None:
            self.data_dir ='app/rob/data' 
            
        self.model = model        
        
    def save_feature_importances(self):
        fig = plt.figure(figsize = (16, 12))
        title = fig.suptitle("Default Feature Importances from XGBoost", fontsize=14)

        ax1 = fig.add_subplot(2,2, 1)
        xgb.plot_importance(self.model, importance_type='weight', ax=ax1)
        t=ax1.set_title("Feature Importance - Feature Weight")

        ax2 = fig.add_subplot(2,2, 2)
        xgb.plot_importance(self.model, importance_type='gain', ax=ax2)
        t=ax2.set_title("Feature Importance - Split Mean Gain")

        ax3 = fig.add_subplot(2,2, 3)
        xgb.plot_importance(self.model, importance_type='cover', ax=ax3)
        t=ax3.set_title("Feature Importance - Sample Coverage")
        
        self.__save_result_plot('FeatureImportance.jpg')
        
