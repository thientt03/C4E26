def is_inside(list_a, list_b):
    if list_a[0] < list_b[0] or list_a[1] < list_b[1] or list_a[0] > list_b[0]+list_b[3] or list_a[1] > list_b[1]+list_b[2]:
        check = False
    else:
        check = True
    print(check)

is_inside([100,120], [140,60,100,200])
is_inside([200,120], [140,60,100,200])