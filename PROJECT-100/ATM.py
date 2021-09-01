class Atm:
    def ___init___ (self, cardnumber, pin):
     self.cardnumber = cardnumber
     self.pin = pin
     
     
     def balanceinwuiry(self):
         print("Your Balance Is: Rs.100 ")
         
     def cashwithdrawl(self, amount):
         new_amount = 100-amount
         print("You Withdrawed: " + str(amount) + "Your Remaing Balance is: " + str(new_amount))

    def main():
          name = input("Write Your Name Here:")
          print("Hello" + name)
          cardnumber=input("Insert Your Card Number:")
          pin=input("Insert Your Pin")
          new_user = Atm(cardnumber, pin)
          
          print("What You Want To Do With Your Account ")
          print("1.Balance Enquiry")
          print("2.Widthdraw Money")
          activity = int(input("Enter Activity Choice:"))
          
          if activity==1:
            new_user.balanceinquiry()
          elif activity==2:
            amount = int(input("Enter The Amount:")) 
            new_user.cashwidthrawl(amount)
         else:
             print("Enter A Valid Number")
             
if ___name___ == "___main___":
     main()
            
          