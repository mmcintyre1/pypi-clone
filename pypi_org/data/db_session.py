import sqlalchemy as sa
import sqlalchemy.orm as orm

from pypi_org.data.modelbase import SqlAlchemyBase

factory = None


def global_init(db_file: str):
    global factory

    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    conn_str = f'sqlite:///{db_file.strip()}'
    print(f"Connecting to DB with {conn_str}")
    engine = sa.create_engine(conn_str, echo=False)

    factory = orm.sessionmaker(bind=engine)

    import pypi_org.data.__all_models
    SqlAlchemyBase.metadata.create_all(engine)
