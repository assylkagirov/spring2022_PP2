def unique_list(list1):
    unique = []
    for i in list1:
        if i not in unique:
            unique.append(i)
            print(i, end = ' ')

lst = input().split(' ')
unique_list(lst)