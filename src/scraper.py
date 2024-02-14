
import requests  # Importing the requests library

root_url = "https://country-leaders.onrender.com"  # Assigning the root URL without /status to the root_url variable
status_url = root_url + "/status"  # Assigning the /status endpoint to the status_url variable
req = requests.get(status_url)  # Querying the /status endpoint using the get() method and storing it in the req variable

# Checking the status_code using a condition and printing appropriate messages
if req.status_code == 200:
    print("Connection to the status endpoint successful!")
else:
    print(f"Error: Failed to connect to the status endpoint. Status code: {req.status_code}")

cookie_url = root_url + "/cookie"  # Set the cookie_url variable
cookies = requests.get(cookie_url).cookies  # query /cookie endpoint and setting the cookies variable

countries_url = root_url + "/countries"  # Set the countries_url variable
req = requests.get(countries_url, cookies=cookies) # query the /countries endpoint using the get() method and store it in the req variable 
countries = req.json() # Get the JSON content and store it in the countries variable 
print(countries) # Display the countries variable

leaders_per_country = {} # Initialize an empty dictionary to store leaders for each country

# Loop through each country code and query the /leaders endpoint
for country_code in countries: 
    leaders_endpoint_url = f"{root_url}/leaders?country={country_code}" # Construct the URL for the /leaders endpoint with the country code as a parameter
    leaders_response = requests.get(leaders_endpoint_url, cookies=cookies) # Query the /leaders endpoint for the current country code
    leaders_per_country[country_code] = leaders_response.json() # Store the JSON result in the leaders_per_country dictionary

print(leaders_per_country) # Print the dictionary containing leaders for each country

