import sys

repository = sys.argv[1]

with open("xml/ApplyOperationsRequestTemplate.xml", 'r') as template:
    data = template.read()
    data = data.replace("$REPOSITORY", repository)
    with open("xml/ApplyOperationsRequest.xml", 'w') as file:
        file.write(data)
