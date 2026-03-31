#The Virtual Vending Machine

#Stage 1: Create a console app where a user selects a product (Coke, Pepsi, Water) and inserts "coins." Calculate change.
#Stage 2: Add a "Stock Manager." If an item is out of stock, the user must be alerted before inserting money.
#Constraint: Use Enums for products and handle invalid inputs (e.g., negative money) gracefully.

#Goal: Assess basic OOP, control flow, and ability to follow a specification.


class venderMachine:
   def __init__(self):
      self.products = {
         "Coke": 700,
         "Pepsi": 500,
         "Water": 300
      }
      self.money_inserted = 0
      if amount > 0:
         self.money_inserted += amount
         return f"You have inserted ${amount/100:.2f}. Total: ${self.money_inserted/100:.2f}"
      else:
         return "Invalid amount. Please insert a positive amount of money."

   def show_amount(self,product):
      if product in self.products:
        return f"The price of {product} is ${self.products[product]/100:.2f}"
      else:
        return "Invalid product selected."
      
      def check_amount(self,product,amount):
        if product in self.products:
            price = self.products[product]
            if amount >= price:
                change = amount - price
                return f"Purchase successful. Your change is ${change/100:.2f}"
            else:
                return f"Insufficient funds. Please insert at least ${price/100:.2f}"
        
      def give_change(self,amount):
        if amount > 0:
            return f"Returning change: ${amount/100:.2f}"
        else:
            return "No change to return."
      

class stockManger:
  
 def __init__(self):
    self.coke_stock=10
    self.pepsi_stock=10
    self.water_stock=10
      

def is_avilable(self,product):
    if product=="Coke":
      return self.coke_stock>0
    elif product=="Pepsi":
      return self.pepsi_stock>0
    elif product=="Water":
      return self.water_stock>0
    else:
      return "Item is out of stock"
    
class User:
  
  def __init__(self):
    self.money_inserted=0
       
  
  def select_product(self,product):
    if product in ["Coke","Pepsi","Water"]:
      return f"You have selected {product}."
    else:
      return "Invalid product selected. Please select a valid product."

  
  def __init__(self):

    self.money_inserted=0  

    
      
  def select_product(self,product):
       if product in ["Coke","Pepsi","Water"]:
         return f"You have selected {product}."
       else: 
              return "invalid product selected"
       


user1=User()
stock =stockManger()
vender=venderMachine()



user1.select_product("water")
user1.money_inserted=1000
stock.is_available("water")
vender.insert_money(1000)
vender.check_amount("water",1000)
vender.give_change(700)



