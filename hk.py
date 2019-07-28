import sys, string, math
# program for dividing array to make average equal

def findSubarrays(arr, n):
    # Find array sum
    sum = 0;
    for i in range(0, n):
        sum += arr[i];

    found = False
    lsum = 0
    for i in range(0, n - 1):
        lsum += arr[i]
        rsum = sum - lsum

        if lsum * (n - i - 1) == rsum * (i + 1):
            #print("From (%d %d) to (%d %d)" % (0, i, i + 1, n - 1))
            #print(arr[:i+1],arr[i+1:])
            return True

    # If no subarrays found
    if found == False:
        return False

# Driver code
n = int(input())
L = [ int(x) for x in input().split()]
if findSubarrays(L, n) : print('yes')
else :                   print('no')
