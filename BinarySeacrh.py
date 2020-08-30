
# concept of binary search

pos=-1

def binary_search(list,key):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if list[mid]==key:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<key:
                low=mid+1
            else:
                high=mid-1
    return False

list=list(map(int,input().split(",")))
key=int(input("Enter element to search : "))

if binary_search(list,key):
    print("Element found at position :",pos)
else:
    print("Element not found")

