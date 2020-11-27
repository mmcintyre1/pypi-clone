import flask

from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name: str):
    if not package_name.strip().lower():
        return flask.abort(404)

    package = package_service.get_package_by_id(package_name.strip().lower())

    if not package:
        return flask.abort(404)

    latest_release = package.releases[0]
    latest_version = latest_release.version_text
    release_version = latest_release.version_text
    is_latest = True

    return {
        'package': package,
        'latest_version': latest_version,
        'latest_release': latest_release,
        'release_version': release_version,
        'is_latest': is_latest,
    }


@blueprint.route('/<int:rank>')
# @response(template_file='packages/details.html')
def popular(rank: int):
    return f"Package details for {rank} most popular packages"
