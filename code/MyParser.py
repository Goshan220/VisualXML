import lxml.etree as etree
import re

DEFINE_TAB = 1

def start(text):
    tree = etree.parse(text)
    root = tree.getroot()
    # print(root.tag) console log: DEBUG
    file = open("~temp.txt", 'w')
    file.write("0: " + str(root.tag)+ ": "+ str(root.attrib) + str(root.text))
    recurs(root, DEFINE_TAB, file)
    file.close()
    return 0


def recurs(root, tab, file):
    for child in root:
        indent = " " * tab * 4
        if (child.attrib != {}) | (child.text != None):
            # print(child.tag + " attrib -> " + str(child.attrib)) #console log: DEBUG
            if child.text == None:
                s = str(tab)+": " + indent + str(child.tag) + ": " + str(child.attrib) + "\n"
            else:
                if (re.search(r'[\!-\~]', str(child.text))):
                    s = str(tab)+": " + indent + str(child.tag) + ": " + str(child.attrib) + "TEXT: " + str(child.text) + "\n"
                else:
                    s = str(tab) + ": " + indent + str(child.tag) + ": " + str(child.attrib) + "\n"
            s = re.sub(r'\n\s{2}', '', s)
            file.write(s)
        tab += DEFINE_TAB
        root = child
        recurs(root, tab, file)
        tab -= DEFINE_TAB
    return 0
