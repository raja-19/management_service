import sys
import requests
from requests.auth import HTTPBasicAuth

username, password, repository =  sys.argv[1:]

url = "https://meet-encore.blueriq.com/Studio/Server/Services/ManagementService"
headers = {"Content-Type": "text/xml","SOAPAction": "CreateFeatureBranch"}
auth = HTTPBasicAuth(username, password)

body = ""
with open("xml/CreateFeatureBranchRequest.xml", 'r') as file:
    body = file.read()

body = body.replace("$REPOSITORY", repository)
requests.post(url, auth=auth, headers=headers, data=body)
