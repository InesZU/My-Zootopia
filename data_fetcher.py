import requests

API_KEY = 'eoieZ402XIK9RnHYmLLt5Q==cQL10xx0ToRBYBRy'

def fetch_data(animal_name):
  """Fetches the animals data for the animal 'animal_name' from an API.

  Args:
      animal_name (str): The name of the animal to search for.

  Returns:
      list: A list of animal dictionaries containing information (may be empty if not found).
  """

  api_url = "https://api.api-ninjas.com/v1/animals"
  headers = {'X-Api-Key': API_KEY}
  params = {'name': animal_name}

  response = requests.get(api_url, headers=headers, params=params)

  if response.status_code == requests.codes.ok:
    # Parse the JSON response
    data = response.json()
    return data
  else:
    print(f"API request failed with status code: {response.status_code}")
    return []  # Return an empty list on error
