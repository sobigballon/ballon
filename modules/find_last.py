def find_last(search_string,target_string):
    position=search_string.find(target_string)
    while True:
        second_position=search_string.find(target_string,position+1)
        if second_position>0:
            position=second_position
        else:
            return position
    return position


print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0




