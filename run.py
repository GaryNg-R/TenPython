
def getmostvisited2(n, sprints):
    arr = [0]*(n)
    for i in range(len(sprints)-1):
        start = min(sprints[i], sprints[i+1])
        end = max(sprints[i], sprints[i+1])
        arr[start] += 1
        arr[end ] -= 1
        print("start = " , start , "end  = " , end)
        print("here what is arr = " , arr)
    ans = -1
    s = 0
    maxi = -1
    for i in range(1, n):
        print("arr[i] = ",arr[i],"  s = " , s)
        arr[i] += s
        s = arr[i]
        print("after arr[i] = ",arr[i],"  s = " , s)
        if s > maxi:
            print("s> maxi , maxi = " , maxi, "so maxi = s = " , s) 
            maxi = s
            ans = i

    return ans


def getmostvisited(n, sprints):
    arr = [0]*(n+2)
    for i in range(len(sprints)-1):
        start = min(sprints[i], sprints[i+1])
        end = max(sprints[i], sprints[i+1])
        arr[start] += 1
        arr[end + 1] -= 1
    ans = -1
    s = 0
    maxi = -1
    for i in range(1, n+1):
        arr[i] += s
        s = arr[i]
        if s > maxi:
            maxi = s
            ans = i

    return ans

a = [1,5,3,4,2,6]
a = [2,4,1,2]
print(getmostvisited(10,a ))