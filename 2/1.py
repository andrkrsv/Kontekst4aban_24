def back_biggest_count(n_list, useless):
    if useless != len(n_list):
        return
    if useless == len(n_list):
        counter = {}
        for i in n_list:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        most_frequent_number = max(counter, key=counter.get)
        return most_frequent_number
    else:
        return

useless = int(input()) 
n_list = list(map(int, input().split()))
print(back_biggest_count(n_list,useless))
