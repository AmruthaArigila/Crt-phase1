class showroom:
     def __init__(self,cgst,sgst,insurance):
         self.cgst=cgst
         self.sgst=sgst
         self.insurance=insurance
     def company(self):
         while True:
              a=input("select the brand ")
              self.a=a
              if a=="honda":
                  print("welcome to the honda family")
                  break
              elif a=="mahindra":
                  print("welcome to the mahindra family")
                  break
              elif a=="tata":
                  print("welcome to the tata family")
                  break
              else:
                  print("enter valid company")
                  
                
     def model(self):
          while True:
               if self.a=="honda":
                 c=["city","civic"]
                 print(c)
                 c=input("enter the model ")
                 self.c=c
                 break
               elif self.a=="mahindra":
                   c=["thar","scorpio"]
                   print(c)
                   c=input("enter the model ")
                   self.c=c
                   break
               elif self.a=="tata":
                  c=["nexon","altroz"]
                  print(c)
                  c=input("enter the model ")
                  self.c=c
                  break
               else:
                  print("enter the valid model")
                  
     def price(self):
            while True:
                if(self.a=="honda" and self.c=="city"):
                    p=1500000
                    break
                elif(self.a=="honda" and self.c=="civic"):
                    p=2500000
                    break
                elif(self.a=="mahindra" and self.c=="thar"):
                    p=5500000
                    break
                elif(self.a=="mahindra" and self.c=="scorpio"):
                    p=4500000
                    break
                elif(self.a=="tata" and self.c=="nexon"):
                    p=2500000
                    break
                elif(self.a=="tata" and self.c=="altroz"):
                    p=4000000
                    break
                else:
                    print("enter valid")

            final_price=p+(self.cgst+self.sgst/100)+self.insurance
            print(final_price)

            
s=["honda","mahindra","tata"]
print(s)
obj=showroom(17,19,1500000)
obj.company()
obj.model()
obj.price()
            
                


              
      





     
