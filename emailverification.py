email=input("Enter your email : ")
j=k=l=0

if len(email)>6:

    if email[0].isalpha():
        
        if "@" in email and email.count("@")==1:
            
            if email[-3]=="." or email[-4]==".":
                
                for i in email:
                   
                    if i==i.isspace():
                        j=1
                    
                    elif i.isalpha():
                        if i==i.isupper():
                            k=1
                    
                    elif i.isdigit():
                         continue
                    
                    elif i=="_" or i=="@" or i==".":
                        continue
                    else:
                        l=1
                
                if j==1 or k==1 or l==1:
                    print("You have entered Invalid Email")
                    
                else:
                    print("Your email has verified")   
                    
            else:
                print("Invalid Email")
        
        else:
            print("check your @, there should be atmost 1")
        
    else:
        print("Firt letter should be alphabet")
        
else:
    print("Your Email length is too small")
