import pandas as pd

# DataFrame - read the file 
df = pd.read_csv(r"C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\Library Systembook.csv",quotechar='"')
# DataFrame - read the file 
customerid_df = pd.read_csv(r"C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\Library SystemCustomers.csv")

customer_df = customerid_df[['Customer ID', 'Customer Name']]
  
#print(df.to_string())
#print(customer_df.to_string())
##print (df['Book checkout'].str.len() > 12)
#print(df.dtypes)
#print(df.duplicated())

#convert book checkout 
#df['Book checkout'] = pd.to_datetime(df['Book checkout'].str.replace('"', '', regex=False))
#df['Book checkout'] = pd.to_datetime(df['Book checkout'].str.replace('"', '', ))
#df['Book checkout'] = pd.to_datetime(df['Book checkout'].str.replace('"', ''), format='mixed')
#df['Book checkout'] = pd.to_datetime(df['Book checkout'].str.replace('"', ''), errors='coerce')

print(df[df['Book checkout'].isna()])

# drops empty cells
new_df = df.dropna()
#new_df.drop_duplicates(inplace = True)
new_df['Book checkout'] = pd.to_datetime(new_df['Book checkout'].str.replace('"', ''), errors='coerce')
new_df['Book Returned'] = pd.to_datetime(new_df['Book Returned'].str.replace('"', ''), errors='coerce')
#print(new_df.to_string())

# Perform the merge to add the Science column to the student_records
missing_df = new_df.merge(
  customer_df,
  left_on=['Customer ID'],
  right_on=['Customer ID'], how = 'left'
)

missing_customer = missing_df[missing_df['Customer Name'].isna()]
#print(missing_customer.to_string())
errors_customer = missing_customer[['Books', 'Book checkout', 'Book Returned', 'Days allowed to borrow', 'Customer ID']]
#print(errors_customer.to_string())


def enrich_dateDuration():
    new_df['LoadDurationDays'] = (new_df['Book Returned']-new_df['Book checkout']).dt.days
    return new_df
  
new_df = enrich_dateDuration()

# Export to CSV
new_df.to_csv(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\cleaned_books.csv', index=False)  # Set index=False to exclude the index column

# Export errors to CSV
errors_df = new_df[new_df['Book checkout'].isna()]
errors_df.to_csv(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\invalid_books.csv', index=False)  # Set index=False to exclude the index column

with open(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\invalid_books.csv', 'a') as f:
    errors_customer.to_csv(f, header=f.tell()==0)


# DataFrame - read the file 
#df2 = pd.read_csv(r"C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\Library SystemCustomers.csv",quotechar='"') 
#print(df2.to_string())
#print(df2.dtypes)
#print(df2.duplicated())

# drops empty cells
new_customer_df = customerid_df.dropna()
#print(new_customer_df.to_string())

new_customer_df.to_csv(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\cleaned_customers.csv', index=False)  # Set index=False to exclude the index column
