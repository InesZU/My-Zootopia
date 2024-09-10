import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes a single animal object into HTML format with each field in its own list item."""
    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += '    <ul class="card__details">\n'

    # Append location information
    if 'locations' in animal_obj and len(animal_obj['locations']) > 0:
        output += f'      <li class="card__detail-item"><strong>Location:</strong> {", ".join(animal_obj["locations"])}</li>\n'

    # Append type information
    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f'      <li class="card__detail-item"><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'

    # Append diet information
    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f'      <li class="card__detail-item"><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n'

    # Append color information
    if 'characteristics' in animal_obj and 'color' in animal_obj['characteristics']:
        output += f'      <li class="card__detail-item"><strong>Color:</strong> {animal_obj["characteristics"]["color"]}</li>\n'

    # Append lifespan information
    if 'characteristics' in animal_obj and 'lifespan' in animal_obj['characteristics']:
        output += f'      <li class="card__detail-item"><strong>Lifespan:</strong> {animal_obj["characteristics"]["lifespan"]}</li>\n'

    output += '    </ul>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


# Main code to generate the HTML file
def generate_html(animals_data, template_path, output_path):
    """Generates an HTML file by serializing animal data into a predefined template."""
    # Initialize an empty string for the list of animals
    output = '<ul class="cards">\n'

    # Loop through each animal and serialize its data
    for animal in animals_data:
        output += serialize_animal(animal)

    # Close the unordered list tag
    output += '</ul>\n'

    # Load the HTML template
    with open(template_path, "r") as template_file:
        html_template = template_file.read()

    # Replace the placeholder in the template with the serialized animal data
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    # Write the final HTML to the output file
    with open(output_path, "w") as output_file:
        output_file.write(html_output)

    print(f"HTML file has been generated and saved to {output_path}!")


# Example usage
if __name__ == "__main__":
    # Load animal data from the JSON file
    animals_data = load_data('animals_data.json')

    # Generate the HTML output
    generate_html(animals_data, 'animals_template.html', 'animals.html')