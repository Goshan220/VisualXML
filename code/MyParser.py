import xml.etree.ElementTree as etree

def start(text):
    tree = etree.parse(text)
    root = tree.getroot()
    file = open("~temp.txt", 'w')
    recurs(root, 0, file)
    return 0

def recurs(root, tab, file):
    tab += 4
    for child in root:
        indent = " " * tab
        print(child)
        print(child.text) #console log: DEBUG
        s = indent + str(child.tag) + ": " + str(child.text) + "\n"
        root = child
        file.write(s)
        recurs(root, tab, file)
    return 0