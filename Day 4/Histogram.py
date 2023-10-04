def hist(dict, design='===', show_value=True, align = True):
    max_space = max(list(dict.values())) * len(design)
    for key,val in dict.items():
        space = val * len(design)
        print(f'{key} |', end=' ')
        print(f'{design*val}', end='')
        if show_value==True:
            if align == True:
                print(' ' * (max_space-space), end='')
            print(f' {val}', end='')
        print()
    

hist({2:1, 6:5, 5:4}, design='$$$', show_value=True)

    