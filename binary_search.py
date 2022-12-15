def find(search_list, value):
    len_list = len(search_list)
    midpoint = int(len_list / 2)
    beg = 0
    end = len_list-1
    
    while (len_list >= 0):
        if (search_list[beg] > value) or (search_list[end] < value):
            raise ValueError("value not in array")

        if (search_list[midpoint] > value):
            end = midpoint
        elif (search_list[midpoint] < value):
            beg = midpoint + 1
        else:
            return midpoint

        len_list = end - beg
        midpoint = beg + int(len_list / 2)
        
        
        
   
