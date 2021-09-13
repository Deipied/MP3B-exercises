def dont_give_me_five(start,end):
    new_list = list(range(start,end+1))
    for num in new_list:
        if str(num).find('5') != -1:
            new_list.remove(num)
    return new_list

print(dont_give_me_five(50,81))
