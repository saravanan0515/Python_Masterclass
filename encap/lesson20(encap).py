class order:
    def __init__(self, customer_name, items, total_amount, discount):
        self.customer_name = customer_name #public
        self.items = items #public
        self.__total_amount = total_amount # private
        self.__discount = discount #private

    def __calculate_final(self): #private helper method,its encapluse
        return self.__total_amount - self.__discount

    def _get_admin_view(self): # protected metod
        return{
          "customer":self.customer_name,
         "items":self.items,
         "total_amount": f"${self.__total_amount}",
         "discount applied":f"${self.__discount}",
          "final bill ":f"${self.__calculate_final()}"
        }

    def customer_view(self): # public method
      return{
        "customer": self.customer_name,
        "items":self.items,
        "final bill":f"${self.__calculate_final()}"
      }


class adimportal:
    def show_order(self, order):
        return order._get_admin_view() #allowed but protected
    
class customerapp:
    def show_order(self, order):
        return order.customer_view() # safe public method
    
order = order("sar",["pizza","pepsi"],600,150)
admin = adimportal()
customer = customerapp()

print("admin view:")
print(admin.show_order(order))
print("customer view:")
print(customer.show_order(order))


#output is 
#admin view:
#{'customer': 'sar', 'items': ['pizza', 'pepsi'], 'total_amount': '$600', 'discount applied': '$150', 'final bill ': '$450'}
#customer view:
#{'customer': 'sar', 'items': ['pizza', 'pepsi'], 'final bill': '$450'}