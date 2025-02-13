from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

## Start Google Authentication
gauth = GoogleAuth()

# Load JSON credentials downloaded from Google
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = 'client_secrets.json'
# Try to use the credential .txt generated at the first 0Auth approval
gauth.LoadCredentialsFile("mycreds.txt")

# If the app was not yet authenticated it will ask to get the authentication from Google
if gauth.credentials is None:
    # Authenticate if they're not there
    # gauth.LocalWebserverAuth() # <-- WebApp approval
    gauth.CommandLineAuth()  # <-- Command Line Approva

# If credential has expired refresh
elif gauth.access_token_expired:
    gauth.Refresh()

# Initialize the saved creds
else:
    gauth.Authorize()

# Save current credentials into a TXT file for the future
gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)
