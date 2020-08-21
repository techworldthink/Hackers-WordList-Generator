from rounds_loop import*
round_array = [round_1,round_2,round_3,round_4,round_5,round_6,round_7,round_8,round_9,round_10,round_11,round_12,round_13,round_14,round_15,round_16]

def rounding_loop(getchr,getmi,getma,getrno):
    for i in range(getmi-1,getma):
        round_array[i](getrno,getchr)
        
