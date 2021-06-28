for i in range(7):
    for j in range(7):
        if i==3:
            print("*", end='')
        elif i == 0:
            if j==0 or j==3 or j==4 or j==5 or j==6:
                print("*", end='')
            else:
                print(" ", end='')
        elif i == 1 or i == 2:
            if j==0 or j==3:
                print("*", end='')
            else:
                print(" ", end='')
        elif i == 4 or i == 5:
            if j==6 or j==3:
                print("*", end='')
            else:
                print(" ", end='')
        elif i == 6:
            if j==0 or j==1 or j==2 or j==3 or j==6:
                print("*", end='')
            else:
                print(" ", end='')
    print()
            