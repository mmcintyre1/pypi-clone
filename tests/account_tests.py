import pytest
import unittest.mock
from flask import Response

from pypi_org.data.users import User
from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from tests.test_client import flask_app, client


@pytest.mark.viewmodel
def test_register_validation_when_valid():
    form_data = {
        'name': 'mike',
        'email': 'm@gmail.com',
        'password': 'a' * 6,
    }

    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    target = 'pypi_org.services.user_service.find_user_by_email'
    with unittest.mock.patch(target, return_value=None):
        vm.validate()

    assert vm.error is None


@pytest.mark.viewmodel
def test_vm_register_validation_for_existing_user():
    form_data = {
        'name': 'mike',
        'email': 'm@gmail.com',
        'password': 'a' * 6,
    }

    with flask_app.test_request_context(path='/account/register', data=form_data):
        vm = RegisterViewModel()

    target = 'pypi_org.services.user_service.find_user_by_email'
    with unittest.mock.patch(target, return_value=User()):
        vm.validate()

    assert vm.error is not None
    assert 'already exists' in vm.error


@pytest.mark.view
def test_v_register_view_new_user():
    form_data = {
        'name': 'mike',
        'email': 'm@gmail.com',
        'password': 'a' * 6,
    }
    from pypi_org.views.account_views import register_post

    target = 'pypi_org.services.user_service.find_user_by_email'
    find_user = unittest.mock.patch(target, return_value=None)
    target = 'pypi_org.services.user_service.create_user'
    create_user = unittest.mock.patch(target, return_value=User())
    request = flask_app.test_request_context(path='/account/register', data=form_data)

    with find_user, create_user, request:
        resp: Response = register_post()

    assert resp.location == '/account'


@pytest.mark.integration
def test_account_home_no_login(client):
    target = 'pypi_org.services.user_service.find_user_by_id'
    with unittest.mock.patch(target, return_value=None):
        resp: Response = client.get('/account')

    assert resp.status_code == 302
    assert resp.location == 'http://localhost/account/login'


@pytest.mark.integration
def test_account_home_no_login(client):
    target = 'pypi_org.services.user_service.find_user_by_id'
    with unittest.mock.patch(target, return_value=User(name='Mike')):
        resp: Response = client.get('/account')

    assert resp.status_code == 200
