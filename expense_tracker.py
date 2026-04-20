import functools
working = True 

#Functions

expenses = []
def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n \nExecuting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"\nFinished executing {func.__name__}.")
        return result
    return wrapper

@log_action
def add_expense(target_list,**kwargs):
    target_list.append(kwargs)



def total(*amounts):
    return sum(amounts)


def get_category_summary(expenses):
    category_summary = {}
    for i in expenses:
        category = i["category"]
        price = i["price"]
        if category in category_summary:
            category_summary[category] += price
        else:
            category_summary[category] = price
    return category_summary



def get_total_spent(expenses):
    total_spent = []
    for i in expenses:
        total_spent.append(i["price"])
    return total(*total_spent)



def most_expensive_purchase(expenses):
    total_spent = []
    for i in expenses:
        total_spent.append(i["price"])
    for i in expenses:
        if i["price"] == max(total_spent):
            return i["purcase"], i["price"]



def least_expensive_purchase(expenses):
    total_spent = []
    for i in expenses:
        total_spent.append(i["price"])
    for i in expenses:
        if i["price"] == min(total_spent):
            return i["purcase"], i["price"]


@log_action
def report(expenses):
    print("\n \n \n══════════ EXPENSE REPORT ══════════")
    print("#  Name           Category     Amount")
    print("────────────────────────────────────────")
    for i in expenses:
        print(f"i,  {i['purcase']},           {i['category']},     {i['price']}")
    print("\n📂 BY CATEGORY:")
    for category, amount in get_category_summary(expenses).items():
        print(f"{category} -> {amount}")
    print(f"\n🏆 Biggest     : {most_expensive_purchase(expenses)}")
    print(f"-cheapest    : {least_expensive_purchase(expenses)}")
    print(f"💰 Grand Total: {get_total_spent(expenses)}")


#The code that the user sees
while working:
    print("\n \n  --- Your Expenses Manager ---")
    print("1. Add Expense")
    print("2. Print Report")
    print("3. Print Report And Exit the program")
    print("4. Get Category Summary")
    print("5. Exit")
    
    choice = input("Choose an option: ").lower()
    
    
    if choice not in ["1", "2", "3", "4", "5"] and choice.lower() not in ["add expense", "print report", "get category summary", "exit"]:
        print("Invalid choice, please select a valid option.")
        continue
    
    
    match choice:
    ### First option - add expense
        case "1" | "add expense":
            purcase = input("Enter purcase's name: ")
            price = input("Enter price: ")
            
            
            ##### Price validation
            
            
            if not price.isdigit():
                while not price.isdigit():
                    print("Invalid price, please enter a numeric price.")
                    price = input(f"What is the price of {purcase}?: ")
                    if price.isdigit():
                        break
                print("Invalid price, please enter a numeric price.")
            price = float(price)
            
            #### End of price validation
            category = input("Enter category: ")
            add_expense(expenses, price=price, category=category, purcase=purcase)
            continue
        

        
        
        ### second option - print report
        case "2" | "print report":
        
        
            report(expenses)
            continue
        
        
        ##### 3rd option 
        case "3" | "print report and exit the program":
            
        
        
            report(expenses)
            break
        
        
        ##### 4th option - category summary
        case "4" | "get category summary":
            category_summary = get_category_summary(expenses)
            print("--- Category Summary ---")
            for category, amount in category_summary.items():
                print(f"Spent on {category}: {amount}")
            continue
        
        
        #### 5th option - exit
        case "5" | "exit":
            print("Exiting the program. Goodbye!")
            break
