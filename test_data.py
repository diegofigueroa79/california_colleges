import unittest

from early_scripts import csv_script



class TestCSVScript(unittest.TestCase):

	def test_create_df_of_specific_size(self):
		"""
		Test that the function returns a df of size (6806, 1982)
		"""
		
		data_path = 'TESTMERGED2018_19_PP.csv'
		
		df = csv_script.create_df(data_path)
		self.assertEqual(df.shape, (6806, 1982))
	
if __name__ == '__main__':

	unittest.main()
		




