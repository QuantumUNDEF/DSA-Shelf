
def create_dict(arr):

    dict = {}

    # Your code here
    # Hint: use loop to iterate through arr
    # and assign key value to the dict
    for name, marks in arr:
        dict[name] = marks

    return dict