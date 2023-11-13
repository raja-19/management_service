from lxml import etree  
import json

data = {}
tree = etree.parse("xml/GetModulesResponse.xml")
module = tree.find(".//{http://www.everest.nl/aquima/studio/ManagementService/1.0}ModuleKey[@ModuleType='Interaction']");
data["name"] = module.attrib["Name"]
print(json.dumps(data))
