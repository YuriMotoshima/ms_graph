from pydantic import BaseModel, EmailStr, ValidationError


class PassProfile(BaseModel):
    forceChangePasswordNextSignIn: bool
    
class NewUser(BaseModel):
    accountEnabled: bool
    displayName: str
    mailNickname: str
    userPrincipalName: EmailStr
    passwordProfile: PassProfile

class AddUserApp(BaseModel):
  principalId: str
  resourceId: str
  appRoleId: str
  
class MessageInvitation(BaseModel):
    customizedMessageBody:str

class InvitationUser(BaseModel):
    invitedUserEmailAddress: EmailStr
    inviteRedirectUrl: str
    sendInvitationMessage: bool
    invitedUserMessageInfo: MessageInvitation