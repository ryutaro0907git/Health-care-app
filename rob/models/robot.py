"""Defined a robot model """
import pandas as pd
import numpy as np
from datetime import datetime
import glob
import os 
import sys 
import cv2
from PIL import Image

from model import MyModel
from db import to_sql

DEFAULT_ROBOT_NAME = 'Roboko'
USER_NAME = 'Ryu'

class Robot(object):
    """Base model for Robot."""
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=USER_NAME,
                 speak_color='green'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color

class HealthRobot(Robot):
    """Handle user data."""
    
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_data_list=None):
        super().__init__(name=name)
        # self.ranking_model = ranking.RankingModel()
        if user_data_list is None:
            self.user_data_list = list()
        else:
            print('data is already given.')
            
        self.df = pd.read_csv('app/rob/data/mydata.csv')
        self.col_names = self.df.columns.tolist()
        self.now = str(datetime.now())
        
        self.project_dir = 'app/rob'
        self.data_dir = os.path.join(self.project_dir, 'data')
    
    def save_plots(self):
        model = MyModel()
        model.run_xgboost()
    
    def show_plots(self):
        result_dir = os.path.join(self.data_dir, 'result')
        results = glob.glob(os.path.join(result_dir, '*.jpg'))
        print(results)
        for path in results:
            img = Image.open(path)
            img.show()
        
    def updata_dataframe_and_sql(self):
        new_data = self.__get_a_dataframe()
        new_df = self.df.append(new_data)
        new_df.to_csv('app/rob/data/mydata.csv')
        
        to_sql(new_df)
        
        
    def __get_a_dataframe(self):
        user_datas = self.__collect_user_data()
        if len(user_datas) == len(self.col_names):
            d = {}
            for k, v in zip(self.col_names, user_datas):
                d[k] = v
                
            df = pd.DataFrame(d,index=[len(self.df)+1])
            
            return df 
        else:
            print('there are missing data')
    
    def __collect_user_data(self):
        while True:
            now = datetime.now()
            self.user_data_list.append(now)
            sleep_hours = float(input('How long did you sleep last night(h):?'))
            if 1 <= sleep_hours <= 20:
                self.user_data_list.append(sleep_hours)
            else:
                self.user_data_list.append(None)
            freshness = int(input('How fresh are you? (from 1 to 5): '))
            if 1 <= freshness <= 5:
                self.user_data_list.append(freshness)
            else:
                self.user_data_list.append(None)

            melatonin = str(input('Did you take melatonin last night? (yes or no):')).lower()
            if melatonin == 'yes' or melatonin=='no': 
                self.user_data_list.append(melatonin)
            else:
                self.user_data_list.append(None)
            motivation = int(input('How motibated are you (from 1 to 5):'))
            if 1 <= motivation <= 5:
                self.user_data_list.append(motivation)
            else:
                self.user_data_list.append(None)
            nap = float(input('How long did you take nap today? (min):'))
            if 1<= nap <= 500:
                self.user_data_list.append(nap)
            else:
                self.user_data_list.append(None)
                
            sunlight = float(input('Were you exposed to sunlight(h):?'))
            if 0.1 <= sunlight <= 24:
                self.user_data_list.append(sunlight)
            else:
                self.user_data_list.append(None)  
                
            bluelight = str(input('Were you exposed to blunelight before bed? (yes or no):'))
            if bluelight == 'yes' or  bluelight == 'no':
               self.user_data_list.append(bluelight)
            else:
                self.user_data_list.append(None)
                
            night_snak = str(input('Did you eat before going to bed? (yes or no):'))
            if night_snak == 'yes' or night_snak == 'no':
                self.user_data_list.append(night_snak)
            else:
                self.user_data_list.append(None)
                
            night_drink = str(input('Did you drink an alchol before going to bed? (yes or no);'))
            if night_drink == 'yes' or night_drink == 'no':
                self.user_data_list.append(night_drink)
            else:
                self.user_data_list.append(None)
                
            late_workout = str(input('Did you do late excersise? (yes or no):'))
            if late_workout == 'yes' or late_workout == 'no':
                self.user_data_list.append(late_workout)
            else:
                self.user_data_list.append(None)
                
            stay_up = str(input('Did you stay up late? (yes or no):'))
            if stay_up == 'yes' or stay_up == 'no':
                self.user_data_list.append(stay_up)
            else:
                self.user_data_list.append(None)
                
            breakfast = float(input('Carories(break fast):'))   
            if 1 <= breakfast <= 5000:
                self.user_data_list.append(breakfast)
            else:
                self.user_data_list.append(None)
                
            lunch = float(input('Carories(lunch):'))
            if 1 <= lunch <= 5000:
                self.user_data_list.append(lunch)
            else:
                self.user_data_list.append(None)
            dinner = float(input('Carories(dinner):'))
            if 1 <= dinner <= 5000:
                self.user_data_list.append(dinner)
            else:
                self.user_data_list.append(None)
                
            snack = float(input('Carories(snack):'))
            if 1 <= snack <= 5000:
                self.user_data_list.append(snack)
            else:
                self.user_data_list.append(None)  
                  
            morning_excersies = str(input('Did you do excersise this morning?(yes or no):'))
            if morning_excersies == 'yes' or morning_excersies == 'no':
                self.user_data_list.append(morning_excersies)
            else:
                self.user_data_list.append(None)
                
            microburst = int(input('How many microburst did you do today? (num):'))
            if 0 <= microburst <= 100:
                self.user_data_list.append(microburst)
            else:
                self.user_data_list.append(None)
                
            steps = float(input('How steps did you have today? (num):'))
            if 0 <= steps:
                self.user_data_list.append(steps)
            else:
               self.user_data_list.append(None)
            sport = float(input('How many hours did you play sport today?'))
            if 0 <= sport <= 24:
                self.user_data_list.append(sport)
            else:
                self.user_data_list.append(None)
            meditation = float(input('How long did you meditate today?'))
            if 0 <= meditation <=1000:
                self.user_data_list.append(meditation)
            else:
                self.user_data_list.append(None)
            
            protein = float(input('How much protein did you take today?'))
            if 0 <= protein <=300:
                self.user_data_list.append(protein)
            else:
                self.user_data_list.append(None)
                
            cho = float(input('How many cho did you take today?'))
            if 0 <= cho <=1000:
                self.user_data_list.append(cho)
            else:
                self.user_data_list.append(None)
            
            fat = float(input('How many fat did you take today?'))
            if 0 <= fat <= 100:
                self.user_data_list.append(fat)
            else:
                self.user_data_list.append(None)
                
            saturated_fat = float(input('How many saturated_fat did you take today?'))
            if 0 <= saturated_fat <= 1000:
                self.user_data_list.append(saturated_fat)
            else:
                self.user_data_list.append(None)
                
            coffee = int(input('How many coffee did you have today?'))
            if 0 <= coffee <=20:
                self.user_data_list.append(coffee)
            else:
                self.user_data_list.append(None)
            fiber = float(input('How much fiber did you take today?'))
            if 0 <= fiber <= 200:
                self.user_data_list.append(fiber)
            else:
                self.user_data_list.append(None)
            sugar = float(input('How much sugar did you take today?'))
            if 0 <= sugar <= 1000:
                self.user_data_list.append(sugar)
            else:
                self.user_data_list.append(None)
            study_hours = float(input('How many hours did you study today?'))
            if 0 <= study_hours <= 24:
                self.user_data_list.append(study_hours)
            else:
                self.user_data_list.append(None)
            reading_hours = float(input('How many hours did you read?'))
            if 0 <= reading_hours <= 24:
                self.user_data_list.append(reading_hours)
            else:
                self.user_data_list.append(None)
            work_hours = float(input('How many hours did you work today?'))
            if 0 <= work_hours <= 24:
                self.user_data_list.append(work_hours)
            else:
                self.user_data_list.append(None)
            talk_to_friend = str(input('Did you talk to your frined today? (yes or no):'))
            if talk_to_friend == 'yes' or talk_to_friend == 'no':
                self.user_data_list.append(talk_to_friend)
            else:
                self.user_data_list.append(None)
            hungout = str(input('Did you hung out today?(yes or no):'))
            if hungout == 'yes' or hungout == 'no':
                self.user_data_list.append(hungout)
            else:
                self.user_data_list.append(None)
            Did_something_new = str(input('Did you do something new today? (yes or no):'))
            if Did_something_new == 'yes' or Did_something_new == 'no':
                self.user_data_list.append(Did_something_new)
            else:
                self.user_data_list.append(None)
            achived_something = str(input('Did you achive something today? (yes or no)'))
            if achived_something == 'yes' or achived_something == 'no':
                self.user_data_list.append(achived_something)
            else:
                self.user_data_list.append(None)
                
            stressful_event = str(input('Any stressful event? (yes or no):'))
            if stressful_event == 'yes' or stressful_event == 'no':
                self.user_data_list.append(stressful_event)
                
            else:
                self.user_data_list.append(None)
            
            weather = str(input('wether? (sunny, cloudy, rainy, snowy)'))
            if weather in ("sunny", "cloudy", "rainy", "snowy"):                         
               self.user_data_list.append(weather)
            else:
                self.user_data_list.append(None)
            temparature = float(input('Temparature?'))
            if -50 <= temparature <= 50:
                self.user_data_list.append(temparature)
            else:
                self.user_data_list.append(None)
                
            help_others = str(input('Did you help_others today?(yes or no):'))
            if help_others == 'yes' or help_others == 'no':
                self.user_data_list.append(help_others)
            else:
                self.user_data_list.append(None)
            happiness = int(input('How happy are you today? (1 to 5):'))
            if 1 <= happiness <= 5:
                self.user_data_list.append(happiness)
            else:
                self.user_data_list.append(None)
            
            tiredness = int(input('How tired are you now? (1 to 5):'))
            if 1 <= tiredness <= 5:
                self.user_data_list.append(tiredness)
            else:
                self.user_data_list.append(None)
                
            print('Alright we got your data!')
            print(self.user_data_list)
            
            return self.user_data_list 


    def recommend_actino(self):
        """Recommend action to increase the target feature"""
        pass
