def find_min_between_a_and_b():
    N = int(input()) 
    arr = list(map(int, input().split()))
    A, B = map(int, input().split())

    min_value = float('inf')
    for i in range(len(arr)):
        if A <= arr[i] <= B:
            min_value = min(min_value, arr[i])

    if min_value == float('inf'):
        print(-1)
    else:
        print(min_value)

find_min_between_a_and_b()