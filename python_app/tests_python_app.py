import pandas as pd
import unittest
from python_app import enrich_dateDuration

""" # Define column names
columns = ['Book checkout', 'Book Returned', 'ExpectedValue']

# Define data with dates
data = [
    ['2025-04-01', '2025-04-30', '29'],
]

# Create the DataFrame
df = pd.DataFrame(data, columns=columns)

# Convert 'Date' column to datetime format (optional)
df['Book checkout'] = pd.to_datetime(df['Book checkout'])
df['Book Returned'] = pd.to_datetime(df['Book Returned'])
df['ExpectedValue'] = int(df['ExpectedValue'])

expectedvalue = df['ExpectedValue']

function_value = enrich_dateDuration(colA='Book Returned', colB='Book checkout',df=df)
date_delta = function_value['date_delta']

# Display the DataFrame
print(df)
print(expectedvalue)
print(date_delta) """





#data = enrich_dateDuration(df=data, colA='Book Returned', colB='Book checkout')

class TestEnrichment(unittest.TestCase):
    
        def setUp(self):
 
        # Creating a test dataframe
            self.test_df = pd.DataFrame({
                'Book checkout': ['1/01/2025', '2/01/2025', '3/01/2025'],
                'Book returned': ['1/02/2025', '2/02/2025', '3/02/2025']
            #    'ExpectedValue': [31,31,31]
            })

            # Convert the columns to datetime 
            self.test_df['Book checkout'] = pd.to_datetime(self.test_df['Book checkout'], format = '%d/%m/%Y')
            self.test_df['Book returned'] = pd.to_datetime(self.test_df['Book returned'], format = '%d/%m/%Y')
            #self.test_df['ExpectedValue'] = int(self.test_df['ExpectedValue'])
            
        # Apply the enrichment function
            self.enriched_df = enrich_dateDuration(df=self.test_df, colA='Book returned', colB='Book checkout') 
            #self.expectedvalue_df = self.test_df['ExpectedValue']
         
        def test_duration(self):
            self.assertEqual((self.enriched_df['date_delta']).all(),31, "The Calculation is wrong")
            
        def test_duration_as_int(self):
            self.assertTrue(pd.api.types.is_integer_dtype(self.enriched_df['date_delta']), "The delta col is not an integer")

        def test_duration_above_zero(self):
            self.assertTrue((self.enriched_df['date_delta']>0).all(), "Some durations are less than 0")  
 
if __name__ == '__main__':
    unittest.main()     