from datetime import datetime

date_format = "%m-%d-%Y"
categories = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    while True:
        date_str = input(prompt)
        if allow_default and not date_str:
            return datetime.today().strftime(date_format)
        
        try:
            valid_date = datetime.strptime(date_str, date_format)
            return valid_date
        except ValueError:
            print(f"Invalid date format. Please enter the date in {date_format} format.")

def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError("Amount must be a positive non-zero value")
            return amount
        except ValueError as e:
            print(e)

def get_category():
    while True:
        category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
        if category in categories:
            return categories[category]
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense")

def get_description():
    return input("Enter a description (optional): ")

# Example usage
if __name__ == "__main__":
    date = get_date("Enter the date of the transaction (mm-dd-yyyy) or press Enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    print(f"Date: {date.strftime(date_format)}")
    print(f"Amount: {amount}")
    print(f"Category: {category}")
    print(f"Description: {description}")
