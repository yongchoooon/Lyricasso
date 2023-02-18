import requests
import base64

# Define the authorization endpoint and parameters
auth_url = "https://accounts.spotify.com/authorize"
client_id = "a653f099fbd54d0699b5c48863305cce"
response_type = "code"
redirect_uri = "http://localhost:8000/callback"
scope = "user-library-read"  # Replace with the scopes you need
state = "123"

# Build the authorization URL
auth_params = {
    "client_id": client_id,
    "response_type": response_type,
    "redirect_uri": redirect_uri,
    "scope": scope,
    "state": state,
}
auth_url = f"{auth_url}?{requests.compat.urlencode(auth_params)}"

# Redirect the user to the authorization URL
print(f"Please authorize the app by visiting:\n{auth_url}")
auth_code = input("Enter the authorization code from the URL: ")

# Exchange the authorization code for an access token
token_url = "https://accounts.spotify.com/api/token"
client_secret = "3d23d1ac9c454bc4af38cf6c61e4a17d"
grant_type = "authorization_code"
auth_header = f"{client_id}:{client_secret}"
auth_header = base64.b64encode(auth_header.encode("utf-8")).decode("utf-8")
token_params = {
    "grant_type": grant_type,
    "code": auth_code,
    "redirect_uri": redirect_uri,
}
token_headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/x-www-form-urlencoded",
}
response = requests.post(token_url, headers=token_headers, data=token_params)
tokens = response.json()
access_token = tokens["access_token"]

print("access_token : ", access_token)
