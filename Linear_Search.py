
# concept of linear search

pos=-1

def linear_search(list,key):
    for i in range(0,len(list)):
        if list[i]==key:
            globals()['pos']=i
            return True
    else:
        return False

list=list(map(int,input().split(",")))
key=int(input("Enter element to search : "))

if linear_search(list,key):
    print("Element found at position : ",pos)
else:
    print("Element not found")
