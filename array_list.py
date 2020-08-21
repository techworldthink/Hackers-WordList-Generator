from pre_decisions_call import* 
n = [1,2,3,4,5,6,7,8,9,0]                                                 
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']         
A = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']      
s = [" ","!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]",'^','_','{','|','}','~','`',"\\"]
#10
#26
#26
#32

def word_array(characters_get,mini,maxi):
    if characters_get == 1:
        round_no = 10
        send_chr = n
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 2:
        round_no = 26
        send_chr = A
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 4:
        round_no = 26
        send_chr = a
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 8:
        round_no = 32
        send_chr = s
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 3:
        round_no = 36
        send_chr = n + A
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 5: 
        round_no = 36
        send_chr = n + a
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 9: 
        round_no = 42
        send_chr = n + s
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 6: 
        round_no = 52
        send_chr = a + A
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 10: 
        round_no = 58
        send_chr = s + A
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 12: 
        round_no = 52
        send_chr = s + a
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 14: 
        round_no = 84
        send_chr = a + A + s
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 15: 
        round_no = 94
        send_chr = n+a+A+s
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 11: 
        round_no = 68
        send_chr = n + A +s
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 13: 
        round_no = 68
        send_chr = n+a+s
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 7: 
        round_no = 62
        send_chr = n + A + a
        rounding_loop(send_chr,mini,maxi,round_no)
    elif characters_get == 0: 
        round_no = 0
        send_chr = n 
        rounding_loop(send_chr,mini,maxi,round_no)
    else :
        print('exception')


        
