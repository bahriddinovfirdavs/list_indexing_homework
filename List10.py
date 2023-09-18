def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    a=list_num
    if a[0]>a[-1]:
        return a[0]
    if a[0]<a[-1]:
        return a[-1]
    if a[0]==a[-1]:
        return a[0] or a[-1]

