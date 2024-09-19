def is_lucky_number(N):
    
    N_str = str(N)
  
    count_4 = N_str.count('4')
    count_7 = N_str.count('7')
    
   
    total_lucky_digits = count_4 + count_7
    

    if total_lucky_digits == 4 or total_lucky_digits == 7:
        return "YES"
    else:
        return "NO"
n = input().strip()
print(is_lucky_number(n))
