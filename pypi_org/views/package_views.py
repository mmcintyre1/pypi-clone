import flask

from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name: str):
    return {
        'package': package_service.get_package(package_name),
        'releases': package_service.get_package_releases(package_name)
    }


@blueprint.route('/<int:rank>')
# @response(template_file='packages/details.html')
def popular(rank: int):
    return f"Package details for {rank} most popular packages"
