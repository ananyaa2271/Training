class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_next(self):
        return self.__next
    
    def set_next(self, node):
        self.__next = node
    
    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data

class Linked_List:
    def __init__(self):
        self.__node = None
    
    def update_first(self, old_data, new_data):
        temp = self.__node
        flag = False

        if temp.get_data() == old_data:
            temp.set_data(new_data)
            flag = True
        else:
            while temp.get_next() != None:
                if temp.get_data() == old_data:
                    temp.set_data(new_data)
                    flag = True
                    break
                temp = temp.get_next()

            if temp.get_data() == old_data:
                temp.set_data(new_data)
                flag = True
        if flag:
            print(f"First {old_data} updated to {new_data}")
        else:
            print(f"{old_data} not found")
    
    def update_all(self, old_data, new_data):
        temp = self.__node
        flag = False

        if temp.get_data() == old_data:
            temp.set_data(new_data)
            flag = True
        else:
            while temp.get_next() != None:
                if temp.get_data() == old_data:
                    temp.set_data(new_data)
                    flag = True
                temp = temp.get_next()

            if temp.get_data() == old_data:
                temp.set_data(new_data)
                flag = True
        if flag:
            print(f"All {old_data} updated to {new_data}")
        else:
            print(f"{old_data} not found")
    
    def append(self, data):
        temp = self.__node
        node = Node(data)
        # print(node.__data)
        if temp == None:
            self.__node = node
        else:
            while temp.get_next() != None:
                temp = temp.get_next()
                # print(node.__data)    
            temp.set_next(node)
        print(f"{node.get_data()} appended")
    
    def print_list(self):
        temp = self.__node
        while temp.get_next() != None:
            print(temp.get_data(), end=' --> ')
            temp = temp.get_next()
        print(temp.get_data())
    
    def remove(self, data):
        # print(node.__data)
        temp = self.__node
        prev = self.__node

        flag = False

        if temp.get_data() == data:
            self.__node = temp.get_next()
            flag = True
        else:
            while temp.get_next() != None:
                if temp.get_data() == data:
                    prev.set_next(temp.get_next())
                    flag = True
                    break
                prev = temp
                temp = temp.get_next()

            if temp.get_data() == data and flag==False:
                prev.set_next(None)
                flag = True
        if flag:
            print(f"{data} removed")
        else:
            print(f"{data} not found")

def main():

    l1 = Linked_List()
    # node = l1

    l1.append(2)
    l1.append(3)
    l1.append(4)
    l1.append(5)
    l1.append(6)
    l1.append(7)
    l1.append(8)
    l1.append(9)
    l1.append("8454656")

    l1.print_list()

    l1.remove(3)

    l1.print_list()

    l1.update_first(2, 10)

    l1.print_list()

    l1.update_all(2, 1001)

    l1.print_list()

    
    # print(temp.get_data())
        
main()