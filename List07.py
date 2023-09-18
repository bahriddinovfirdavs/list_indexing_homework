def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a=[]
    for i in list1:
        if i==0:
            a+=[False]
        else:
            a+=[1]
    return a
