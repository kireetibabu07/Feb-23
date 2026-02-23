""" Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function """
a=int(input())
b=[]
for i in range(a):
    if i%2==1:
        b.append(i)
print(b)        