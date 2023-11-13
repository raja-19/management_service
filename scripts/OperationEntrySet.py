import sys
from lxml import etree
import json

element_name, nl_text = sys.argv[1:]

request = etree.parse("xml/ApplyOperationsRequest.xml")
element = request.find(".//{http://www.everest.nl/aquima/studio/ManagementService/1.0}ModuleElement[@Name='" + element_name + "']")
node = element.find(".//NodeSet[@Language='Nederlands']").find(".//Node[@{http://www.w3.org/2001/XMLSchema-instance}type='q1:TextNode']")
node.attrib["Text"] = nl_text

with open("xml/ApplyOperationsRequest.xml", 'w') as file:
    file.write(etree.tostring(request, encoding="unicode"))
