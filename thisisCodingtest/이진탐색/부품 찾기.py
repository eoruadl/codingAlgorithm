n = int(input())
haveList = list(map(int, input().split()))
m = int(input())
requestList = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for i in requestList:
    result = binary_search(haveList, i, 0, len(haveList) - 1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
