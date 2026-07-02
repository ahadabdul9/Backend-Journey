# 	4. Find maximum of three numbers

a = int(input("Enter a value :"))
b = int(input("Enter b value :"))
c = int(input("Enter c value :"))

max = a
if(b > max):
    max = b
elif(c > max):
    max = c

print(max, " is the maximum of the given")