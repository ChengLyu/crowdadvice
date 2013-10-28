def move_to_last(lst, str):
    """Move a matching string to the end of list
    
    Only one occurrence of the string is expected
    """
    
    try:
        lst.remove(str)
    except:
        pass
    
    lst.append(str)