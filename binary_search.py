def find(search_list, value):
    len_list = len(search_list)
    midpoint = int(len_list / 2)
    
    while (len_list > 0):
        if (search_list[0] > value) or (search_list[len_list - 1] < value):
            raise ValueError("value not in array")

        if (search_list[midpoint] > value):
            len_list = midpoint
            midpoint = int(len_list / 2)
        elif (search_list[midpoint] < value):
            len_list = len_list - midpoint
            midpoint = int(len_list / 2)
        else:
            return midpoint
        
        
        
   
