So you want a simplish way to convert YAML to HTML with the option of Markdown formatting template?

Look no further - thanks to a load of libraries, such as Jinja2, pyyaml, jinja-markdown, pyadantic
and pydantic-yaml!

## Components

### `y2h.py`
Aka YAML-to-HTML.

Takes test_data.yaml, loads `template.html` and spits out `output.html`, then load `output.html`
in your favourite browser.

### `example.html`

Here's one I made earlier

### `template.html`
A Jinja2 template https://jinja.palletsprojects.com/en/3.1.x/templates/. Entries are available using the 
`directory.entries` property.

Everything between `{% markdown %}` and `{% endmarkdown %}` is rendered as Markdown

### `test_data.yaml`

Data created by `create_test_data.py` using `models.py`

### `models.py`

Rather than freestyling the YAML, the models define the schema.

## Usage

### Requirements

- Python >= 3.8

### Installation

    pip3 install -r requirements.txt

### Data

#### Programmatically

1. Edit `create_test_data.py`
2. Run ```python3 create_test_data.py```

#### Manually

1. Edit `test_data.yaml`
2. Don't make any mistakes

### Template

1. Edit template.html with your HTML, Markdown and CSS vodoo.

### Run

1. Run ```python3 y2h.py```
2. Open `output.html` in a browser
    

