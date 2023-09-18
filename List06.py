import re


def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a=[]
    for i in list1:
        if i==1:
            a+=[True]
        else:
            a+=[0]
    return a
