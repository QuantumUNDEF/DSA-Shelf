# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    tag = True
    for i in arr:
        if str(i) != str(i)[::-1]:
            tag = False
            break
    return tag