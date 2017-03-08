def find_max_min(list):
    # check to ensure elements in list are equal
    if all(x == list[0] for x in list) == True:
        new_list = []
        new_list.append(len(list))
        # returns length of list
        return new_list
    else:
        maxim = max(list)  # find maximum value
        minim = min(list)  # find minimum value
        # adding maximum and minimum  values to a list and returning the list
        maxmin = []
        maxmin.append(minim)
        maxmin.append(maxim)
        return maxmin