import random as rand

#this func returns the password after adding a lower case character at random
def lowc(password):
    lower = "abcdefghijklmnopqrstuvwxyz"
    x = rand.randint(0,len(lower)-1)
    password += lower[x]
    return password

#this func returns the password after adding a upper case character at random
def upc(password):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = rand.randint(0,len(upper)-1)
    password += upper[x]
    return password

#this func returns the password after adding a special character at random
def spc(password):
    special = ["(","~","!", "@","#","$","%","^","&","*","_","-","+","=","`","|","(",")","{","}","[","]",":",";","<>",".","?","/",")",'"']
    x = rand.randint(0,len(special)-1)
    password += special[x]
    return password

def numc(password):
    num = "0123456789"
    x = rand.randint(0,len(num)-1)
    password += num[x]
    return password

def main():
    size = int(input("Enter size of password, recommended size 12 +, 8+ is the minimum \n"))
    password = ""
    left = ""
 
    for i in range(size):
       x = rand.randint(1,4)
       if x==1:
           password = lowc(password)
           left+=str(x)
           
       elif x==2:
            password = upc(password)
            left+=str(x)
            
       elif x==3:
            password = spc(password)
            left+=str(x)
            
       else:
            password = numc(password)
            left+=str(x)
    #
    m = "1234"
    


    for j in range (len(password)):
        print(left)
        for i in range(len(m)):
            temp = left.rfind((m[i]))
            
            if(temp == -1):
                re = rand.randint(0, len(password)-1)
                if int(m[i]) == 1 :
                    password = password.replace(password[re],lowc(""))
                    left = left.replace(left[re],"1",1) 
                     
                elif int(m[i]) == 2:
                    password  = password.replace(password[re],upc(""))
                    left = left.replace(left[re],"2",1) 
                elif int(m[i]) == 3:
                    password = password.replace(password[re],spc(""))
                    left = left.replace(left[re],"3",1) 
                elif int(m[i]) == 4:
                    password = password.replace(password[re],numc(""))
                    left = left.replace(left[re],"4",1) 
                j = 0
              
    print(password)  

if __name__ == "__main__":
    main()


    
    
