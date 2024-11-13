x = [1,2]
n=5
for i in range(2,n):
    x.append(x[i-2] + x[i-1])
    print(x[-1])









