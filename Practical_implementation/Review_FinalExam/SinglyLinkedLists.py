# Xây dựng ngăn xếp (stack) sử dụng cấu trúc danh sách liên kết đơn (singly linked list)

class SinglyLinkedStack():
    # Cấu trúc Node dùng cho danh sách liên kết đơn
    class _Node():
        def __init__(self, element = None):
            self._element=element
            self._next=None
    #-----------------
    def __init__(self, head=None):
        self._head=head
        self._size=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):                          # Trả về giá trị của phần tử trên cùng mà không xóa nó
        if self.is_empty():
            return None
        return self._head._element

    def push(self, element):
        newNode=self._Node(element)         # Tạo một node mới
        newNode._next=self._head            # Thêm vào đầu danh sách
        self._head=newNode
        self._size+=1

    def pop(self):
        if self.is_empty():
            return None
        term=self._head._element
        self._head=self._head._next
        self._size-=1
        return term

    def __str__(self):
        result=""
        run=self._head
        for i in range(self._size):
            result+=' '+str(run._element)
            run=run._next
        return result

######################
#danhSach = SinglyLinkedStack()
#danhSach.push(5)
#danhSach.push(7)
#print(len(danhSach))
#danhSach.push(4)
#print(danhSach.top())
#danhSach.pop()
#danhSach.pop()
#danhSach.pop()
#danhSach.pop()
#print(danhSach.is_empty())
#print(danhSach)

# Xây dựng hàng đợi (queue) sử dụng cấu trúc danh sách liên kết đơn (singly linked list)

class SinglyLinkedQueue():
    # Cấu trúc Node dùng cho danh sách liên kết đơn
    class _Node():
        def __init__(self, element = None):
            self._element=element
            self._next=None
    #-----------------
    def __init__(self, head=None, tail=None):
        self._head=head
        self._tail=tail
        self._size=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def first(self):                          # Trả về giá trị của phần tử trên cùng mà không xóa nó
        if self.is_empty():
            return None
        return self._head._element

    def last(self):
        if self.is_empty():
            return None
        return self._tail._element

    def enqueue(self, element):
        newNode=self._Node(element)          # Tạo một node mới
        newNode._next=None                   # Vì newNode là phần tử cuối cùng
        if self.is_empty():
            self._head=newNode
        else:
            self._tail._next=newNode
        self._tail=newNode
        self._size+=1

    def dequeue(self):
        if self.is_empty():
            return None
        term=self._head._element
        self._head=self._head._next
        self._size-=1
        if self.is_empty():                   
            self._tail=None
        return term

    def __str__(self):
        result=""
        run=self._head
        for i in range(self._size):
            result+=' '+str(run._element)
            run=run._next
        return result

danhSach = SinglyLinkedQueue()
danhSach.enqueue(5)
danhSach.enqueue(7)
print(len(danhSach))
danhSach.enqueue(4)
print('Queue:',danhSach)
print('First:',danhSach.first())
print('Last:',danhSach.last())
danhSach.dequeue()

print('Queue:',danhSach)
print('First:',danhSach.first())
print('Last:',danhSach.last())
danhSach.dequeue()
danhSach.dequeue()
danhSach.dequeue()
print('Is it empty?',danhSach.is_empty())
print(danhSach)