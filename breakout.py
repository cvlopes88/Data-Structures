class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def add(self, value):
        self.next = Node(value)
        
    def find_middle(self):
        self.q = self.head.next
        self.p = self.head
        while self.q is not None:
          self.q = self.q.next.next
          self.p = self.p.next
        return self.p.value
      
      
      
class SLL:
      def __init__(self, head, tail):
        self.head = None
        self.tail = None
        self.count = 0


      def add_to_head(self, val):
            # if list is empty set head and tail to node
            # increment count
            if self.count is 0:
              self.head = self.tail = Node(val)
            else:
              node = node(val, self.head)
              self.head = node
              self.count += 1

        # if list is size 1 
            # set head to new node
            # set head.next to tail

lonked_list = SLL()

       
