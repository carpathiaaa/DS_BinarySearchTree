class Node:
    def __init__(self, value, left=None, right=None, present=True):
        self.value = value
        self.left = left
        self.right = right
        self.present = present

    
    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    
class Tree:
    def __init__ (self):
        self.root = None


    def insertValue(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            node = Node(value)
            while current is not None:
                if value > current.value:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = node
                        return
                elif value < current.value:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = node
                        return
                else:
                    current.present = True
                    return


    def findValue(self, value):
        current = self.root
        while current is not None:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return current.present

        return False

    def removeValue(self, value):
        current = self.root
        while current is not None:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                if current.present:
                    current.present = False
                    return True
                else:
                    return False

        return False

    def nodeText(self, node):
        if node.present == False:
            return f"{node.value}D "
        else:
            return f"{node.value} "

    def recursivePreOrder(self, node):
        if node is None:
            return ""
        else:
            left = self.recursivePreOrder(node.left)
            right = self.recursivePreOrder(node.right)
            return f"{self.nodeText(node)}{left}{right}"

    def recursiveInOrder(self, node):
        if node is None:
            return ""
        else:
            left = self.recursiveInOrder(node.left)
            right = self.recursiveInOrder(node.right)

            return f"{left}{self.nodeText(node)}{right}"

    def recursivePostOrder(self, node):
        if node is None:
            return ""
        else:
            left = self.recursivePostOrder(node.left)
            right = self.recursivePostOrder(node.right)
            return f"{left}{right}{self.nodeText(node)}"

    
    def preOrder(self):
        return self.recursivePreOrder(self.root)

    def inOrder(self):
        return self.recursiveInOrder(self.root)

    def postOrder(self):
        return self.recursivePostOrder(self.root)

    def findLarger(self, value):
        current = self.root
        successor = None
        while current is not None:
            if value > current.value:
                current = current.right
            elif value < current.value:
                successor = current
                current = current.left
            elif current.value == value and current.present is True:
                successor = current.value
                return successor
            else:
                current = current.right

        if successor:
            return successor.value
        else:
            return -1



    def removeLarger(self, value):
        pass


