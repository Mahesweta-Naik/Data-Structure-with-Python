#QUEUE
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("empty")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
def check_number(queue1):
    size=queue1.get_max_size()
    sol_queue=Queue(size)
    while size>0:
        element=queue1.dequeue()
        if all(element%i==0 for i in range(1,11)):
            sol_queue.enqueue(element)
        size-=1
    return sol_queue
queue1=Queue(5)
queue1.enqueue(13983)
queue1.enqueue(10080)
queue1.enqueue(7113)
queue1.enqueue(2520)
queue1.enqueue(2500)
queue1.display()
 
