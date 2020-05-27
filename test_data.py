import unittest

from early_scripts import csv_script



class TestCSVScript(unittest.TestCase):

	def test_create_df_of_specific_size(self):
		"""
		Test that the function returns a df of size (6806, 1982)
		"""
		df = csv_script.create_df('TESTMERGED2018_19_PP.csv')
		self.assertEqual(df.shape, (6806, 1982))
		
	def test_trimmed_df_to_len_of_clmn_ls(self):
		"""
		Tests that the function creates a new dataframe from the list
		argument and it is the correct column size as the list
		"""
		df = csv_script.create_df('TESTMERGED2018_19_PP.csv')
		test_clmns = ['INSTNM', 'CITY', 'STABBR']
		df = csv_script.trim_df(df, test_clmns)
		self.assertEqual(df.shape[1], len(test_clmns))
	
	def test_renamed_column_exists(self):
		"""
		Test that the newly renamed column now exists
		"""
		df = csv_script.create_df('TESTMERGED2018_19_PP.csv')
		df = csv_script.rename_columns(df, rename_dict={'INSTNM': 'NAME'})
		self.assertFalse(df['NAME'].empty)
	
	def test_checks_head_if_is_correct_state(self):
		"""
		Test checks if the head of the dataframe contains only
		the specified state
		"""
		df = csv_script.create_df('TESTMERGED2018_19_PP.csv')
		df = csv_script.rename_columns(df, rename_dict={'STABBR': 'STATE'})
		df = csv_script.retrieve_by_state(df, 'CA')
		self.assertEqual(df['STATE'].iloc[0], 'CA')
	
	def test_df_has_reset_index_from_zero(self):
		"""
		Test checks whether the index has been reset to start from
		zero and whether a new column has been mirroring the index
		"""
		df = csv_script.create_df('TESTMERGED2018_19_PP.csv')
		df = csv_script.rename_columns(df, rename_dict={'STABBR': 'STATE'})
		df = csv_script.retrieve_by_state(df, 'CA')
		df = csv_script.reformat_index(df)
		self.assertEqual(df['index'].iloc[0], 0)
		
	
	def test_checks_tuple_list_equals_df(self):
		"""
		Test checks if the list of tuples created is the same length
		as the number of rows from the dataframe
		"""
		df = csv_script.create_df('TESTMERGED2018_19_PP.csv')
		df = csv_script.rename_columns(df, rename_dict={'STABBR': 'STATE'})
		df = csv_script.retrieve_by_state(df, 'CA')
		ls = csv_script.create_ls_of_tuples(df)
		self.assertEqual(df.shape[0], len(ls))
	
if __name__ == '__main__':

	unittest.main()
		




