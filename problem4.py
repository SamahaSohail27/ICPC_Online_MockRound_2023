def find_last_seat(num_people):
    circular_list = list(range(1, num_people+1))
    idx = 0
    step = 0
    
    while len(circular_list) > 1:
        circular_list.pop(idx)
        #print(circular_list)
        step += 1
        idx = (idx + step) % len(circular_list)
        #idx -= 1 if idx >= 1 else 0
    
    return circular_list[0]


num_test_cases = int(input())
for _ in range(num_test_cases):
    num_people = int(input())
    last_seat = find_last_seat(num_people)
    print(last_seat)
