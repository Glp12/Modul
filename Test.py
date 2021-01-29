import Plus  
k = int(input())
sum = 0.0
for i in range(k):
    a = (int(input()),int(input()))
    b = (0,1)
    c = Plus.add(a,b)
    sum = sum + c
print(1/sum)
