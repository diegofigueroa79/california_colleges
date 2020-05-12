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
	
if __name__ == '__main__':

	unittest.main()
		




