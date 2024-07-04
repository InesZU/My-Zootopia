import json


def load_data(file_path):
    """ Loads a JSON file """

    with open("animals_data.json", "r") as handle:
        return json.load(handle)


def generate_animal_info():
    """Generates the animal information string"""
    animal_info = ""
    for animal in animals_data:
        animal_info += '<li class="cards__item">\n'
        animal_info += f"<div class='card__title'> {animal['name']}</div>\n"
        animal_info += '  <p class="card__text">\n'
        animal_info += f' <strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n'
        animal_info += f' <strong>Location:</strong> {", ".join(animal['locations'])}<br/>\n'
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            animal_info += f' <strong>Type:</strong> {animal['characteristics']['type']}<br/>\n'
        animal_info += '  </p>\n'
        animal_info += '</li>\n'
    return animal_info


def animal_html(output_file):
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
    animal_info = generate_animal_info()

    # Replace the placeholder with the animal information
    html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    # Write the final HTML content to a file
    with open("animals_template.html", 'w') as file:
        file.write(html_content)


# Load the animal data
animals_data = load_data('animals_data.json')

# Generate the HTML file with animal information
animal_html(output_file='animals_template.html')
