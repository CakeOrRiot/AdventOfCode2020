with open('../input.txt','rt') as f:
    lst = set(map(int,f.readlines()))
    for x in lst:
        if 2020-x in lst:
            print(x*(2020-x))