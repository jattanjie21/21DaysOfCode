#Day 1/100 

#Creating a list class for data structures
#Creating a new data type and ensure that this data provides the
#list,queue and stack like behaviour and hide the list inside this data type..

class List():

    def __init__(self):
        self._list = [] #Initial length

    def add_item(self,item):
        self._list.append(item)

    def remove_item(self,item): #Support the len protocol
        self._list.remove(item)

    def __len__(self):
        return len(self._list)

    def is_empty(self):
        return self.__len__() == 0

class Queue(List):
#Adding more Queue like objects

    def pop_item(self,element):
        self._list.pop[0]

    def __str__(self):
        return 'Queue List = ' + str(self._list)

    def __str__(self):
        return 'Queue: ' + str(self._list)

class Stack(Queue):
    pass

    