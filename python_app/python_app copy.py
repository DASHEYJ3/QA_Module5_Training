import pandas as pd
from sqlalchemy import create_engine
import pyodbc
#import argparse
#import sqlite3

# Function to output dataframe that can be manipulated via a filepath
def fileLoader(filepath):
    data = pd.read_csv(filepath)
    return data 

# Duplicate Dropping Function
def duplicateCleaner(df):
    return df.drop_duplicates().reset_index(drop=True)

# NA handler - future scope can handle errors more elegantly. 
def naCleaner(df):
    return df.dropna().reset_index(drop=True)

# Turning date columns into datetime
def dateCleaner(col, df):
    date_errors = pd.DataFrame(columns=df.columns)  # Store rows with date errors

    # Strip any quotes from dates
    df[col] = df[col].str.replace('"', "", regex=True)

    try:
        df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')

    except Exception as e:
        print(f"Error while converting column {col} to datetime: {e}")

    # Identify rows with invalid dates
    error_flag = pd.to_datetime(df[col], dayfirst=True, errors='coerce').isna()
        
    # Move invalid rows to date_errors - Future feature
    date_errors = df[error_flag]
        
    # Keep only valid rows in df
    df = df[~error_flag].copy()

    # Reset index for the cleaned DataFrame
    df.reset_index(drop=True, inplace=True)

    return df

def enrich_dateDuration(colA, colB, df):
    """
    Takes the two datetime input column names and the dataframe to create a new column date_delta which is the difference, in days, between colA and colB.
    
    Note:
    colB>colA
    """
    df['date_delta'] = (df[colA]-df[colB]).dt.days

    #Conditional Filtering to be able to gauge eroneous loans.
    df.loc[df['date_delta'] < 0, 'valid_loan_flag'] = False
    df.loc[df['date_delta'] >= 0, 'valid_loan_flag'] = True

    return df

def writeToSQL(df, table_name, server, database):

    # Create the connection string with Windows Authentication
    connection_string = f'mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'

    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)

    try:
        # Write the DataFrame to SQL Server
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)

        print(f"Table{table_name} written to SQL")
    except Exception as e:
        print(f"Error writing to the SQL Server: {e}")

if __name__ == '__main__':
    print('**************** Starting Clean ****************')

    # Instantiation
    dropCount= 0
    customer_drop_count = 0
    filepath_input = './data/03_Library Systembook.csv'
    date_columns = ['Book checkout', 'Book Returned']
    date_errors = None
    today_date_time = pd.to_datetime('today')
    today_date = today_date_time.date()

    print(today_date)

    data = fileLoader(filepath=filepath_input)
    count_row = data.shape[0]     

    
    # Drop duplicates & NAs
    data = duplicateCleaner(data)
    data = naCleaner(data)

    # Converting date columns into datetime
    for col in date_columns:
        data = dateCleaner(col, data)
    
    # Enriching the dataset
    data = enrich_dateDuration(df=data, colA='Book Returned', colB='Book checkout')

    data.to_csv('./data/cleaned_books.csv')
    print(data)
    count_row2 = data.shape[0]     
    
    ProcessLog = {
        'DateTimeProcessed': today_date_time,
        'DateProcessed': today_date,
        'SourceCSV': filepath_input, 
        'SourceRecordCount': count_row,
        'LoadedRecordCount': count_row2        
        }
    print(ProcessLog)  
   
    #Cleaning the customer file
    filepath_input_2 = './data/03_Library SystemCustomers.csv'

    data2 = fileLoader(filepath=filepath_input_2)
 
    count_row = data2.shape[0]     
 
    # Drop duplicates & NAs
    data2 = duplicateCleaner(data2)
    data2 = naCleaner(data2)
    
    data2.to_csv('./data/cleaned_customers.csv')
    print(data2)
    count_row2 = data2.shape[0]     
    
    ProcessLog2 = {
        'DateTimeProcessed': today_date_time,
        'DateProcessed': today_date,
        'SourceCSV': filepath_input_2, 
        'SourceRecordCount': count_row,
        'LoadedRecordCount': count_row2        
        }
  
    pl1 = pd.DataFrame(ProcessLog, index=[0])
    pl2 = pd.DataFrame(ProcessLog2, index=[0])
    print(ProcessLog2)  
    
    result = pd.concat([pl1, pl2], axis=0)
    print(result)
    
    print('**************** DATA CLEANING FINISHED ****************')

    print('Writing to SQL Server ...')

    writeToSQL(
        data, 
        table_name='loans_bronze', 
        server = 'localhost', 
        database = 'DE5_Module5' 
    )

    writeToSQL(
        data2, 
        table_name='customer_bronze', 
        server = 'localhost', 
        database = 'DE5_Module5'
    )
   
    writeToSQL(
        result, 
        table_name='ProcessLog', 
        server = 'localhost', 
        database = 'DE5_Module5' 
    )
 
    print('**************** The End ****************')