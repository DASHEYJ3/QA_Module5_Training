import pandas as pd

# DataFrame - read the file 
df = pd.read_csv(r"C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\Library SystemCustomers.csv",quotechar='"')
  
print(df.to_string())

#print (df['Book checkout'].str.len() > 12)

print(df.dtypes)
print(df.duplicated())


# drops empty cells
new_df = df.dropna()
#new_df.drop_duplicates(inplace = True)
#new_df['Book checkout'] = pd.to_datetime(new_df['Book checkout'].str.replace('"', ''), errors='coerce')

print(new_df.to_string())


# Export to CSV
#new_df.to_csv(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\cleaned_customers.csv', index=False)  # Set index=False to exclude the index column

#errors_df = new_df[new_df['Book checkout'].isna()]
#errors_df.to_csv(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\invalid_customers.csv', index=False)  # Set index=False to exclude the index column


# DataFrame - read the file 
#df = pd.read_csv(r"C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\Library SystemCustomers.csv")