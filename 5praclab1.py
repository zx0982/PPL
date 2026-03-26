# Input from user
nums = tuple(map(int, input("Enter numbers: ").split()))

print("Tuple:", nums)

# a) Total number of items
print("Total items:", len(nums))

# b) Last item
print("Last item:", nums[-1])

# c) Reverse order
print("Reversed tuple:", nums[::-1])

# d) Check if 5 exists
if 5 in nums:
    print("Yes, 5 is present")
else:
    print("No, 5 is not present")

# e) Remove first and last elements
if len(nums) > 2:
    new_tuple = nums[1:-1]
    print("After removing first & last:", new_tuple)
else:
    print("Not enough elements to remove")
