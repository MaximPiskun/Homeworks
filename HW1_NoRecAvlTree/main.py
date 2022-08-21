import operator


class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class bin_tree():

    def __init__(self):
        self.root = None
        self.size = 0

    def help_insert(self, key, node):
        mid = node
        helpp = ""
        while mid != None:
            if key < mid.key:
                mid = mid.left
                helpp = helpp + "left."
            else:
                mid = mid.right
                helpp = helpp + "right."

        return self.help_help_delete(node, helpp, Node(key))

    def insert(self, key):
        self.root = self.help_insert(key, self.root)
        self.size += 1

    def help_find(self, key, node):
        nod = node
        while (nod != None) and (nod.key != key):
            print(nod.key)
            if key > nod.key:
                nod = nod.right
            else:
                nod = nod.left
        if nod == None:
            return False
        if nod.key == key:
            return True

    def find(self, key):
        return self.help_find(key, self.root)

    def search_right(self, node):
        nod = node
        while nod.left != None:
            nod = nod.left
        return nod

    def unlink_right(self, node):
        while node.left != None:
            node = node.left
        return node.right

    def help_help_delete(self, node, helpp, num):  # замена по координате helpp на число num
        helpp = helpp[:-4]
        if helpp != "":
            if helpp[-1] == "i":
                helpp = helpp[:-3]
                if helpp != "":
                    setattr(operator.attrgetter(helpp)(node), "right", num)
                else:
                    setattr(node, "right", num)
            else:
                helpp = helpp[:-2]
                if helpp != "":
                    setattr(operator.attrgetter(helpp)(node), "left", num)
                else:
                    setattr(node, "left", num)
        else:
            node = num
        return node

    def help_delete(self, key, node):
        nod = node
        helpp = ""
        while (nod != None) and (nod.key != key):
            if key > nod.key:
                nod = nod.right
                helpp += "right."
            else:
                nod = nod.left
                helpp += "left."
        if nod.key == key:
            if nod.right == None:
                return nod.left
            else:
                node_new = self.search_right(nod.right)
                nod.right = self.unlink_right(nod.right)
                node = self.help_help_delete(node, helpp, node_new)
                node = self.help_help_delete(node, helpp, nod.right)
                node = self.help_help_delete(node, helpp, nod.left)
                return node_new
        return node

    def delete(self, key):
        self.root = self.help_delete(key, self.root)
        self.size -= 1


A = bin_tree()
B = [5, 4, 8, 2, 3, 6, 9, 100, -10]
for i in B:
    A.insert(i)
print(A.find(-10))
A.delete(-10)
print(A.find(-10))


