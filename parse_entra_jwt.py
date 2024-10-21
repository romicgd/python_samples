import json
from typing import Dict
from msal.oauth2cli.oidc import decode_id_token 

token:str = "<bearer token content>"
token_client_id:str="<token_audience_here>"
token_issuer:str = "https://sts.windows.net/<tenant_id>/"
decodedAccessToken: Dict[str, int] = decode_id_token(token, client_id=token_client_id, issuer=token_issuer)
accessTokenFormatted:str = json.dumps(decodedAccessToken, indent=2) 
print (decodedAccessToken["aud"])
print (decodedAccessToken["upn"])
print (accessTokenFormatted)