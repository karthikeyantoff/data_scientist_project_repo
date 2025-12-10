# <!-- Create a folder named 'templates' and put this file inside it -->
# <!-- <!DOCTYPE html>
# <html>
#     <head>
#         <title>LOGIN FORM</title>
#         <style>
#             body { font-family: sans-serif; text-align: center; margin-top: 50px; }
#             form { display: inline-block; border: 1px solid #ccc; padding: 20px; border-radius: 10px; }
#         </style>
#     </head>
#     <body>
#         <h1>LOGIN HERE</h1>
#         <!-- The action must match the Python route '/login' -->
#         <form action="/login" method="post">
#             <label>Username:</label>
#             <input type="text" name="username" required><br><br>
            
#             <label>Password:</label>
#             <input type="password" name="password" required><br><br>
            
#             <input type="submit" value="Login Now">
#         </form>
#     </body>
# </html> -->
# total_amount=20000
# for i in range(len(total_amount)):
#     print(total_amount)
# user_witra_amout=int(input("enter the value"))
# while 500<total_amount:
#     if user_witra_amout<total_amount:
#         rem=total_amount-user_witra_amout
#         print(rem)
#     else:
#         print("enter the valied amount of amount")

# s="ABABA"
# seen={}
# for i in s:
#     seen[i]=seen.get(i,0)+1

# max_key = None
# max_val = 0

# for k, v in seen.items():
#     if v > max_val:
#         max_val = v
#         max_key = k
        
# print("Most repeated:", max_key, "Count:", max_val)
# def k(fruits):
#    if len(fruits)>2:
#         mapp={}
#         for i in fruits:
#             mapp[i]=mapp.get(i,0)+1
#         maxelement=max(mapp,key=mapp.get)
#         max_val=mapp[maxelement]
#         sec_max_ele=None
#         sec_max_val=-1
#         for k,v in mapp.items():
#             if k!=maxelement and v>sec_max_val:
#                 sec_max_val=v
#         return max_val+sec_max_val
# l=[3,3,3,1,2,1,1,2,3,3,4]
# ans=k(l)
# print(ans)

# l=[1,2,2,3,4,4,5]
# pointer1=0
# pointer2=1
# count=1
# count1=1
# for i in range(2,(len(l))):
#     # for j in range(i+1,len(l)):
#     if l[i]==l[pointer2]:
#         count1+=1
        
    

#     print(l[i])

#     # break

# def k(x):
#     if x<=1:
#         return 0
#     for i in range(2,x*x):
#         if x%i==0:
#             return False
#     return True
# print(k(10))
# c=a+b
# print(c)
# can="soda"
# 
can="soda"
print(type(can))
