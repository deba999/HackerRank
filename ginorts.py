You are given a string . 
 contains alphanumeric characters only. 
Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Sorting1234 -->  ginortS1324

#code

s=list(input())

s.sort(key=lambda x:( x.isdigit()and int(x)%2==0,x.isdigit(),x.isupper(),x) )

print(''.join(s))
