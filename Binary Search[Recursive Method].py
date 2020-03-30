a=[1,2,3,4,6,8,4,43,89,98,75]
target=8
def bsearch(a,target,low=0,high=len(a)):
    while low<high:
        mid=(low+high)//2
        if target==a[mid]:
            return True
        elif target<a[mid]:
            return bsearch(a,target,low=0,high=mid-1)
        else:
            return bsearch(a,target,low=mid+1,high=len(a))
    return False
bsearch(a,target)
