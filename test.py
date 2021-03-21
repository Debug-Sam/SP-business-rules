lst = [1, 0, 4, 1]

def my_sort(lst):

    k = max(lst)

    lst2 = []
    for i in range(0, k+1):
            lst2.append((i,0))
    print(lst2)
    freqs = dict()
    for i in lst:
        freqs[i] = lst.count(i)

    lst3 = []
    for i in lst2:
        key = i[0]
        if freqs.get(key) != None:
            lst3.append((key, freqs.get(key)))
    print(lst3)
    final_lst = []
    for key, value in lst3:
        while value != 0:
            final_lst.append(key)
            value += -1

    return final_lst

print(my_sort(lst))

