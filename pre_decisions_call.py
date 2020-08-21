from rounds_loop import*
round_array = [round_1,round_2]

def rounding_loop(getchr,getmi,getma,getrno):
    for i in range(getmi-1,getma):
        round_array[i](getrno,getchr)
        
