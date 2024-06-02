immutable_var = 13, 15, "iPhone",  "Pro"
print(immutable_var)
# immutable_var [2] = "Xiaomi"
# print(immutable_var)
# Кортеж нельзя изменить, добавить или удалить. Именно поэтому кортежи используют в качестве хранилища, т.к. данные в нем нельзя изменить и они находятся в безопасности.

mutable_list = [13, 15, "iPhone",  "Pro"]
# print(mutable_list)
mutable_list[0] = 14
# print(mutable_list)
mutable_list.append('Max')
# print(mutable_list)
mutable_list.extend(["1 tb", "very expensive"])
print(mutable_list)