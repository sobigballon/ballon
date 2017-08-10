def find_last(search_string,target_string):
    last_p=-1
    while True:
        second_p=search_string.find(target_string,last_p+1)
        if second_p==-1:
            return last_p
        last_p=second_p
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




