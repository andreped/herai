from flask import Flask, render_template
import yaml
from yaml.loader import SafeLoader

app = Flask("SINTEF MIA Catalogue")
APP_DICT = dict()

@app.route("/")
def main():
    ctx = load_catalogue()
    for app in ctx['apps']:
        APP_DICT[app['name']] = app
    return render_template("catalogue.jinja2", title="Catalogue", **ctx)   # By default, Flask expects your templates in a templates/ directory

@app.route("/application/<string:app_name>")
def application(app_name):
    return render_template("{}.jinja2".format(app_name.lower()), **{'app_name': app_name.capitalize()})


# @app.route("process/<string:app_name>", methods=['GET', 'POST'])
# def process(app_name):
#     if request.method == 'POST':
#         # Forward the uploaded data to the corresponding service
#         APP_DICT[app_name].


def load_catalogue(catalogue_configuration_file: str='resources/catalogue.yaml') -> dict:
    catalogue_file = yaml.load(open(catalogue_configuration_file, 'r'), Loader=SafeLoader)
    return catalogue_file


if __name__ == '__main__':
    app.run(debug=True)

