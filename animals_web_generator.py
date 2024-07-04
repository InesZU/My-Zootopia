import json


def load_data(file_path):
    """ Loads a JSON file """
    file_path = "animals_data.json"
    with open("animals_data.json", "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML string"""
    output = '<li class="cards__item">\n'
    output += f' <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += '  <ul class="cards">\n'
    output += f'  <li class="cards"><strong>Scientific name:</strong> {animal_obj["taxonomy"]["scientific_name"]}</li>\n'
    output += f'  <li class="cards"><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n'
    if 'characteristics' in animal_obj and 'color' in animal_obj['characteristics']:
        output += f' <li class="cards"><strong>Color:</strong> {animal_obj["characteristics"]["color"]}</li>\n'
        output += f' <li class="cards"><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'
    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f' <li class="cards"><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'
    output += f' <li class="cards"><strong>Lifespan:</strong> {animal_obj["characteristics"]["lifespan"]}</li>\n'
    output += '  </ul>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


def generate_animal_info(data):
    """Generates the animal information string"""
    animal_info = ""
    for animal_obj in animals_data:
        animal_info += serialize_animal(animal_obj)
    return animal_info


def animal_html(data, output_file):
    # HTML template with a placeholder
    html_template = """
        <html>
        <head>
            <style>
            @gray-darker:               #444444;
            @gray-dark:                 #696969;
            @gray:                      #999999;
            @gray-light:                #cccccc;
            @gray-lighter:              #ececec;
            @gray-lightest:             lighten(@gray-lighter,4%);


            html {
              background-color: #ffe9e9;
            }

            h1 {
                text-align: center;
                font-size: 40pt;
                font-weight: normal;
            }

            body {
              font-family: 'Roboto','Helvetica Neue', Helvetica, Arial, sans-serif;
              font-style: normal;
              font-weight: 400;
              letter-spacing: 0;
              padding: 1rem;
              text-rendering: optimizeLegibility;
              -webkit-font-smoothing: antialiased;
              -moz-osx-font-smoothing: grayscale;
              -moz-font-feature-settings: "liga" on;
              width: 900px;
              margin: auto;
            }

            .cards {
              list-style: none;
              margin: 0;
              padding: 0;
            }

            .cards__item {
              background-color: white;
              border-radius: 0.25rem;
              box-shadow: 0 20px 40px -14px rgba(0,0,0,0.25);
              overflow: hidden;
              padding: 1rem;
              margin: 50px;
            }

            .card__title {
              color: @gray-dark;
              font-size: 1.25rem;
              font-weight: 300;
              letter-spacing: 2px;
              text-transform: uppercase;
            }

            .card__text {
              flex: 1 1 auto;
              font-size: 0.95rem;
              line-height: 2;
              margin-bottom: 1.25rem;
            }
            </style>
        </head>
        <body>
            <h1>My Animal Repository</h1>
            <ul class="cards">
            __REPLACE_ANIMALS_INFO__
            </ul>
        </body>
        </html>
        """

    # Generate the animal information string
    animal_info = generate_animal_info(animals_data)

    # Replace the placeholder with the animal information
    html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    # Write the final HTML content to a file
    with open('animals_template.html', 'w') as file:
        file.write(html_content)


# Load the animal data
animals_data = load_data('animals_data.json')

# Generate the HTML file with animal information
animal_html(animals_data, 'animals_template.html')
