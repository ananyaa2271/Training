col = 1
for i in range(1, 30+1):
    
    if col==1:
        print("\n|", end='')
    if col==7:
        # print("\n|")
        col=0
    print(f'\t{i}\t|', end='')

    col+=1
    