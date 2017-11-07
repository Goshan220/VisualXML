import re

class Tree(object):
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def show(self):
        print(self.name)
        if self.children is not None:
            for i in self.children:
                i.show()
            else:
                print("DEBUG| last")

    def select(self, name):
        if self.name == name:
            return self
        else:
            if self.children is not None:
                for i in self.children:
                    print(i.name)
                    i.select(name)

# <[^\/].*[^\/]> - только открываюшие теги
# <[^\/].*\/> - только самозакрывающиеся теги
# <\/.*> - только закрывающие теги

def text_analyze(text):
    openTags = re.findall(r'(<[^\/].*[^\/]>)|(<[^\/].*\/>)|(<\/.*>)', text)
    # closerTags = re.findall(r'<\/.*>', text)
    # oneTags = re.findall(r'<[^\/].*\/>', text)
    print(openTags)
    # print(closerTags)
    # print(oneTags)
    return 0
# t = Tree('*',
#          [Tree('1'), Tree('2'), Tree('+',
#             [Tree('3'), Tree('4')])])
#
# r = Tree("ROOT", None)
# print(r)
# print(r.children)
# r.add_child(Tree("rereq", None))
# r.add_child( Tree("speed", None))
# print(r.children)
# r.children[0].add_child(Tree("Fucl", None))
# r.show()
# t.add_child(Tree("DDD", None))
# t.add_child(Tree("sqrt", None))
# t.show()
# print('test')
