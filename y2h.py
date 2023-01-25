from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja_markdown import MarkdownExtension

import models

with open('test_data.yaml', 'r') as yaml_f:
    directory = models.Directory.parse_raw(yaml_f.read())

jinja_env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape()
)

jinja_env.add_extension(MarkdownExtension)

template = jinja_env.get_template("template.html")

html = template.render(directory=directory)

with open('example.html', 'w', encoding='utf-8') as html_f:
    html_f.write(html)