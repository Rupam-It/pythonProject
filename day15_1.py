# this  is a coffee machine project
coffee_machine_ingridience={
    "water":[1000,'ml'],
    "milk":[1000,'ml'],
    "coffee":[200,'g'],
    "money":[2.5,'$']
}


# this is peice chart of money
price_chart={
    "espresso":1.5,
    "latte": 2.5,
    "cappuccino":3.0
}

# for each coffee required ingredient   espresso/latte/cappuccino
# required_materials={
#                    water      coffee       milk    price
#     "espresso":    50ml       18g             x     $1.5
#      "latte"  :    200ml      24g           150     $2.5
#   "cappuccino":   250ml       24g          100      $3.0 
# }


# first on coffee machine
def status(stat:str):
    if stat=='on':
        print("welcome...")
        return True
    elif stat=='off':
        print("Thank You")
        return False
    else:
        False

# here we can see reamiling ingreience in machine
def report(d:dict):
    print(f"Water: {d['water'][0]}{d['water'][1]}")
    print(f"Milk: {d['milk'][0]}{d['milk'][1]}")
    print(f"Coffee: {d['coffee'][0]}{d['coffee'][1]}")
    print(f"Money: {d['money'][1]}{d['money'][0]}")

# report(coffee_machine_ingridience)


# here we cheak that there are enough ingreadence for (espresso/latte/cappuccino)
def enough_ingridence(d:dict, coffee_type:str):
    if coffee_type=="espresso":
        if d['water'][0]>=50 and d['coffee'][0]>=18:
            return True
    elif coffee_type=='latte':
        if  d['water'][0]>=200 and d['coffee'][0]>=24 and d['milk'][0]>=150:
            return True
    elif coffee_type=='cappuccino':
        if d['water'][0]>=250 and d['coffee'][0]>=24 and d['milk'][0]>=100:
            return True
    return False

# here we calculate the user money
def calculate_money():
    print("Please insert coin..")
    Quater=int(input("How many Quaters?: "))
    Dine=int(input("How many Dine?: "))
    Nickel=int(input("How many Nickel?: "))
    Penny=int(input("How many Penny?: "))
    value= Quater *0.25 + Dine*.1 + Nickel*.05+ Penny*.01
    return value



# cheaking user money is sufficient or not
def sufficient_money(p_chart:dict, money:float,coffee_type):
    if p_chart[coffee_type]>money:
        print("Not enough money....")
        return False
    
    elif p_chart[coffee_type]<money:
        change=money-p_chart[coffee_type]
        print(f"Here is your change: {change}")
        return True

    return True


#update ingredient(,needed_ingredient:dict)
def update_ingredient(d:dict,coffee_type:str):
    if coffee=='espresso':
        d['water'][0]-=50
        d['milk'][0]-=0
        d['coffee'][0]-=18
        d['money'][0]+=1.5


    elif coffee=='latte':
        d['water'][0]-=200
        d['milk'][0]-=150
        d['coffee'][0]-=24
        d['money'][0]+=2.5


    elif coffee=='latte':
        d['water'][0]-=250
        d['milk'][0]-=100
        d['coffee'][0]-=24
        d['money'][0]+=3.5

    return d



while True:
    on_status=input("on/off ? ").lower()
    if on_status=='on':
        coffee=input("What Would you like ? (espresso/latte/cappuccino): ")
        if coffee== 'report':
            report(coffee_machine_ingridience)

        if coffee=='espresso' or coffee=='latte' or coffee=='cappuccino':
            if enough_ingridence(coffee_machine_ingridience,coffee):
                money=calculate_money()
                if sufficient_money(price_chart,money,coffee):
                    coffee_machine_ingridience=update_ingredient(coffee_machine_ingridience,coffee)
                    print(f"Enjoy your {coffee}..... ")
                    continue
                else:
                    print("Sorry you have not sufficent money..")
                    continue
            else:
                print("Sorry not enough ingredience is here ....")
                continue
                   
        
    elif on_status=='off':
        break