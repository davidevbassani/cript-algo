counter=open(r"C:\Users\david\Desktop\counter.txt")
def funconv(par1):
    sum = 0
    for i in range(len(par1)):
        sum += ord(par1[i])
    return sum

def collatz(n):
    n = int(n)
    lst = []
    while (n != 1):
        lst.append(n)
        if (n % 2 == 0):
            n = n // 2
        else:
            n = n * 3 + 1
    return len(lst)

par = input("Insert a string: ")
sum = funconv(par)
inte = collatz(sum)
for i in range(inte):
    a = inte%i
    if a==0 or i==range(inte):
        break
if a%2==0:
