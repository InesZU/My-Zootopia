import requests

def generate_animal_website(animal_name):
  """Fetches animal information from an API and generates an HTML website.

  Args:
      animal_name (str): The name of the animal to search for.
  """

  api_url = "https://api.api-ninjas.com/v1/animals"
  headers = {'X-Api-Key': 'eoieZ402XIK9RnHYmLLt5Q==cQL10xx0ToRBYBRy'}

  params = {'name': animal_name}
  response = requests.get(api_url, headers=headers, params=params)

  if response.status_code == requests.codes.ok:
    # Parse the JSON response
    data = response.json()

    # Check if there are any results
    if not data:
      # Generate HTML content for animal not found
      html_content = f"""
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Animal Not Found</title>
      </head>
      <body>
          <h1>Oops! We couldn't find information about "{animal_name}"</h1>
          <p>Please try searching for another animal.</p>
      </body>
      </html>
      """
    else:
      # Generate HTML content for animal found
      html_content = f"""
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>{animal_name} Information</title>
      </head>
      <body>
          <h1>{animal_name}</h1>
          <ul>
      """
      for animal in data:
        html_content += f"\t<li>Name: {animal['name']}</li>\n"
        html_content += f"\t<li>Taxonomy: {animal['taxonomy']}</li>\n"
      html_content += """
          </ul>
      </body>
      </html>
      """

    # Write the HTML content to a file
    with open("animals.html", "w") as file:
      file.write(html_content)

    print("Website successfully generated to the file animals.html.")
  else:
    print(f"API request failed with status code: {response.status_code}")

if __name__ == "__main__":
  animal_name = input("Enter a name of an animal: ")
  generate_animal_website(animal_name)
