"""" This code shows how to implement linked list with explanation for every step """
"""toturial source: https://www.youtube.com/watch?v=qp8u-frRAnU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=4"""
class Node:
    """ creating a node; the node is used to store data and a pointer in many data structures """
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next #the pointer which will point to the next node

class Linked_list:
    def __init__(self):
        self.head=None #initializing the head of the list

    def insert_at_beginning(self, data):
        """ inserting element at the beginning of the list"""

        node = Node(data, self.head) #passing the data to the node
        self.head = node #passing the node itself to the attribute "head" to make it point to the next element.

    def insert_at_end(self,data):
        """inserting elements at the last index, first checking if the list is empty, else iterating on the list ot reach the last element"""
        if self.head is None:
            self.head=Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)

    def insert_values(self,data_list):
        """inserting list of values"""
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        """insetting elements by index"""
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_beginning(data)
            return
    def print(self):
        """iterating over the list and printing each element with a separator to differentiate between each element"""
        if self.head is None:
            print('list is empty')
            return
        itr = self.head
        llstr = ""

        while itr:
         llstr +=str(itr.data) + '--->'
         itr=itr.next

        print(llstr)


    def get_length(self):
        """Getting the length of list"""
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def remove_element(self,index):
        """Removing elements by index"""
        if index<0 or index>= self.get_length():
            raise Exception("Invalid index")

        if index ==0:
            self.head=self.head.next
            return

        count=0
        itr=self.head
        while itr:
            if count== index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
if __name__=='__main__':
    ll=Linked_list()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(55)
    ll.insert_at_end(50)
    ll.print()