import sys 
sys.path.append('app/rob/models')
from robot import HealthRobot
  
def record():
    rob = HealthRobot()
    rob.updata_dataframe_and_sql()
    rob.save_plots()
    
    
