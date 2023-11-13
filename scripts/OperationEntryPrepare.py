import sys
from lxml import etree
import json

project, module = sys.argv[1:]

element = etree.parse("xml/GetModuleElementResponse.xml")
name = element.find(".//{http://www.everest.nl/aquima/studio/ManagementService/1.0}GetModuleElementResult").attrib["Name"]
nl_text = element.find(".//NodeSet[@Language='Nederlands']").find(".//Node[@{http://www.w3.org/2001/XMLSchema-instance}type='q1:TextNode']").attrib["Text"]

entry_xml = ""
with open("xml/OperationEntryTemplate.xml", 'r') as file:
    entry_xml = file.read()

entry_xml = entry_xml.replace("$PROJECT", project); 
entry_xml = entry_xml.replace("$MODULE", module); 
entry_xml = entry_xml.replace("$NAME", name);
entry_xml = entry_xml.replace("$NL-TEXT", nl_text);

entry = etree.fromstring(entry_xml)

request = etree.parse("xml/ApplyOperationsRequest.xml")
operations = request.find(".//{http://www.everest.nl/aquima/studio/ManagementService/1.0}Operations")
operations.append(entry)

request_xml = etree.tostring(request, encoding="unicode")

with open("xml/ApplyOperationsRequest.xml", 'w') as file:
    file.write(request_xml)
