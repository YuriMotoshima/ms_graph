import pytest
from pytest_httpx import HTTPXMock

from tests.conftest import azure_data
from tests.mocks import mock_token_request_response


@pytest.fixture(autouse=True)
def mock_token_request(httpx_mock: HTTPXMock):
    mock_token_request_response(httpx_mock, azure_data['token_app'])


def test_token_request(ms_graph_instance):
    response = ms_graph_instance.get_token()
    assert response == None
    assert ms_graph_instance.access_token != None


@pytest.mark.parametrize('method_name, endpoint_path', [
    ('get_list_users', '/users/'),
    ('get_groups', '/groups/'),
    ('get_applications', '/applications/'),
])
def test_generic_get_methods(ms_graph_instance, method_name, endpoint_path):
    method = getattr(ms_graph_instance, method_name)
    response = method()
    assert 'value' in response  # Verifica se a resposta possui a chave 'value'
    assert isinstance(response['value'], list)  # Verifica se o valor de 'value' é uma lista


def test_invitation_request(ms_graph_instance, valid_user_data_invitation_payload):
    response = ms_graph_instance.invite_user(valid_user_data_invitation_payload)
    assert response['id'] == '00000000-0000-0000-0000-000000000000'
    assert response['status'] == 'PendingAcceptance'


def test_invalid_invitation_request(ms_graph_instance, invalid_user_data_invitation_payload):
    with pytest.raises(Exception) as excinfo:
        ms_graph_instance.invite_user(invalid_user_data_invitation_payload)
    assert 'The email address is not valid.' in str(excinfo.value) 


def test_get_user_by_id(ms_graph_instance):
    fake_id_user = 'fb077aa8-52aa-4270-8f1b-4f6d360b2b4f'
    response = ms_graph_instance.get_user(fake_id_user)
    assert response['id'] == fake_id_user
    assert response['displayName'] == 'teste.testando'


def test_get_user_filtered(ms_graph_instance):
    response = ms_graph_instance.get_user_filter('teste.testando@gail.com')
    assert response['value'][0]['mail'] == 'teste.testando@gail.com'


def test_update_user(ms_graph_instance, valid_update_user_data_payload):
    fake_id_user = 'fb077aa8-52aa-4270-8f1b-4f6d360b2b4f'
    response = ms_graph_instance.update_user(fake_id_user, valid_update_user_data_payload)
    assert response.status_code == 204  # 204 No Content


def test_create_new_user(ms_graph_instance, valid_user_data_payload):
    response = ms_graph_instance.create_new_user(valid_user_data_payload)
    assert response['value'][0]['displayName'] == 'Testando, Tester Dev'


def test_invalid_create_new_user(ms_graph_instance, invalid_user_data_payload):
    with pytest.raises(Exception) as excinfo:
        ms_graph_instance.create_new_user(invalid_user_data_payload)
    assert 'The email address is not valid.' in str(excinfo.value) 


def test_delete_user(ms_graph_instance):
    fake_id_user = 'fb077aa8-52aa-4270-8f1b-4f6d360b2b4f'
    response = ms_graph_instance.delete_user(fake_id_user)
    assert response.status_code == 204 


def test_add_user_application(ms_graph_instance, valid_add_user_application_payload):
    resource_id = valid_add_user_application_payload['resourceId']
    response = ms_graph_instance.add_user_application(resource_id, valid_add_user_application_payload)
    assert response['id'] == '00000000-0000-0000-0000-000000000000'


def test_get_info_application(ms_graph_instance, valid_add_user_application_payload):
    resource_id = valid_add_user_application_payload['resourceId']
    response = ms_graph_instance.get_info_application(resource_id)
    assert response['id'] == '00000000-0000-0000-0000-000000000000'
    assert response['displayName'] == 'EHR_FUTUREBPO'
