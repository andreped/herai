from flask import Flask, render_template
import yaml
from yaml.loader import SafeLoader

app = Flask("SINTEF MedIA Catalogue")

@app.route("/")
def main():
    ctx = load_catalogue()
    return render_template("catalogue.jinja2", title="Catalogue", **ctx)   # By default, Flask expects your templates in a templates/ directory

@app.route("/app")
def catalogue():
    return render_template("application_template.jinja2")


def load_catalogue(catalogue_configuration_file: str='resources/catalogue.yaml') -> dict:
    catalogue_file = yaml.load(open(catalogue_configuration_file, 'r'), Loader=SafeLoader)
    return catalogue_file


if __name__ == '__main__':
    app.run(debug=True)

