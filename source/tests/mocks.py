from pytest_httpx import HTTPXMock


def mock_token_request_response(httpx_mock: HTTPXMock, tenant_id: str):
    url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token/'
    httpx_mock.add_response(
        method='POST',
        url=url,
        json={
            'token_type': 'Bearer',
            'expires_in': 3599,
            'ext_expires_in': 3599,
            'access_token': 'fake_access_token'
        },
        status_code=200
    )


def mock_get_list_users_response(httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        method='GET',
        url='https://graph.microsoft.com/v1.0/users/',
        json={
            '@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#users',
            'value': [
                {
                    'businessPhones': [],
                    'displayName': 'Testando, Tester Dev',
                    'givenName': None,
                    'jobTitle': None,
                    'mail': 'tester.testando.dev@accenture.com',
                    'mobilePhone': None,
                    'officeLocation': None,
                    'preferredLanguage': None,
                    'surname': None,
                    'userPrincipalName': 'tester.testando.dev_accenture.com#EXT#@bpoanaliytics.onmicrosoft.com',
                    'id': 'fab315f4-fb61-462b-95f2-9e59735c11f0'
                },
                {
                    'businessPhones': [],
                    'displayName': 'Testei Testando',
                    'givenName': 'Testei',
                    'jobTitle': None,
                    'mail': 'testei.testando@accenture.com',
                    'mobilePhone': None,
                    'officeLocation': None,
                    'preferredLanguage': None,
                    'surname': 'Testando',
                    'userPrincipalName': 'testei.testando_accenture.com#EXT#@bpoanaliytics.onmicrosoft.com',
                    'id': '6cb67dbd-7dda-461c-9779-025f6ece4af1'
                }
            ]
        },
        status_code=200
    )


def mock_get_groups_response(httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        method='GET',
        url='https://graph.microsoft.com/v1.0/groups/',
        json={
            '@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#groups',
            'value': [
                {
                    'id': '20ad61ce-7ea2-49a6-9779-025f6ece4af1',
                    'deletedDateTime': None,
                    'classification': None,
                    'createdDateTime': '2024-05-22T18:50:30Z',
                    'creationOptions': [],
                    'description': 'Controle de Usu\u00e1rios para o AD Outsystems',
                    'displayName': 'User Outsystems',
                    'expirationDateTime': None,
                    'groupTypes': [],
                    'isAssignableToRole': None,
                    'mail': None,
                    'mailEnabled': False,
                    'mailNickname': 'd7fadbb0-1',
                    'membershipRule': None,
                    'membershipRuleProcessingState': None,
                    'onPremisesDomainName': None,
                    'onPremisesLastSyncDateTime': None,
                    'onPremisesNetBiosName': None,
                    'onPremisesSamAccountName': None,
                    'onPremisesSecurityIdentifier': None,
                    'onPremisesSyncEnabled': None,
                    'preferredDataLocation': None,
                    'preferredLanguage': None,
                    'proxyAddresses': [],
                    'renewedDateTime': '2024-05-22T18:50:30Z',
                    'resourceBehaviorOptions': [],
                    'resourceProvisioningOptions': [],
                    'securityEnabled': True,
                    'securityIdentifier': 'S-1-12-1-54678-1-8832062',
                    'theme': None,
                    'uniqueName': None,
                    'visibility': None,
                    'onPremisesProvisioningErrors': [],
                    'serviceProvisioningErrors': []
                }
            ]
        },
        status_code=200
    )


def mock_get_applications_response(httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        method='GET',
        url='https://graph.microsoft.com/v1.0/applications/',
        json={
            '@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#applications',
            'value': [
                {
                    'id': '0000000-0000-0000-000-000000000000',
                    'deletedDateTime': None,
                    'appId': '00000000-0000-000000000',
                    'applicationTemplateId': None,
                    'disabledByMicrosoftStatus': None,
                    'createdDateTime': '2019-09-24T18:26:35Z',
                    'displayName': 'BPO Analytics',
                    'description': None,
                    'groupMembershipClaims': None,
                    'identifierUris': [],
                    'isDeviceOnlyAuthSupported': None,
                    'isFallbackPublicClient': None,
                    'nativeAuthenticationApisEnabled': None,
                    'notes': None,
                    'publisherDomain': 'bpotestes.com',
                    'serviceManagementReference': None,
                    'signInAudience': 'AzureADMyOrg',
                    'tags': [],
                    'tokenEncryptionKeyId': None,
                    'uniqueName': None,
                    'samlMetadataUrl': None,
                    'defaultRedirectUri': None,
                    'certification': None,
                    'optionalClaims': None,
                    'servicePrincipalLockConfiguration': None,
                    'requestSignatureVerification': None,
                    'addIns': [],
                    'api': {
                        'acceptMappedClaims': None,
                        'knownClientApplications': [],
                        'requestedAccessTokenVersion': None,
                        'oauth2PermissionScopes': [],
                        'preAuthorizedApplications': []
                    },
                    'appRoles': [],
                    'info': {
                        'logoUrl': None,
                        'marketingUrl': None,
                        'privacyStatementUrl': None,
                        'supportUrl': None,
                        'termsOfServiceUrl': None
                    },
                    'keyCredentials': [],
                    'parentalControlSettings': {
                        'countriesBlockedForMinors': [],
                        'legalAgeGroupRule': 'Allow'
                    },
                    'passwordCredentials': [],
                    'publicClient': {
                        'redirectUris': []
                    },
                    'requiredResourceAccess': [
                        {
                            'resourceAppId': '0000000-0000-0000-000-000000000000',
                            'resourceAccess': [
                                {
                                    'id': '0000000-0000-0000-000-000000000000',
                                    'type': 'Role'
                                },
                                {
                                    'id': '0000000-0000-0000-000-000000000000',
                                    'type': 'Role'
                                }
                            ]
                        },
                        {
                            'resourceAppId': '0000000-0000-0000-000-000000000000',
                            'resourceAccess': [
                                {
                                    'id': '0000000-0000-0000-000-000000000000',
                                    'type': 'Scope'
                                }
                            ]
                        }
                    ],
                    'verifiedPublisher': {
                        'displayName': None,
                        'verifiedPublisherId': None,
                        'addedDateTime': None
                    },
                    'web': {
                        'homePageUrl': None,
                        'logoutUrl': None,
                        'redirectUris': [
                            'https://app.powerbi.com/groups/me/reports/0000000-0000-0000-000-000000000000/ReportSectionb0000000000000000000'
                        ],
                        'implicitGrantSettings': {
                            'enableAccessTokenIssuance': False,
                            'enableIdTokenIssuance': False
                        },
                        'redirectUriSettings': [
                            {
                                'uri': 'https://app.powerbi.com/groups/me/reports/0000000-0000-0000-000-000000000000/ReportSectionb0000000000000000000',
                                'index': None
                            }
                        ]
                    },
                    'spa': {
                        'redirectUris': []
                    }
                }
            ]
        },
        status_code=200
    )


def mock_invitations_response(httpx_mock: HTTPXMock):
    url = 'https://graph.microsoft.com/v1.0/invitations/'
    httpx_mock.add_response(
        method='POST',
        url=url,
        status_code=201,
        json={
            '@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#invitations/$entity',
            'id': '00000000-0000-0000-0000-000000000000',
            'inviteRedeemUrl': 'https://login.microsoftonline.com/redeem?rd=https%3a%2f%2finvitations.microsoft.com%2fredeem%2f%3ftenant%3d00000000-0000-0000-0000-000000000000%26user%3d00000000-0000-0000-0000-000000000000%26ticket%3dLKUmfbccl92sxT7t%25252fceGD1l62LS%25252baV9B9ZYxDmS%25252bsAA%25253d%26ver%3d2.0',
            'invitedUserDisplayName': None,
            'invitedUserType': 'Guest',
            'invitedUserEmailAddress': 'teste.testando@gail.com',
            'sendInvitationMessage': True,
            'resetRedemption': False,
            'inviteRedirectUrl': 'https://myapplications.microsoft.com/?tenantid=00000000-0000-0000-0000-000000000000',
            'status': 'PendingAcceptance',
            'invitedUserMessageInfo': {
                'messageLanguage': None,
                'customizedMessageBody': 'Olá, você foi convidado para acessar nosso diretório.',
                'ccRecipients': [
                    {
                        'emailAddress': {
                            'name': None,
                            'address': None
                        }
                    }
                ]
            },
            'invitedUser': {
                'id': 'fb077aa8-52aa-4270-8f1b-4f6d360b2b4f'
            }
        }
    )


def mock_get_user_id_response(httpx_mock: HTTPXMock, fake_id_user: str):
    url = f'https://graph.microsoft.com/v1.0/users/{fake_id_user}'
    httpx_mock.add_response(
        method='GET',
        url=url,
        status_code=200,
        json={
            '@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#users/$entity',
            'businessPhones': [],
            'displayName': 'teste.testando',
            'givenName': None,
            'jobTitle': None,
            'mail': 'teste.testando@gail.com',
            'mobilePhone': None,
            'officeLocation': None,
            'preferredLanguage': None,
            'surname': None,
            'userPrincipalName': 'teste.testando_gail.com#EXT#@bpoanaliytics.onmicrosoft.com',
            'id': 'fb077aa8-52aa-4270-8f1b-4f6d360b2b4f'
        }
    )


def mock_get_user_filtered_response(httpx_mock: HTTPXMock):
    url = "https://graph.microsoft.com/v1.0/users/?teste.testando%40gail.com="
    httpx_mock.add_response(
        method='GET',
        url=url,
        status_code=200,
        json={
            '@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#users',
            'value': [
                {
                    'businessPhones': [],
                    'displayName': 'teste.testando',
                    'givenName': None,
                    'jobTitle': None,
                    'mail': 'teste.testando@gail.com',
                    'mobilePhone': None,
                    'officeLocation': None,
                    'preferredLanguage': None,
                    'surname': None,
                    'userPrincipalName': 'teste.testando_gail.com#EXT#@bpoanaliytics.onmicrosoft.com',
                    'id': 'fb077aa8-52aa-4270-8f1b-4f6d360b2b4f'
                }
            ]
        }
    )


def mock_update_user_data_response(httpx_mock: HTTPXMock, fake_id_user: str):
    url = f'https://graph.microsoft.com/v1.0/users/{fake_id_user}'
    httpx_mock.add_response(
        method='PATCH',
        url=url,
        status_code=204
    )


def mock_create_new_user_response(httpx_mock: HTTPXMock):
    url = 'https://graph.microsoft.com/v1.0/users/'
    httpx_mock.add_response(
        method='POST',
        url=url,
        status_code=201,
        json={
            '@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#users/$entity',
            'id': '00000000-0000-0000-0000-000000000000',
            'businessPhones': [],
            'displayName': 'Adele Vance',
            'givenName': 'Adele',
            'jobTitle': 'Product Marketing Manager',
            'mail': 'teste.testando@gail.com',
            'mobilePhone': '+1 425 555 0109',
            'officeLocation': '18/2111',
            'preferredLanguage': 'en-US',
            'surname': 'Vance',
            'userPrincipalName': 'teste.testando@gail.com'
        }
    )


def mock_invalid_create_new_user_response(httpx_mock: HTTPXMock):
    url = 'https://graph.microsoft.com/v1.0/users/'
    httpx_mock.add_response(
        method='POST',
        url=url,
        status_code=400,
        json={
            'error': {
                'code': 'Request_BadRequest',
                'message': 'The domain portion of the userPrincipalName property is invalid. You must use one of the verified domain names in your organization.',
                'details': [
                    {
                        'code': 'InvalidValue',
                        'message': 'The domain portion of the userPrincipalName property is invalid. You must use one of the verified domain names in your organization.',
                        'target': 'userPrincipalName'
                    }
                ],
                'innerError': {
                    'date': '2024-06-04T12:18:23',
                    'request-id': '00000000-0000-0000-0000-000000000000',
                    'client-request-id': '00000000-0000-0000-0000-000000000000'
                }
            }
        }
    )


def mock_delete_user_response(httpx_mock: HTTPXMock, fake_id_user: str):
    url = f'https://graph.microsoft.com/v1.0/users/{fake_id_user}'
    httpx_mock.add_response(
        method='DELETE',
        url=url,
        status_code=204,
    )


def mock_expiration_token_response(httpx_mock: HTTPXMock):
    url = 'https://graph.microsoft.com/v1.0/users/'
    httpx_mock.add_response(
        method='POST',
        url=url,
        status_code=401,
        json={
            'error': {
                'code': 'InvalidAuthenticationToken',
                'message': 'Lifetime validation failed, the token is expired.',
                'innerError': {
                    'date': '2024-06-04T12:53:08',
                    'request-id': '00000000-0000-0000-0000-000000000000',
                    'client-request-id': '00000000-0000-0000-0000-000000000000'
                }
            }
        }
    )


def mock_add_user_application_response(httpx_mock: HTTPXMock, resource_id: str):
    url = f'https://graph.microsoft.com/v1.0/applications' \
        f'/{resource_id}/appRoleAssignments'
    httpx_mock.add_response(
        method='POST',
        url=url,
        status_code=201,
        json={
            '@odata.context': "https://graph.microsoft.com/v1.0/$metadata#servicePrincipals('00000000-0000-0000-0000-000000000000')/appRoleAssignments/$entity",
            'id': '00000000-0000-0000-0000-000000000000',
            'deletedDateTime': None,
            'appRoleId': '00000000-0000-0000-0000-000000000000',
            'createdDateTime': '2024-06-04T12:54:15.9126515Z',
            'principalDisplayName': 'teste.testando',
            'principalId': 'fb077aa8-52aa-4270-8f1b-4f6d360b2b4f',
            'principalType': 'User',
            'resourceDisplayName': 'EHR_FUTUREBPO_EXT',
            'resourceId': '00000000-0000-0000-0000-000000000000'
        }
    )


def mock_get_info_application_response(httpx_mock: HTTPXMock, resource_id: str):
    url = f'https://graph.microsoft.com/v1.0/applications/{resource_id}'
    httpx_mock.add_response(
        method='GET',
        url=url,
        status_code=201,
        json={
            "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#servicePrincipals/$entity",
            "id": "00000000-0000-0000-0000-000000000000",
            "deletedDateTime": None,
            "accountEnabled": True,
            "alternativeNames": [],
            "appDisplayName": "EHR_FUTUREBPO",
            "appDescription": None,
            "appId": "00000000-0000-0000-0000-000000000000",
            "applicationTemplateId": "00000000-0000-0000-0000-000000000000",
            "appOwnerOrganizationId": "00000000-0000-0000-0000-000000000000",
            "appRoleAssignmentRequired": True,
            "createdDateTime": "2024-04-30T17:30:49Z",
            "description": None,
            "disabledByMicrosoftStatus": None,
            "displayName": "EHR_FUTUREBPO",
            "homepage": "https://*.abc.defggh.com|ISV9.2|primary|z",
            "loginUrl": None,
            "logoutUrl": "https://abc.defggh.com/SLO.aspx",
            "notes": None,
            "notificationEmailAddresses": [
                "yuri.motoshima@accenture.com"
            ],
            "preferredSingleSignOnMode": "saml",
            "preferredTokenSigningKeyThumbprint": "00000000000000000000000000000000",
            "replyUrls": [
                "https://abc.defggh.com/SSO.aspx"
            ],
            "servicePrincipalNames": [
                "http://abc.defggh.com",
                "00000000-0000-0000-0000-000000000000"
            ],
            "servicePrincipalType": "Application",
            "signInAudience": "AzureADMyOrg",
            "tags": [
                "WindowsAzureActiveDirectoryIntegratedApp"
            ],
            "tokenEncryptionKeyId": None,
            "addIns": [],
            "appRoles": [
                {
                    "allowedMemberTypes": [
                        "User"
                    ],
                    "description": "msiam_access",
                    "displayName": "msiam_access",
                    "id": "00000000-0000-0000-0000-000000000000",
                    "isEnabled": True,
                    "origin": "Application",
                    "value": None
                }
            ],
            "info": {
                "logoUrl": None,
                "marketingUrl": None,
                "privacyStatementUrl": None,
                "supportUrl": None,
                "termsOfServiceUrl": None
            },
            "keyCredentials": [
                {
                    "customKeyIdentifier": "000000000000000000000000",
                    "displayName": "CN=Microsoft Azure Federated SSO Certificate",
                    "endDateTime": "2027-04-30T17:34:16Z",
                    "key": None,
                    "keyId": "0fced439-9397-45f9-bd0b-7035927630b9",
                    "startDateTime": "2024-04-30T17:34:16Z",
                    "type": "AsymmetricX509Cert",
                    "usage": "Verify"
                }
            ],
            "oauth2PermissionScopes": [
                {
                    "adminConsentDescription": "Allow the application to access EHR_FUTUREBPO on behalf of the signed-in user.",
                    "adminConsentDisplayName": "Access EHR_FUTUREBPO",
                    "id": "00000000-0000-0000-0000-000000000000",
                    "isEnabled": True,
                    "type": "User",
                    "userConsentDescription": "Allow the application to access EHR_FUTUREBPO on your behalf.",
                    "userConsentDisplayName": "Access EHR_FUTUREBPO",
                    "value": "user_impersonation"
                }
            ],
            "passwordCredentials": [
                {
                    "customKeyIdentifier": "000000000000000000000000",
                    "displayName": "CN=Microsoft Azure Federated SSO Certificate",
                    "endDateTime": "2027-04-30T17:34:16Z",
                    "hint": None,
                    "keyId": "00000000-0000-0000-0000-000000000000",
                    "secretText": None,
                    "startDateTime": "2024-04-30T17:34:16Z"
                }
            ],
            "resourceSpecificApplicationPermissions": [],
            "samlSingleSignOnSettings": {
                "relayState": ""
            },
            "verifiedPublisher": {
                "displayName": None,
                "verifiedPublisherId": None,
                "addedDateTime": None
            }
        }
    )
