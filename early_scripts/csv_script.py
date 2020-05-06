import pandas as pd


temp_path = '..\CollegeScorecard_Raw_Data\CollegeScorecard_Raw_Data\MERGED2018_19_PP.csv'


def create_df(csv_path):
	
	df = pd.read_csv(csv_path)
	
	return df


