def lotto_kr():
    import random
    
    nums = 6
    arr = list(range(1, 46))
    
    for i in range(nums):
        random.shuffle(arr)
        arr_selected = arr[:6]
        arr_selected.sort()
    print(arr_selected)