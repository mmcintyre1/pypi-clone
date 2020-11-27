import sqlalchemy.orm
from typing import List

import pypi_org.data.db_session as db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def get_latest_releases(limit=10) -> List[Release]:
    session = db_session.create_session()
    releases = session.query(Release)\
        .options(sqlalchemy.orm.joinedload(Release.package))\
        .order_by(Release.created_date.desc())\
        .limit(limit)\
        .all()
    session.close()
    return releases


def get_package_count() -> int:
    session = db_session.create_session()
    return session.query(Package).count()


def get_release_count() -> int:
    session = db_session.create_session()
    return session.query(Release).count()


def get_package_by_id(package_name):
    session = db_session.create_session()
    package = session.query(Package) \
        .options(sqlalchemy.orm.joinedload(Package.releases)) \
        .filter_by(id=package_name)\
        .order_by(Release.created_date.desc()) \
        .first()
    session.close()
    return package
