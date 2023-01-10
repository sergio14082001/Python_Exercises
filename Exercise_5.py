def is_leap(year):
    leap = False
    
    # Write your logic here
    first = year%100
    second = year%4
    third = year%400
    if first != 0 or second != 0 or third != 0:
        leap = False
    else:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))