from json import load

import pytest
from pytest_httpx import HTTPXMock

from app.modules.ms_graph import MSGraph
from tests.mocks import (mock_add_user_application_response,
                         mock_create_new_user_response,
                         mock_delete_user_response,
                         mock_get_applications_response,
                         mock_get_groups_response,
                         mock_get_info_application_response,
                         mock_get_list_users_response,
                         mock_get_user_filtered_response,
                         mock_get_user_id_response,
                         mock_invalid_create_new_user_response,
                         mock_invitations_response,
                         mock_token_request_response,
                         mock_update_user_data_response)

azure_data = None
with open('./azure_data.json') as config_file:
    azure_data = load(config_file) or None
    azure_data['fake_user'] = 'fb077aa8-52aa-4270-8f1b-4f6d360b2b4f'


@pytest.fixture
def ms_graph_instance():
    return MSGraph(azure_data=azure_data)


@pytest.fixture
def valid_user_data_invitation_payload():
    return {
        'invitedUserEmailAddress': 'teste.testando@gail.com',
        'inviteRedirectUrl': f'https://myapplications.microsoft.com/?tenantid={azure_data['token_app']}',
        'sendInvitationMessage': True,
        'invitedUserMessageInfo': {
            'customizedMessageBody': 'Olá, você foi convidado para acessar nosso diretório.'
        }
    }


@pytest.fixture
def invalid_user_data_invitation_payload():
    return {
        'invitedUserEmailAddress': 'teste.testando$$$gail.com',
        'inviteRedirectUrl': f'https://myapplications.microsoft.com/?tenantid={azure_data['token_app']}',
        'sendInvitationMessage': True,
        'invitedUserMessageInfo': {
            'customizedMessageBody': 'Olá, você foi convidado para acessar nosso diretório.'
        }
    }


@pytest.fixture
def valid_user_data_payload():
    return {
        'accountEnabled': True,
        'displayName': 'Testanto, Teste T',
        'mailNickname': 'Testanto',
        'userPrincipalName': 'testanto.teste.t@testtt.com',
        'passwordProfile': {
            'forceChangePasswordNextSignIn': True
        }
    }


@pytest.fixture
def invalid_user_data_payload():
    return {
        'accountEnabled': True,
        'displayName': 'Testanto, Teste T',
        'mailNickname': 'Testanto',
        'userPrincipalName': 'testanto.teste.t####testtt.com',
        'passwordProfile': {
            'forceChangePasswordNextSignIn': True
        }
    }


@pytest.fixture
def valid_update_user_data_payload():
    return {
        'jobTitle': 'Senior Manager'
    }


@pytest.fixture
def valid_add_user_application_payload():
    return {
    'principalId': azure_data['fake_user'],
    'resourceId': azure_data['resource_id'],
    'appRoleId': azure_data['app_role_id']
    }


@pytest.fixture
def assert_all_responses_were_requested() -> bool:
    return False


@pytest.fixture(autouse=True)
def mock_httpx_requests(httpx_mock: HTTPXMock):
    mock_get_applications_response(httpx_mock)
    mock_token_request_response(httpx_mock, azure_data['token_app'])
    mock_get_groups_response(httpx_mock)
    mock_get_list_users_response(httpx_mock)
    mock_invitations_response(httpx_mock)
    mock_get_user_id_response(httpx_mock, azure_data['fake_user'])
    mock_get_user_filtered_response(httpx_mock)
    mock_update_user_data_response(httpx_mock, azure_data['fake_user'])
    mock_create_new_user_response(httpx_mock)
    mock_invalid_create_new_user_response(httpx_mock)
    mock_delete_user_response(httpx_mock, azure_data['fake_user'])
    mock_add_user_application_response(httpx_mock, azure_data['resource_id'])
    mock_get_info_application_response(httpx_mock, azure_data['resource_id'])
    