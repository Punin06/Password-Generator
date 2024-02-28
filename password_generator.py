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

#this func returns the password after adding a number character at random
def numc(password):
    num = "0123456789"
    x = rand.randint(0,len(num)-1)
    password += num[x]
    return password

def main():
    #Creating size to store the size of the password, password to store password, left to keep track of the missing criteria characters.
    size = int(input("Enter size of password, recommended size 12 +, 8+ is the minimum \n"))
    password = ""
    left = ""

    #input validation, to ensure the minimum strong password length is selected
    while (size < 8):
        size = int(input("The size of the password was less than the recommended! Please select a recommended size! Recommended size 12 +, 8+ is the minimum \n"))

    #A loop to go to random func to return a random character such as upper, lower, special and number, and keeping track of the func visit with left.
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
    #stores the responding choices selections
    m = "1234"
    

#this goes through the password to check the missing criteria, and then fills it.
    for j in range (len(password)):
        for i in range(len(m)):
            #temp stores the missing criteria
            temp = left.rfind((m[i]))

            #if there's a miss it's, stored as -1. We go through the missing criteria fill them and replace them, to ensure that criteria is not visited again unless it's missing.
            if(temp == -1):
                #creating re to go to a random point in the password and change it 
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
                #setting j to zero, to go through the password again, to ensure no criteria is missing.
                j = 0
    #prints the password     
    print(password)  

if __name__ == "__main__":
    main()


    
    
