def round_1(ind_rounds,get_chars):
    for i in range(ind_rounds):
        print(get_chars[i])
        
def round_2(ind_rounds,get_chars):
    for a in range(ind_rounds):
        for b in range(ind_rounds):
            print(str(get_chars[a])+str(get_chars[b]))

