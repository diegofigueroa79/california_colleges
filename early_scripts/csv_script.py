import pandas as pd


college_data_path = '..\CollegeScorecard_Raw_Data\CollegeScorecard_Raw_Data\MERGED2018_19_PP.csv'


ls_of_relevant_clmns = ['INSTNM', 'CITY', 'STABBR', 'ZIP', 'INSTURL',
						'ADM_RATE', 'SATVR25', 'SATVR75', 'SATMT25',
						'SATMT75', 'SATWR25', 'SATWR75',
						'SATVRMID', 'SATMTMID', 'ACTCM25', 'ACTCM75',
						'ACTEN25', 'ACTEN75', 'ACTMT25', 'ACTMT75',
						'ACTWR25', 'ACTWR75', 'ACTCMMID', 'ACTENMID',
						'ACTMTMID', 'ACTWRMID', 'SAT_AVG',
						'TUITIONFEE_IN', 'TUITIONFEE_OUT',]
						
rename_dict = {
	'INSTNM': 'NAME', 'STABBR': 'STATE', 'INSTURL': 'URL',
}


def create_df(csv_path):
	
	df = pd.read_csv(csv_path)
	
	return df

def trim_df(df, columns):
	
	new_df = df[columns]
	
	return new_df
	
def rename_columns(df, rename_dict):
	
	df.rename(columns=rename_dict, inplace=True)
	
	return df

def retrieve_by_state(df, state):
	
	is_state = df['STATE'] == state
	new_df = df[is_state]
	
	return new_df

def reformat_index(df):
	
	df.reset_index(drop=True, inplace=True)
	df.reset_index(inplace=True)
	
	return df

def create_ls_of_tuples(df):
	
	ls = list(df.itertuples(index=False, name=None))
	
	return ls


