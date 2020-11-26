import pathlib

from pypi_org.data import db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def init_db():
    db_file = pathlib.Path(__file__).parent.parent / 'db' / 'pypi_org.sqlite'
    db_session.global_init(str(db_file))


def insert_a_package():
    p = Package()
    p.id = input('Package id / name: ').strip().lower()
    p.summary = input('Package summary: ').strip()
    p.author_name = input('Author: ').strip()
    p.license = input('License: ').strip()

    r = Release()
    r.major_ver = int(input('Major version: '))
    r.minor_ver = int(input('Minor version: '))
    r.build_ver = int(input('Build version: '))
    r.size = int(input('Size (in bytes): '))

    p.releases.append(r)

    session = db_session.create_session()
    session.add(p)
    session.commit()


def main():
    init_db()
    while True:
        insert_a_package()


if __name__ == '__main__':
    main()
