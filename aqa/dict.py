# new_dic = {'opel':5000, "toyota" : 6000, 'bmw':9000}
# print(new_dic)
# print(new_dic['toyota'])
# new_dic['mazda']=4000
# print(new_dic)
# del new_dic['toyota']
# print(new_dic)

dic={'son':0, 'daugter':0}
person = {
    'first name' : 'Jack',
    'last name' : 'Brown',
    'age' : 45,
    'hobbies' : ['football', 'singing', 'photo'],
    'children' : [{'son':1, 'daugter':2},
                  {'son':3, 'daugter':4},
                  ]
}
# print(person['age'])
# print(person['hobbies'])
# hobbies = person['hobbies']
# print(len(hobbies))
# print(hobbies[2])
# print(person['hobbies'][2])
# print(person['children']['daugter'])
# person['children'].pop('son')
# print(person)
# person['price']=45
# person['hobbies'].append('basket')
person['children'].clear()

change = 0
while change <2:
    person['children'].append(dic)
    person['children'][change]['son']=1+change
    person['children'][change]['daugter']=2+change
    change +=1
print(person)



