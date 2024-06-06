import requests

url = 'https://4rooms.app/master_apis/api/get-country-currency-list.php'  # 
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Authorization': 'Bearer your_api_token'
}
form_data = {
    'api_key': '28d50cd6-befb-4b02-b024-dbf5b43b2912',
    'translation_language_id':'1'
}

try:
    response = requests.post(url, data=form_data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    print('Success:', response.json())  # Process the JSON response
    currencyList = response.json().data
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Specific HTTP error
except Exception as err:
    print(f'Other error occurred: {err}')  # Any other error