import sys
import requests
from requests.auth import HTTPBasicAuth

username, password = sys.argv[1:]

url = "https://meet-encore.blueriq.com/Studio/Server/Services/ManagementService"
headers = {"Content-Type": "text/xml","SOAPAction": "ApplyOperations"}
auth = HTTPBasicAuth(username, password)

body = ""
with open("xml/ApplyOperationsRequest.xml", 'r') as file:
    body = file.read()

requests.post(url, auth=auth, headers=headers, data=body)
