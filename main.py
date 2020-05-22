from early_scripts import csv_script, pg




if __name__ == '__main__':
	
	df = csv_script.create_df("TESTMERGED2018_19_PP.csv")
	
	df = csv_script.trim_df(df, csv_script.ls_of_relevant_clmns)
	
	df = csv_script.rename_columns(df, csv_script.rename_dict)
	
	df = csv_script.retrieve_by_state(df, 'CA')
	
	ls = csv_script.create_ls_of_tuples(df)
	
	print("List of tuples ready.")