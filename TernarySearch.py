
# concept of ternary search
pos=-1
list=list(map(int,input().split(",")))
n=len(list)
l=0
r=n-1

def ternarySearch(list,l,r,key):
    #for i in range(len(list)):
    while r>=l:
        mid1=l+(r-l)//3
        mid2=r+(r-l)//3

        if list[mid1]==key:
            globals()['pos']=mid1
            return mid1
        if list[mid2]==key:
            globals()['pos']=mid2
            return mid2
        if key<list[mid1]:
            #return ternarySearch(list,l,mid1-1,key)
            r=mid1-1
        elif key>list[mid2]:
            #return  ternarySearch(list,mid2+1,r,key)
            l=mid2+1
        else:
            #return  ternarySearch(list,mid1+1,mid2-1,key)
            l=mid1+1
            r=mid2-1
    else:
        return False


key=int(input("Enter the element to found : "))

if ternarySearch(list,l,r,key):
    print("Element found : ",pos)
else:
    print("Element not found")