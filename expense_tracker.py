import functools
working = True 

#Functions
expenses = []
def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n \nExecuting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished executing {func.__name__}.")
        return result
    return wrapper

@log_action
def add_expense(target_list,**kwargs):
    target_list.append(kwargs)
add_expense(expenses, price=100, category="Food", purcase="Groceries")


@log_action
def total(*amounts):
    return sum(amounts)

@log_action
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

#The code that the user sees
while working:
    print("\n \n  --- Your Expenses ---")
    print("1. Add Expense")
    print("2. Print Report")
    print("3. Get Category Summary")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    
    if choice not in ["1", "2", "3", "4"] and choice.lower() not in ["add expense", "print report", "get category summary", "exit"]:
        print("Invalid choice, please select a valid option.")
        continue
    
    
    ### First option - add expense
    if choice == "1"or choice.lower() == "add expense":
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
    if choice == "2" or choice.lower() == "print report":
        
        # Calculate total amount spent
        total_spent = []
        for i in expenses:
            total_spent.append(i["price"])
        total_amount = float(total(*total_spent))
        #end
    
    
    
        print("--- Expense Report ---")
        for i in expenses:
            print(f"Purcase: {i['purcase']}, Price: {i['price']}, Category: {i['category']}")
        print(f"Total Spent: {total_amount}")
        continue
    
    
    
    
    
    ##### 3rd option - category summary
    if choice == "3" or choice.lower() == "get category summary":
        category_summary = get_category_summary(expenses)
        print("--- Category Summary ---")
        for category, amount in category_summary.items():
            print(f"Spent on {category}: {amount}")
    
    
    
    #### 4th option - exit
    if choice == "4" or choice.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break





     