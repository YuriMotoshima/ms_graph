from json import load

from app.modules.ms_graph import MSGraph

azure_data = None

with open('./azure_data.json') as config_file:
    azure_data = load(config_file) or None

        
if __name__ == "__main__":
    api = MSGraph(azure_data=azure_data)
    # response = api.get_user_filter(filter={"$filter":"mail eq 'yuri.motoshima@gmail.com'"})
    # new_user = {
    #     "accountEnabled": True,
    #     "displayName": "Marto, Gabriel Diniz",
    #     "mailNickname": "Marto",
    #     "userPrincipalName": "gabriel.diniz.marto@gmail.com",
    #     "passwordProfile" : {
    #         "forceChangePasswordNextSignIn": True
    #         },
    #     "teste":"bnovo_"
    #     }
    
    # response = api.create_new_user(data=new_user)
    response = api.add_user_applications()
    

    print()