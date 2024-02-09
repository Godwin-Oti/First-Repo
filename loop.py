a=[1,2,3,4,5,6,7,8,9,10]
x=1
while x in a:
  if x%2==0:
    print(x)
  x+=1


a= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for x in a:
  if x%2==0:
    print(x)

berlin = [15, 13, 16, 18, 19, 10, 12 ]
munich = [7, 13, 15, 20, 19, 18, 10, 16]
c=[]
for x in berlin:
  if x in munich:
    if x not in c:
      c.append(x)
print(c)

berlin=[15,13,16,18,19,15,10] ##first method
c=[]
for x in berlin:
  if x not in c:
    c.append(x)
print(c)

berlin =[15,13,16,18,19,15,10]  ##second method
mydict=dict.fromkeys(berlin)
mylist=list(mydict)
print(mylist)

a=("Hello")
print(len(a))

a=input("get_length: ")
length=0
for _ in a:
  length+=1
print("Length of String is ", length)

a=int(input("Enter number "))  ##check for even or odd number
if a%2==0:
  print("This number is even",a)
else:
  print("This number is odd", a)


num=int(input("Enter Number: "))
def even_check(num):
  if num ==0:
    print(num ,"is neither even nor odd")
  elif num %2==0:
    print(num,"is even number")
  else:
    print(num,"is not an even number")
even_check(num)


def myfunction(x):
  return list(dict.fromkeys(x)) 
mylist=myfunction(["Oti","Godwin","Oti","Chibuzor","Onyemaobi","Chimebuka","Chimebuka","Oti","Chibuzor","Godwin","Oti","Oti","Godwin","Oti"])
mylist.sort()
print(mylist)

def myfunction():
    customer_list = [
                    {"name": "Bob", "age": 1999},
                    {"name": "Jack", "age": 1995},
                    {"name": "Lisa", "age": 2005},
                    {"name": "Maria", "age": 2010},
                    {"name": "Ben", "age": 2007},
                    {"name": "Emma", "age": 2006},
                    {"name": "Oscar", "age": 1994},
                    {"name": "Amy", "age": 1996},
                    {"name": "Paul", "age": 1979},
                    {"name": "Etta", "age": 2008}
                ]
    for x in customer_list:
          print(x["name"], "was born in", x["age"])
myfunction()


num=list(input("Enter List: "))

def function(num):
    
    mylist=[1,3,4,5,6,7,8,9]
    for x in mylist:
        if num == x:
            print("Yes!")
        else:
            print("No!")
function()
            




  




