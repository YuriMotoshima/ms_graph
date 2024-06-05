from json import loads

from httpx import Client, Request

from app.data.schemas import AddUserApp, InvitationUser, NewUser


class MSGraph:
    path_user = '/users/'
    path_groups = '/groups/'
    path_applications = '/applications/'
    path_services = '/servicePrincipals/'
    path_invitations = '/invitations/'
    
    def __url_login(self,
        token_app): return f'https://login.microsoftonline.com/{token_app}/oauth2/v2.0/token/'
    
    
    def __credentials_azure(self, azure_data:dict) -> None:
        if azure_data is None:
            raise ValueError("Empty Credentials.")
        return azure_data


    def __init__(self, azure_data: dict) -> None:
        self.azure_data = self.__credentials_azure(azure_data=azure_data)
        self.headers = {'Content-Type': 'application/json'}
        self.url_graph = 'https://graph.microsoft.com/v1.0'
        

    def get_token(self, token_app: str = None) -> None:
        token_app = token_app or self.azure_data['token_app']
        self.client = Client()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'fpc=AikroW4keohAskOlaTR3wPzC6MHkAQAAAFHA5t0OAAAA'
        }
        url = self.__url_login(token_app=token_app)
        payload = f'client_id={self.azure_data['client_id_app']}&scope=https%3A%2F%2Fgraph.microsoft.com%2F.default&' \
        f'client_secret={self.azure_data['secret_id_app']}&grant_type=client_credentials'
        
        try:
            response = self.client.post(url=url, headers=headers, data=payload)
            self.access_token = loads(response.content)["access_token"]
            
        finally:
            self.client.close()
        
        
    def request(self, method:str, path:str, headers:dict = None, params:dict = None, data:dict = None) -> object:
        def create_session(method:str, path:str, headers:dict = None, params:dict = None, data:dict = None) -> object:
            self.get_token()
            self.client = Client()
            url = self.url_graph + path
            headers = headers or self.headers
            headers['Authorization'] = f'Bearer {self.access_token}'
            request = Request(method=method.upper(), url=url, headers=headers, data=data or None, params=params or None)
            return request
        
        try:
            request = create_session(method=method, path=path, headers=headers, params=params, data=data)
            response = self.client.send(request)
        finally:
            self.client.close()
        
        return response
    
    
    def get_user(self, id_user:str) -> dict:
        path = self.path_user + id_user
        return loads(self.request(method='get', path=path).content)


    def get_list_users(self) -> dict:
        path = self.path_user
        return loads(self.request(method='get', path=path).content)


    def get_user_filter(self, filter:dict) -> dict:
        path = self.path_user
        return loads(self.request(method='get', path=path, params=filter).content)
    
    
    def update_user(self, id_user:str, data:dict) -> object:
        path = self.path_user + id_user
        return self.request(method='patch', path=path, data=data)
        
        
    def create_new_user(self, data:NewUser) -> dict:
        data = NewUser(**data)
        path = self.path_user
        return loads(self.request(method='get', path=path, data=data).content)
        
    
    def delete_user(self, id_user:str) -> object:
        path = self.path_user + id_user
        return self.request(method='delete', path=path)
        
    
    def get_groups(self) -> dict:
        path = self.path_groups
        return loads(self.request(method='get', path=path).content)
        

    def get_applications(self) -> dict:
        path = self.path_applications
        return loads(self.request(method='get', path=path).content)


    def get_info_application(self, resource_id:str) -> dict:
        path = self.path_applications + resource_id
        return loads(self.request(method='get', path=path).content)


    def add_user_application(self, resource_id:str, data:AddUserApp) -> dict:
        data = AddUserApp(**data)
        path = self.path_applications + resource_id + '/appRoleAssignments'
        return loads(self.request(method='post', path=path, data=data).content)


    def invite_user(self, data:InvitationUser) -> dict:
        data = InvitationUser(**data)
        path = self.path_invitations
        return loads(self.request(method='post', path=path, data=data).content)


    def get_services(self) -> dict:
        path = self.path_services
        return loads(self.request(method='get', path=path).content)
        