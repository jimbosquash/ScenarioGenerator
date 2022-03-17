import sys
from math import cos, radians, sin
import Core
import Solver
import module_DB
import requests

print ("Author : James Hayward \n Assembly Scenario Automation program launching \n")

if __name__ == "__main__":
# set to a func that can be called from command line
    # below is for importing demo data

    #download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
    #target_csv_path = "nba_all_elo.csv"

    #response = requests.get(download_url)
    #response.raise_for_status()    # Check that the request was successful
    #with open(target_csv_path, "wb") as f:
     #   f.write(response.content)
    # above is for importing demo data
    print("Download ready.")
    dB_Test = module_DB.module_DB_Test()
    dB_Test.launchTestSolver(dB_Test)


    

