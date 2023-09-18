def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    a=list1[0]
    b=list1[1]
    c=list1[2]
    d=list1[3]
    e=list1[4]
    if a==b:
        if b==c:
            if d==e:
                return True
    if a!=b:
        if b!=c:
            if d!=e:
                return False
print(main([0,1,1,1,0]))