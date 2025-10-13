def print_score(score_list):
    sum = 0
    for score in score_list:
        sum += score
    avg = sum / len(score_list)
    print(avg)

print_score([1, 2, 3])