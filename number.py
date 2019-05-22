array = [16, 2, 4, 2, 128, 64, 7, 1, 64, 32, 5, 8]
list_num_i = []
list_num_j =[]
number_list = []
for i in array:
    for j in array:
        if  i*j == 256 :
            list_num_i.append(i)
            list_num_j.append(j)

mylist_i = list(dict.fromkeys(list_num_i))
mylist_j = list(dict.fromkeys(list_num_j))

for i in range(len(mylist_i)):
    num={}
    for j in range(len(mylist_j)):
        if(i ==j ):
            num['num_1'] = mylist_i[i]
            num['num_2'] = mylist_j[j]
            num['num_3'] = mylist_i[i] + mylist_j[j]
    number_list.append(num)
for i in range(len(number_list)):

    for j in range(len(number_list)):
        a = number_list[i]
        c = a['num_2']
        b =  number_list[j]
        d = b['num_1'] 
        if( c == d ):
            del number_list[j] 
        else:
            pass
print(number_list)   








