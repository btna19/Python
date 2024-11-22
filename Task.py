#to find largest and smallest from a list

#Ascending order
#Swap any two elements in a list

# l1=[1,2,3,4,5,6]
# temp=l1[1]
# l1[1]=l1[2]
# l1[2]=temp
# print(l1)

#check Arm strong or not
# num=int(input('Enter a number:'))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp//=10

# if num == sum:
#     print("It is Armstrong number")
# else:
#     print("It is not a Armstrong number")
    
# Print * in H shape
for i in range(1,6):
    for j in range(0,5):
        if i==3:
            print('*',end=' ')
        else:
            if j==1 or j==3:
                print( '*',end='        ')
            print()

# Print * in I shape
# for i in range(1,6):
#     for j in range(0,5):

#         if i==1 or i==5:
#             print('*',end ='')
#         else:
#             if j == 1 :
#                 print('  *',end=' ')
#             print()

#Fibonacci Sequence
# num= int(input("Enter the no of terms:" ))
# a,b=0,1
# for i in range(1,num+1):
#     print(a)
#     c=a+b
#     a=b
#     b=c

