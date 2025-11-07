# def is_pallidrome(s):
#     s=s.lower().replace(" ","")
#     return s==s[::-1]

# print(is_pallidrome("madam"))
# print(is_pallidrome("hello"))

# def second(n):
#     unique_nums=list(set(n))
#     unique_nums.sort()
#     return unique_nums[-2]

# print(second([1,2,3,4,5,5,4,3,2,1]))

# def freq(s):
#     freq={}
#     for char in s:
#         freq[char]=freq.get(char,0)+1
#     return freq
# print(freq("hello world"))

# dict1={"a":1,"b":2}
# dict2={"b":3,"c":4}
# dict3={**dict1,**dict2}
# #merged dictionaries
# print(dict3)


# Two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find common elements
common = list(set(list1) & set(list2))

print("Common elements:", common)

