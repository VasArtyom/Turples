immutable_var = (2, "dva", True)
print(immutable_var)
#Tuples - это такие списки, элементы которого не могут быть изменены в силу изначальной задумки самого Кортежа.
#Элемент кортежа прямым пониманием нельзя изменить, но пожно представить элемент кортежа в виде списка, в котором уже
#и можно проводить операции.
mutable_list = [1, 2, 3, 4, "порядок"]
mutable_list[0] = "один"
print(immutable_var)
print(mutable_list)