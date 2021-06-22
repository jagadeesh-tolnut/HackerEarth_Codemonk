testcase  = int(input())
for _ in range(testcase):
    size,no_of_rotaion = map(int,input().split())
    array = list(map(int,input().split()))
    mod_of_rotaion = no_of_rotaion % size
    print(*(array[size-mod_of_rotaion:]+array[:size-mod_of_rotaion]))