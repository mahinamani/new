
#products list
product_ls=["book","ball","car"]

def main_menu():
    print("\n---MAIN MENU---\n")
    print("[0] Exit App...")
    print("[1] products menu")
    try : 
        choice=int(input("Choose an option : "))
        if choice==0:
            exit()
        elif choice==1:
            product_menu()
        else :
            raise Exception()
    except :
        print('index does not exist!')
        return main_menu()
    



def product_menu():
    print("\n---Product MENU---\n")
    print("[0] RETURN to main menu")
    print("[1] PRINT products list")
    print("[2] CREATE new product")
    print("[3] UPDATE existing product")
    print("[4] DELETE product")

    try : 
        choice=int(input("Choose an option : "))
        if choice==0:
            main_menu()
            
        elif choice==1:
            print_products()
            
        elif choice==2:
            print("CREATE new product")
            product_name=str(input("Enter the product name : "))
            product_ls.append(product_name)
            print_products()
            
        elif choice==3:
            print("UPDATE existing product")
            print_products()
            product_index=int(input("product index : "))
            new_name=str(input("new product name : "))
            product_ls[product_index]=new_name
            print_products()          
                
        elif choice==4:
            print("DELETE product")
            print_products()
            product_index=int(input("product index : "))
            product_ls.pop(product_index)
            print_products()
    except :
        print('index does not exist!')
            
    finally:
        main_menu()
        



def print_products():
    counter=0
    print("\n---Product List---\n")
    for item in product_ls:
        print("[{0}] - {1}\n".format(counter,item))
        counter+=1
    
main_menu()



#products list
product_ls=["book","ball","car"]
#orders
order_ls=[
    
    {
      "customer_name": "John",
     "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
     "customer_phone": "0789887334",
     "status": "preparing"
     }
]

def main_menu():
    print("\n---MAIN MENU---\n")
    print("[0] Exit App...")
    print("[1] products menu")
    print("[2] orders menu")
    choice=int(input("Choose an option : "))
    if choice==0:
        exit()
    elif choice==1:
        product_menu()
    elif choice==2:
        order_menu()

def product_menu():
    print("\n---Product MENU---\n")
    print("[0] RETURN to main menu")
    print("[1] PRINT products list")
    print("[2] CREATE new product")
    print("[3] UPDATE existing product")
    print("[4] DELETE product")
    
    choice=int(input("Choose an option : "))
    
    if choice==0:
        main_menu()
        
        
    elif choice==1:
        print_products()
        
        
    elif choice==2:
        print("CREATE new product")
        product_name=str(input("Enter the product name : "))
        product_ls.append(product_name)
        print_products()
        
        
    elif choice==3:
        print("UPDATE existing product")
        print_products()
        product_index=int(input("product index : "))
        if 0 <= product_index < len(product_ls):
            new_name=str(input("new product name : "))
            product_ls[product_index]=new_name
            print_products()
        else:
            print("Index doesn't exist!")
            
            
    elif choice==4:
        print("DELETE product")
        print_products()
        product_index=int(input("product index : "))
        try:
            product_ls.pop(product_index)
            print_products()
        except:
            print("Index doesn't exist!")
            


    main_menu()
        
def print_products():
    counter=0
    print("\n---Product List---\n")
    for item in product_ls:
        print("[{0}] - {1}\n".format(counter,item))
        counter+=1

def print_orders():
    print("\n---orders List---\n")
    
    counter=0
    
    for order in order_ls:
        print("\n --index=> {0} \n".format(counter))
        print("customer_name : "+order["customer_name"])
        print("customer_address : "+order["customer_address"])
        print("customer_phone : "+order["customer_phone"])
        print("status : "+order["status"])
        
        counter+=1
        
        print("----------------------")
        
def order_menu():
    print("\n---orders MENU---\n")
    print("[0] RETURN to main menu")
    print("[1] PRINT orders dictionary")
    print("[2] APPEND order to orders list")
    print("[3] UPDATE existing order status")
    print("[4] UPDATE existing order")
    print("[5] DELETE order")
    choice=int(input("Choose an option : "))
    
    if choice==0:
        main_menu()
        
    if choice==1:
        print_orders()
        
    if choice==2:
        print("APPEND order to orders list")
        
        name=str(input("user input for customer name : "))
        address=str(input("user input for customer address : "))
        phone=str(input("user input for customer phone number : "))
        
        temp={}
        temp["customer_name"]=name
        temp["customer_address"]=address
        temp["customer_phone"]=phone
        temp["status"]="preparing"
        
        order_ls.append(temp)
    if choice==3:
        print("UPDATE existing order status")
        
        print_orders()
        
        order_index=int(input("order index : "))
        
        
        status_ls=["preparing","Rejected","Delivered"]
        counter=0
        for i in status_ls:
            print("[{0}] {1}".format(counter,i))
            counter+=1
            
            
        status_index=int(input("status index : "))
        
        status=status_ls[status_index]
        
        order_ls[order_index]["status"]=status
        
        
        
    if choice==4:
        print("UPDATE existing order")
        
        print_orders()
        
        index=int(input("order index : "))
        order=order_ls[index]
        
        for key,value in order.items():
            new_value=str(input("user input for {0} update : ".format(key)))
            if new_value=="":
                continue
            else:
                order_ls[index][key]=new_value
                
    if choice==5:
        print("DELETE order")
        
        print_orders()
        
        index=int(input("order index : "))
        
        try:
            order_ls.pop(index)
            print_orders()
        except:
            print("Index doesn't exist!")
            
    main_menu()
    
main_menu()



import os

class ProductsAndCouriers:  
    def __init__(self, type, ls):
        self.file = type + ".txt"
        self.type = type
        self.list = self.read(self.file) if os.path.exists(self.file) else ls
        self.write()

    @staticmethod
    def read(f):
        ls = []
        with open(f, 'r') as file:
            for i in file.readlines():
                ls.append(i[:-1])
        return ls

    def write(self):
        with open(self.file, 'w') as file:
            for i in self.list:
                file.write(i + "\n")

#show list
    def print(self):
        counter = 0
        print("\n---{} List---\n".format(self.type))
        for item in self.list:
            print("[{0}] - {1}\n".format(counter, item))
            counter += 1

    def create(self):
        print("CREATE new {}".format(self.type))
        name = str(input("Enter the {} name : ".format(self.type)))
        self.list.append(name)
        self.write()
        self.print()

#update list
    def update(self):
        print("UPDATE existing {}".format(self.type))
        self.print()
        index = int(input("{} index : ".format(self.type)))
        if 0 <= index < len(self.list):
            new_name = str(input("new {} name : ".format(self.type)))
            self.list[index] = new_name
            self.write()
            self.print()
        else:
            print("Index doesn't exist!")
 
 #delete from list
    def delete(self):
        print("DELETE {}".format(self.type.upper()))
        self.print()
        index = int(input("{} index : ".format(self.type)))
        try:
            self.list.pop(index)
            self.write()
            self.print()
        except:
            print("Index doesn't exist!")

#show menu
    def show_menu(self):
        print("\n---{} MENU---\n".format(self.type.upper()))
        print("[0] RETURN to main menu")
        print("[1] PRINT {} list".format(self.type))
        print("[2] CREATE new {}".format(self.type))
        print("[3] UPDATE existing {}".format(self.type))
        print("[4] DELETE {}".format(self.type))

        choice = int(input("Choose an option : "))

        if choice == 1:
            self.print()

        elif choice == 2:
            self.create()

        elif choice == 3:
            self.update()

        elif choice == 4:
            self.delete()

        main_menu()


class Products(ProductsAndCouriers):
    def __init__(self, ls):
        super().__init__(type="product", ls=ls)


class Couriers(ProductsAndCouriers):
    file = "courier.txt"

    def __init__(self, ls):
        super().__init__(type="courier", ls=ls)


class Orders:#کلاس orders
    def __init__(self, ls):
        self.list = ls

    @staticmethod
    def get_courier(skip=False): 
        print('choose courier : ')
        c_list = Couriers.read(Couriers.file)

        counter = 0
        for i in c_list:
            print("[{0}] {1}".format(counter, i))
            counter += 1

        inp = input("courier index : ")

        if inp.isdigit() and int(inp) < len(c_list):
            courier_index = int(inp)
        elif skip:
            courier_index = ""
        else:
            print('wrong input try again : ')
            return Orders.get_courier(skip)

        return courier_index

    @staticmethod
    def get_status(skip=False):
        print('choose status : ')
        status_ls = ["preparing", "Rejected", "Delivered"]
        counter = 0
        for i in status_ls:
            print("[{0}] {1}".format(counter, i))
            counter += 1

        inp = input("status index : ")

        if inp.isdigit() and int(inp) < len(status_ls):
            status_index = int(inp)
        elif skip:
            return ""
        else:
            print('wrong input try again : ')
            return Orders.get_status(skip)

        status = status_ls[status_index]
        return status

    def print(self):
        print("\n---orders List---\n")

        counter = 0

        for order in self.list:
            print("\n --index=> {0} \n".format(counter))
            print("customer_name : " + order["customer_name"])
            print("customer_address : " + order["customer_address"])
            print("customer_phone : " + order["customer_phone"])
            print("courier : " + str(order["courier"]))
            print("status : " + order["status"])

            counter += 1

            print("----------------------")

    def create(self):
        print("APPEND order to orders list")

        name = str(input("user input for customer name : "))
        address = str(input("user input for customer address : "))
        phone = str(input("user input for customer phone number : "))

        courier_index = self.get_courier()

        temp = {}
        temp["customer_name"] = name
        temp["customer_address"] = address
        temp["customer_phone"] = phone
        temp["courier"] = courier_index
        temp["status"] = "preparing"

        self.list.append(temp)

    def update_status(self):
        print("UPDATE existing order status")
        self.print()
        order_index = int(input("order index : "))
        self.list[order_index]["status"] = self.get_status()

    def update(self):
        print("UPDATE existing order")

        self.print()

        index = int(input("order index : "))
        order = self.list[index]

        for key, value in order.items():
            if key == "courier":
                new_value = self.get_courier(True)
            elif key == "status":
                new_value = self.get_status(True)
            else:
                new_value = str(input("user input for {0} update : ".format(key)))
            if new_value == "":
                continue
            else:
                self.list[index][key] = new_value

    def delete(self):
        print("DELETE order")

        self.print()

        index = int(input("order index : "))

        try:
            self.list.pop(index)
            self.print()
        except:
            print("Index doesn't exist!")

    def show_menu(self):
        print("\n---orders MENU---\n")
        print("[0] RETURN to main menu")
        print("[1] PRINT orders dictionary")
        print("[2] APPEND order to orders list")
        print("[3] UPDATE existing order status")
        print("[4] UPDATE existing order")
        print("[5] DELETE order")
        choice = int(input("Choose an option : "))

        if choice == 0:
            main_menu()

        if choice == 1:
            self.print()

        if choice == 2:
            self.create()
        if choice == 3:
            self.update_status()

        if choice == 4:
            self.update()
        if choice == 5:
            self.delete()

        main_menu()


product_ls = ["ball", "bag", "boot"]
courier_ls = ['jack', 'john', 'hank']
order_ls = [

    {
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887334",
        "courier": 2,
        "status": "preparing"
    }
]

products = Products(product_ls)
couriers = Couriers(courier_ls)
orders = Orders(order_ls)


def main_menu():
    print("\n---MAIN MENU---\n")
    print("[0] Exit App...")
    print("[1] products menu")
    print("[2] couriers menu")
    print("[3] orders menu")

    choice = int(input("Choose an option : "))
    if choice == 0:
        products.write()
        couriers.write()
        exit()

    elif choice == 1:
        products.show_menu()
    elif choice == 2:
        couriers.show_menu()
    elif choice == 3:
        orders.show_menu()


main_menu()
