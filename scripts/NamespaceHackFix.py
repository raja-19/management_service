request = ""
with open("xml/ApplyOperationsRequest.xml", 'r') as file:
    request = file.read()

request = request.replace('xsi:type="q1:TextNode"', 'xmlns:q1="http://www.everest.nl/aquima/studio/ManagementService/1.0" xsi:type="q1:TextNode"')

with open("xml/ApplyOperationsRequest.xml", 'w') as file:
    request = file.write(request)
