import requests
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree 
import json

url = "https://meet-encore.blueriq.com/Studio/Server/Services/ManagementService"
headers = {"Content-Type": "text/xml","SOAPAction": "GetModules"}
auth = HTTPBasicAuth('ansar', 'BszxQfkLCS2TDmJ')

repository = "Kinderbijslag"
project = "Kinderbijslag"

body = ""
with open("xml/GetModulesRequest.xml", 'r') as file:
    body = file.read()

body = body.replace("$REPOSITORY", repository)
body = body.replace("$PROJECT", project)

response = requests.post(url, auth=auth, headers=headers, data=body)

module = ""
tree = ElementTree.fromstring(response.content)
for m in tree.findall(".//{http://www.everest.nl/aquima/studio/ManagementService/1.0}ModuleKey"):
    if m.attrib["ModuleType"] == "Interaction":
        module = m.attrib["Name"]
        break

with open("xml/GetAllModuleElements.xml", 'r') as file:
    body = file.read()

body = body.replace("$REPOSITORY", repository)
body = body.replace("$PROJECT", project)
body = body.replace("$MODULE", module)

headers["SOAPAction"] = "GetAllModuleElements"
response = requests.post(url, auth=auth, headers=headers, data=body)

elements = []
tree = ElementTree.fromstring(response.content)

for me in tree.findall(".//{http://www.everest.nl/aquima/studio/ManagementService/1.0}ModuleElementKey"):
    if me.attrib["ModuleElementType"] == "TextItem":
        elements.append(me.attrib["Name"])

with open("xml/GetModuleElementRequest.xml", 'r') as file:
    body = file.read()

body = body.replace("$REPOSITORY", repository)
body = body.replace("$PROJECT", project)
body = body.replace("$MODULE", module)
headers["SOAPAction"] = "GetModuleElement"

data = {}

for element in elements:
    tmp = body.replace("$ELEMENT", element)
    response = requests.post(url, auth=auth, headers=headers, data=tmp)

    tree = ElementTree.fromstring(response.content)
    nodeset = tree.find(".//NodeSet[@Language='Nederlands']")
    node = nodeset.find(".//Node[@{http://www.w3.org/2001/XMLSchema-instance}type='q1:TextNode']")
    if node != None:
        data[element] = node.attrib["Text"]

print(json.dumps(data))
