#Tutorials
#https://www.youtube.com/watch?v=lFq5mYUWEBk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=10
#https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert_element(self,data):

        if data==self.data:
            return
        if data < self.data:
            if self.left:
                self.left.insert_element(data)
            else:
                self.left=BinaryTree(data)
        else:
            if self.right:
                self.right.insert_element(data)
            else:
                self.right=BinaryTree(data)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def inorder_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorder_traversel()
        return elements

    def  insert_values(self,values_list):
        root=BinaryTree(values_list[0])

        for i in range(1,len(values_list)):
            root.insert_element(values_list[i])
        return root
if __name__=='__main__':

    BT=BinaryTree(10)
    BT.insert_element(12)
    BT.insert_element(9)
    BT.PrintTree()
    values_list=[1,10,20,5,12,18]
    BT.insert_values(values_list).PrintTree()
