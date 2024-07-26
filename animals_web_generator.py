import data_fetcher 

def generate_animal_website(animal_name):
  """Fetches animal information from a data fetcher and generates an HTML website.

  Args:
      animal_name (str): The name of the animal to search for.
  """

  # Fetch data using the data fetcher
  data = data_fetcher.fetch_data(animal_name)

  # Check if any data was found
  if not data:
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Animal Not Found</title>
    </head>
    <body>
        <h1> We couldn't find information about "{animal_name}"</h1>
        <p>Please try searching for another animal.</p>
    </body>
    </html>
    """
  else:

    animal = data[0]  # Assuming the first element is the animal information
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{animal['name']} Information</title>
    </head>
    <body>
        <h1>{animal['name']}</h1>
        <ul>
            <li>Taxonomy: {animal['taxonomy']['kingdom']} - {animal['taxonomy']['phylum']}</li>
            <li>Locations: {', '.join(animal['locations'])}</li>
            <li>Characteristics: {animal['characteristics']['diet']} - {animal['characteristics']['average_lifespan']} lifespan</li>
        </ul>
    </body>
    </html>
    """

  # Write the HTML content to a file
  with open("animals.html", "w") as file:
    file.write(html_content)

  print("Website successfully generated to the file animals.html.")

if __name__ == "__main__":
  animal_name = input("Enter a name of an animal: ")
  generate_animal_website(animal_name)
