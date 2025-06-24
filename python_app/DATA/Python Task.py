import pandas as pd

# Data engineering metrics (instantiation)
dropCount= 0

# DataFrame - read the Book file
book_df = pd.read_csv(r"C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\Library Systembook.csv",quotechar='"')

# DataFrame - read the Customers file
customerid_df = pd.read_csv(r"C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\Library SystemCustomers.csv")

customer_df = customerid_df[['Customer ID', 'Customer Name']]
  
#print(book_df.to_string())
#print(customer_df.to_string())
##print (book_df['Book checkout'].str.len() > 12)
#print(book_df.dtypes)
#print(book_df.duplicated())

#convert book checkout 
#book_df['Book checkout'] = pd.to_datetime(book_df['Book checkout'].str.replace('"', '', regex=False))
#book_df['Book checkout'] = pd.to_datetime(book_df['Book checkout'].str.replace('"', '', ))
#book_df['Book checkout'] = pd.to_datetime(book_df['Book checkout'].str.replace('"', ''), format='mixed')
#book_df['Book checkout'] = pd.to_datetime(book_df['Book checkout'].str.replace('"', ''), errors='coerce')
#print(book_df[book_df['Book checkout'].isna()])

# drops empty cells
#new_df = book_df.dropna()
#new_df.drop_duplicates(inplace = True)
book_df['Book checkout'] = pd.to_datetime(book_df['Book checkout'].str.replace('"', ''), dayfirst=True, errors='coerce')
book_df['Book Returned'] = pd.to_datetime(book_df['Book Returned'].str.replace('"', ''), dayfirst=True, errors='coerce')
# drops empty cells
new_book_df = book_df.dropna()
#new_df = new_df.dropna(inplace = True)
print(new_book_df.to_string())

# Perform the merge to add the Science column to the student_records
missing_df = new_book_df.merge(
  customer_df,
  left_on=['Customer ID'],
  right_on=['Customer ID'], how = 'left'
)

missing_customer = missing_df[missing_df['Customer Name'].isna()]
#print(missing_customer.to_string())
errors_customer = missing_customer[['Books', 'Book checkout', 'Book Returned', 'Days allowed to borrow', 'Customer ID']]
print(errors_customer.to_string())
#Books	Book checkout	Book Returned	Days allowed to borrow	Customer ID

def enrich_LoanDurationDays():
    new_book_df['LoanDurationDays'] = (new_book_df['Book Returned']-new_book_df['Book checkout']).dt.days
    return new_book_df
  
new_book_df = enrich_LoanDurationDays()

# Export to CSV
new_book_df.to_csv(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\cleaned_books.csv', index=False)  # Set index=False to exclude the index column

# Export errors to CSV
#errors_df = book_df[book_df['Book checkout'].isna()]
#errors_df.to_csv(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\invalid_books.csv', index=False)  # Set index=False to exclude the index column

errors_df = book_df[book_df['Book checkout'].isna()]
errors_df.to_csv(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\invalid_books.csv', index=False)  # Set index=False to exclude the index column

with open(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\invalid_books.csv', 'a', newline='', encoding='utf-8') as f:
    errors_customer.to_csv(f, header=f.tell()==0)

#errors_customer.to_csv(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\invalid_books.csv', 'a', index=False) #, encoding='utf-8'

# drops empty cells
new_customer_df = customerid_df.dropna()
#print(new_customer_df.to_string())

new_customer_df.to_csv(r'C:\Users\Admin\Desktop\QA_Module5_Training\python_app\DATA\cleaned_customers.csv', index=False)  # Set index=False to exclude the index column
