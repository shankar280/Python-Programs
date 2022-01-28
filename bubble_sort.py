def sort(num):
    for i in range (0, len(num)-1):
        print("value of i", i)

        for j in range (0, len(num)-1-i):
            print("value of j", j)
            if num[j] > num[j+1]:
                temp = num[j]
                num[j]=num[j+1]
                num[j+1]=temp
num=[1,4,5,3,7,2]
sort(num)
print(num)


