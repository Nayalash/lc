def containsDuplicate(nums):
    for num in nums:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
    return False


# Driver Code
print(containsDuplicate([1,2,10,3,4,7]))
print(containsDuplicate([1,2,1,3,4,7]))