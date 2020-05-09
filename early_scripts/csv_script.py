import pandas as pd


college_data_path = '..\CollegeScorecard_Raw_Data\CollegeScorecard_Raw_Data'


ls_of_relevant_clmns = ['INSTNM', 'CITY', 'STABBR', 'ZIP', 'INSTURL',
						'ADM_RATE', 'ADM_RATE_ALL', 'SATVR25', 'SATVR75',
						'SATMT25', 'SATMT75', 'SATWR25', 'SATWR75',
						'SATVRMID', 'SATMTMID', 'ACTCM25', 'ACTCM75',
						'ACTEN25', 'ACTEN75', 'ACTMT25', 'ACTMT75',
						'ACTWR25', 'ACTWR75', 'ACTCMMID', 'ACTENMID',
						'ACTMTMID', 'ACTWRMID', 'SAT_AVG', 'SAT_AVG_ALL',
						'TUITIONFEE_IN', 'TUITIONFEE_OUT',]


def create_df(csv_path):
	
	df = pd.read_csv(csv_path)
	
	return df


