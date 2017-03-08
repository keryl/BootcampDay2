def words(string):
    # first check splits the string and removes the whitespaces
    chars = string.split()
    # initializing an empty dictionary to hold the final input value
    my_dict = {}
# the check below identifies an integer in a string, if true the string is casted to an integer
    for char in chars:
       if char.isdigit() == True:
           char = int(char)
       my_dict[char] = my_dict.get(char, 0) + 1
    return my_dict
