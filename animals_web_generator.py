import data_fetcher

def generate_animal_info(animals_data):
    """Generates HTML content for the animals."""
    animal_info_html = ""
    for animal in animals_data:
        lifespan = animal['characteristics'].get('average_lifespan', 'Unknown')
        diet = animal['characteristics'].get('diet', 'Unknown')

        phylum = animal['taxonomy'].get('phylum', 'Unknown Phylum')
        taxonomy = f"{animal['taxonomy']['kingdom']} - {phylum}"

        animal_card = f"""
        <li class="cards__item">
          <h2 class="card__title">{animal['name']}</h2>
          <p class="card__text">
            <strong>Taxonomy:</strong> {taxonomy}<br>
            <strong>Locations:</strong> {', '.join(animal['locations'])}<br>
            <strong>Characteristics:</strong> {diet} - {lifespan} lifespan<br>
            {'<strong>Type:</strong> ' + animal['characteristics']['type'] + '<br>' if 'type' in animal['characteristics'] else ''}
          </p>
        </li>
        """
        animal_info_html += animal_card

    return animal_info_html

def animal_html(output_file, animal_name):
    """Fetches animal data and generates HTML content."""
    # Fetch animal data from the API
    animals_data = data_fetcher.fetch_data(animal_name)

    # HTML template with a placeholder
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>My Animal Repository</h1>
        <ul class="cards">
            <!-- Animal cards will be inserted here -->
            __REPLACE_ANIMALS_INFO__
        </ul>
    </body>
    </html>
    """

    # Check if any data was found
    if not animals_data:
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
        # Generate the animal information string
        animal_info = generate_animal_info(animals_data)

        # Replace the placeholder with the animal information
        html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    # Write the final HTML content to a file
    with open(output_file, 'w') as file:
        file.write(html_content)

    print("Website successfully generated to the file animals.html.")

if __name__ == "__main__":
    animal_name = input("Enter a name of an animal: ")
    animal_html(output_file='animals.html', animal_name=animal_name)