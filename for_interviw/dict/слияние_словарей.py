#1--------------------------------------------------------------------------

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

new_dic = {}
for i in (dict_a,dict_b,dict_c):
    new_dic.update(i)
print(new_dic)


#2--------------------------------------------------------------------------
result = {**dict_a, **dict_b, **dict_c}
print(result)
