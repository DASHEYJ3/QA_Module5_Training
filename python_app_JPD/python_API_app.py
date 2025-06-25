# import the required libraries
import requests

# the base URL to query the books API
API_URL = 'https://dogapi.dog/api/v2/breeds'

headers = {'Accept': 'application/json'} #2
    # set all parameters needed to make the request
params = {'id':'036feed0-da8a-42c9-ab9a-57449b530b13'}
 
response = requests.get(API_URL, headers=headers)   #params=params
    
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("API Response:", data)
else:
    print(f"Error: {response.status_code}, {response.text}") 

#print(data['type'])


#import requests #1

#headers = {'Accept': 'application/json'} #2 
#response = requests.get('https://icanhazdadjoke.com/', headers=headers) #3

#print(response) #4
# <Response [200]>

#data = response.json() #5

#print(data) #6
# {"id": "FdNZTnWvHBd", "joke": "I’ve just been reading a book about anti-gravity, it’s impossible to put down!", "status": 200}

#print(data['joke']) #7
# I’ve just been reading a book about anti-gravity, it’s impossible to put down!