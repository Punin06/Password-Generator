import random as rand

def lowc(password):
    lower = "abcdefghijklmnopqrstuvwxyz"
    x = rand.randint(0,len(lower)-1)
    password += lower[x]
    return password

def upc(password):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = rand.randint(0,len(upper)-1)
    password += upper[x]
    return password

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
    print (password)
    m = "1234"
    


    for j in range (len(password)):
        print(left)
        for i in range(len(m)):
        
        #print(m[i])
            temp = left.rfind((m[i]))
            #print(temp)
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
            #It's working, debbug and polish it
            
        #pass
        #have one of each letter, number, special character
        #make it random selection
        #standard password have an upper and lower case letter
# create the flags and check which method it has to go, then replace, consider the other conditions might become false after replacing, must stay within set size
#maybe better to do it in the main for, make sure each of the criteria is at least met once
#I could let it go through each criteria and then scramble the word
#use a boolean flag, and store the selection, to keep track the missing character
#best to do it after, and then replace and scramble       
    
if __name__ == "__main__":
    main()


    
    
