import flask
import pathlib

from pypi_org.views import home_views
from pypi_org.views import account_views
from pypi_org.views import package_views
from pypi_org.views import cms_views
import pypi_org.data.db_session as db_session


app = flask.Flask(__name__)

db_file = pathlib.Path(__file__).parent / 'db' / 'pypi_org.sqlite'
db_session.global_init(str(db_file))

app.register_blueprint(blueprint=home_views.blueprint)
app.register_blueprint(blueprint=package_views.blueprint)
app.register_blueprint(blueprint=cms_views.blueprint)
app.register_blueprint(blueprint=account_views.blueprint)


if __name__ == '__main__':
    app.run(debug=True)
