def get_even_list(l):
    l = l.list()
    n = []
    m = []
    for i in l:
        if i % 2 == 0:
            n.append(i)
        else:
            m.append(i)   
    return l
get_even_list([1, 4, 5, -1, 10, 2, 7])