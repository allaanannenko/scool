# string_set = {"Nicholas", "Michelle", "John", "Mercy"}
# print(string_set)

# f = {1, 2, 3, 4}
# f.discard(2)
# print(f)

#обьединение
# months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
# months_b = set(["July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# all_months = months_a.union(months_b)
# print(all_months)

#обьединение2
# months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
# months_b = set(["July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# print(months_a | months_b)

# x = {1, 2, 3}
# y = {4, 3, 6}
# #print(x & y)
# print(x - y)
# print(y - x)

# may_dict = {"Jan": 15, "Feb": 21, "March": 4, "Apr": 11, "May": 5, "June": 7}
# may_dict["Aug"] = 10
# print(may_dict)


a = {1, 2, 3, 4, 6}
b = frozenset([5, 8, 9, 2])
print(a | b)
print(a & b)







