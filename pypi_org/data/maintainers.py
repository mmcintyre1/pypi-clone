from datetime import datetime
import sqlalchemy as sa

from pypi_org.data.modelbase import SqlAlchemyBase


class Maintainers(SqlAlchemyBase):
    __tablename__ = 'maintainers'

    user_id = sa.Column(sa.String, primary_key=True)
    package_id = sa.Column(sa.String, primary_key=True)
