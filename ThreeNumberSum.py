def test(array,targetsum):
    array.sort()
    triplets=[]
    for i in range(len(array)-2):
        left=i+1
        right=len(array)-1
        while left < right:
            cs=array[i]+array[left]+array[right]
            if cs==targetsum:
                triplets.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif cs < targetsum:
                left+=1
            elif cs > targetsum:
                right-=1
    return triplets
