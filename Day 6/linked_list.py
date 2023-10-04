class Linked_List:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data
    
    def update_first(self, old_data, new_data):
        temp = self
        flag = False

        if temp.__data == old_data:
            temp.__data = new_data
            flag = True
        else:
            while temp.__next != None:
                if temp.__data == old_data:
                    temp.__data = new_data
                    flag = True
                    break
                temp = temp.__next

            if temp.__data == old_data:
                temp.__data = new_data
                flag = True
        if flag:
            print(f"First {old_data} updated to {new_data}")
        else:
            print(f"{old_data} not found")
    
    def update_all(self, old_data, new_data):
        temp = self
        flag = False

        if temp.__data == old_data:
            temp.__data = new_data
            flag = True
        else:
            while temp.__next != None:
                if temp.__data == old_data:
                    temp.__data = new_data
                    flag = True
                temp = temp.__next

            if temp.__data == old_data:
                temp.__data = new_data
                flag = True
        if flag:
            print(f"All {old_data} updated to {new_data}")
        else:
            print(f"{old_data} not found")
    
    def append(self, node):
        temp = self
        # print(node.__data)
        while temp.__next != None:
            temp = temp.__next
            # print(node.__data)    
        temp.__next = node
        print(f"{node.__data} appended")
    
    def get_next(self):
        return self.__next
    
    def print_list(self):
        temp = self
        while temp.__next != None:
            print(temp.__data, end=' --> ')
            temp = temp.__next
        print(temp.__data)
    
    def remove(self, data):
        # print(node.__data)
        temp = self
        prev = self

        flag = False

        if temp.__data == data:
            self = self.__next
            flag = True
        else:
            while temp.__next != None:
                if temp.__data == data:
                    prev.__next = temp.__next
                    flag = True
                    break
                prev = temp
                temp = temp.__next

            if temp.__data == data and flag==False:
                prev.__next = None
                flag = True
        if flag:
            print(f"{data} removed")
        else:
            print(f"{data} not found")

def main():
    l1 = Linked_List(1)
    # node = l1

    l1.append(Linked_List(2))
    l1.append(Linked_List(3))
    l1.append(Linked_List(4))
    l1.append(Linked_List(2))
    l1.append(Linked_List(5))
    l1.append(Linked_List(2))
    l1.append(Linked_List(2))
    l1.append(Linked_List(6))

    l1.print_list()

    l1.remove(3)

    l1.print_list()

    l1.update_first(2, 10)

    l1.print_list()

    l1.update_all(2, 1001)

    l1.print_list()

    
    # print(temp.get_data())
        
main()