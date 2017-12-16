import lxml.etree as etree
import re


class Pars:
    def __init__(self):
        self.tab = 0
        self.tagDict = {}

    def start(self, text):
        tree = etree.parse(text)
        root = tree.getroot()
        file = open("~temp.txt", 'w')
        file.write("0: " + str(root.tag) + ": " + str(root.attrib) + str(root.text)) #корневой тег
        self.recurs(root, self.tab, file)
        file.close()
        # for tag in self.tagDict.keys():
        #     print(tag + " :==: " + str(self.tagDict.get(tag)))
        return 0

    def recurs(self, root, tab, file):
        tab += 1
        for child in root:
            indent = " " * tab * 4
            if (child.attrib != {}) | (child.text != None):
                if child.attrib != {}:
                    if str(child.tag) in self.tagDict:
                        temp = str(self.tagDict.get(str(child.tag)))
                        temp = temp + " ::: " + str(child.attrib)
                        self.tagDict.update({str(child.tag): temp})
                    else:
                        self.tagDict.update({str(child.tag): child.attrib})

                # print(child.tag + " attrib -> " + str(child.attrib)) #console log: DEBUG
                if child.text == None:
                    s = str(tab) + ": " + indent + str(child.tag) + ": " + str(child.attrib) + "\n"
                else:
                    if re.search(r'[\!-\~]', str(child.text)):
                        s = str(tab) + ": " + indent + str(child.tag) + ": " + str(child.attrib) \
                            + ": " + str(child.text) + "\n"
                    else:
                        s = str(tab) + ": " + indent + str(child.tag) + ": " + str(child.attrib) + "\n"
                s = re.sub(r'\n\s{2}', '', s)
                file.write(s)
            root = child
            self.recurs(root, tab, file)
        return 0

    def getTagDict(self):
        return self.tagDict
