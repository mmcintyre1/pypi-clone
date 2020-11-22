import flask

from pypi_org.views import home_views
from pypi_org.views import package_views


app = flask.Flask(__name__)
app.register_blueprint(home_views.blueprint)
app.register_blueprint(package_views.blueprint)


if __name__ == '__main__':
    app.run(debug=True)
