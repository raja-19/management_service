from lxml import etree
import json

tree = etree.parse("xml/GetModuleElementResponse.xml")
element = tree.find(".//{http://www.everest.nl/aquima/studio/ManagementService/1.0}GetModuleElementResult")
node = element.find(".//NodeSet[@Language='Nederlands']").find(".//Node[@{http://www.w3.org/2001/XMLSchema-instance}type='q1:TextNode']")

data = {}
if node != None:
    data["name"] = element.attrib["Name"]
    data["nl-text"] = node.attrib["Text"]

print(json.dumps(data))
