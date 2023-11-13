from lxml import etree
import json

data = {"elements":[]}
tree = etree.parse("xml/GetAllModuleElementsResponse.xml")
for me in tree.findall(".//{http://www.everest.nl/aquima/studio/ManagementService/1.0}ModuleElementKey"):
    if me.attrib["ModuleElementType"] == "TextItem":
        data["elements"].append(me.attrib["Name"])

print(json.dumps(data))
