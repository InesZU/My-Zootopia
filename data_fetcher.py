import requests
import os
from dotenv import load_dotenv

def fetch_data(animal_name):
    """Fetches the animal's data for the animal 'animal_name' from an API.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        list: A list of animal dictionaries containing information (may be empty if not found).
    """
    load_dotenv()

    API_KEY = os.getenv('API_KEY')

    api_url = "https://api.api-ninjas.com/v1/animals"
    headers = {'X-Api-Key': API_KEY}
    params = {'name': animal_name}

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == requests.codes.ok:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        return []  # Return an empty list on error