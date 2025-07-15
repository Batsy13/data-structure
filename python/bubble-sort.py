def BubbleSort(nums: list) -> list:
    size = len(nums)
    
    for _ in nums:
        print(nums)
        for i in range(size - 1):
            if nums[i] > nums[i+1]:
                nums[i+1], nums[i] = nums[i], nums[i+1]

def BetterBubbleSort(nums: list) -> list:
    size = len(nums)
    
    for _ in nums:
        is_sorted = True
        print(nums)
        for i in range(size - 1):
            if nums[i] > nums[i+1]:
                is_sorted = False
                nums[i+1], nums[i] = nums[i], nums[i+1]
        if is_sorted:
            return

array1 = [2,7,6,4,3,5,1]
print(f"Original: {array1}")

BubbleSort(array1)
print(f"Bubble: {array1}")

print("\n")
print("\n")

array2 = [1,2,3,4,5,6,7]
print(f"Original: {array2}")

BetterBubbleSort(array2)
print(f"Bubble: {array2}")