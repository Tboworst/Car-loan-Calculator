def calculate_monthly_payment(principal, annual_interest_rate, loan_period):
    """
    Calculates the monthly payment for the loan.
    Formula: monthly payment [p * r *(1+ r)^n]/[(1+r)^n -1]
    where: 
    P = principal amount (car price - down payment)
    r = monthly interest rate (annual rate / 12)
    n = number of payments (loan term in months)
    """
    monthly_interest_rate = annual_interest_rate / 12 / 100  # Convert APR to monthly decimal
    numerator = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_period
    denominator = (1 + monthly_interest_rate) ** loan_period - 1
    monthly_payment = numerator / denominator
    return monthly_payment


def budget_planner(monthly_income):
    """
    Suggests a comfortable car budget based on the 20/4/10 rule:
    - 20% down payment
    - 4-year loan term
    - 10% of monthly income for payments
    learned about this on tiktok btw LOL
    """
    suggested_down_payment = 0.20
    suggested_loan_term = 48 #im making this 4 years
    suggested_monthly_payment = monthly_income * 0.10

    max_car_price = (suggested_monthly_payment * suggested_loan_term) / (1 - suggested_down_payment)
    return max_car_price


def affordability(monthly_payment, monthly_income):
    """
    Determines if the monthly payment is comfortable or uncomfortable.
    If monthly_payment is less than 15% of monthly_income,it's comfortable.
    if not it will return as uncomfortable.
    """
    affordability_threshold = 0.15
    if monthly_payment < monthly_income * affordability_threshold:
        return "comfortable"
    else:
        return "uncomfortable"


def calc_required_salary(monthly_payment):
    """
    Calculates the required salary to afford the loan.
    Formula: salary = (monthly_payment * 12) / 0.15
    searched this up on google, it is a common formula used by many financial advisors.
    """
    affordability_threshold = 0.15
    required_monthly_income = monthly_payment / affordability_threshold
    required_annual_salary = required_monthly_income * 12
    return required_annual_salary


def debt_to_income_ratio(monthly_debt, monthly_income):
    """
    Calculates the debt-to-income ratio.
    formula:(Total Monthly Debt / Monthly Income) * 100
    """
    return (monthly_debt / monthly_income) * 100


def calculate_interest_rate(credit_score):
    """
    Calculates the annual interest rate based on the user's credit score.
    Credit score ranges and corresponding interest rates:
    - 300-579: Poor (15%)
    - 580-669: Fair (12%)
    - 670-739: Good (8%)
    - 740-799: Very Good (6%)
    - 800-850: Excellent (4%)
    """
    if 300 <= credit_score <= 579:
        return 15.0  # Poor credit
    elif 580 <= credit_score <= 669:
        return 12.0  # Fair credit
    elif 670 <= credit_score <= 739:
        return 8.0   # Good credit
    elif 740 <= credit_score <= 799:
        return 6.0   # Very good credit
    elif 800 <= credit_score <= 850:
        return 4.0   # Excellent credit
    else:
        raise ValueError("Invalid credit score. Credit scores range from 300 to 850.")


def get_positive_float(prompt):
    """
    Prompts the user for a positive float value.
    """
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_credit_score():
    """
    ask the user for a valid credit score (300-850).
    """
    while True:
        try:
            credit_score = int(input("Enter your credit score (300-850): "))
            if 300 <= credit_score <= 850:
                return credit_score
            else:
                print("Credit score must be between 300 and 850.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def generate_amortization_schedule(principal, annual_interest_rate, loan_term):
    """
    Generates an amortization schedule for the loan.
    """
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, loan_term)
    balance = principal

    print("\n--- Amortization Schedule ---")
    print(f"{'Payment':<10}{'Principal':<15}{'Interest':<15}{'Remaining Balance':<20}")
    for payment in range(1, loan_term + 1):
        interest = balance * monthly_interest_rate
        principal_payment = monthly_payment - interest
        balance -= principal_payment
        print(f"{payment:<10}${principal_payment:<14.2f}${interest:<14.2f}${balance:<19.2f}")


def save_to_file(filename, content):
    """
    Saves the provided content to a text file.
    """
    with open(filename, "w") as file:
        file.write(content)
    print(f"Results saved to {filename}.")


def display_car_listings(cars):
    """
    Displays car listings in a user-friendly format.
    """
    print("\n--- Available Cars ---")
    for index, car in enumerate(cars, start=1):
        print(f"{index}. {car['make']} {car['model']} ({car['year']})")
        print(f"   Price: ${car['price']:,.2f}")
        print(f"   Mileage: {car['mileage']:,} miles")
        print()


def select_car(cars):
    """
    This lets the user see and select cars that are on the list that I provided below.
    """
    display_car_listings(cars)
    while True:
        try:
            choice = int(input("Enter the number of the car you're interested in: "))
            if 1 <= choice <= len(cars):
                return cars[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(cars)}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("Welcome to the Car Loan Calculator")

#this is just a list of many cars useed for the program, I picke dmany currently popular cars with their average prices and mileage when they are eing sold. 
#I also included the year of the car to make it more realistic. This list is being used because of my lack of API knwowlege and the fact that I am not able to use one.
    cars = [
        {"make": "Toyota", "model": "Camry", "year": 2020, "price": 25000, "mileage": 15000},
        {"make": "Toyota", "model": "Corolla", "year": 2019, "price": 20000, "mileage": 20000},
        {"make": "Toyota", "model": "Rav4", "year": 2021, "price": 30000, "mileage": 10000},
        {"make": "Toyota", "model": "Highlander", "year": 2018, "price": 35000, "mileage": 25000},
        {"make": "Toyota", "model": "Prius", "year": 2020, "price": 28000, "mileage": 12000},
        {"make": "Honda", "model": "Civic", "year": 2019, "price": 22000, "mileage": 18000},
        {"make": "Honda", "model": "Accord", "year": 2020, "price": 27000, "mileage": 15000},
        {"make": "Honda", "model": "CR-V", "year": 2021, "price": 32000, "mileage": 8000},
        {"make": "Honda", "model": "Pilot", "year": 2018, "price": 34000, "mileage": 22000},
        {"make": "Honda", "model": "Odyssey", "year": 2019, "price": 38000, "mileage": 20000},
        {"make": "Ford", "model": "F-150", "year": 2020, "price": 45000, "mileage": 12000},
        {"make": "Ford", "model": "Mustang", "year": 2021, "price": 35000, "mileage": 5000},
        {"make": "Ford", "model": "Escape", "year": 2019, "price": 25000, "mileage": 18000},
        {"make": "Ford", "model": "Explorer", "year": 2020, "price": 40000, "mileage": 15000},
        {"make": "Ford", "model": "Focus", "year": 2018, "price": 18000, "mileage": 25000},
        {"make": "Chevrolet", "model": "Silverado", "year": 2020, "price": 42000, "mileage": 10000},
        {"make": "Chevrolet", "model": "Equinox", "year": 2019, "price": 23000, "mileage": 20000},
        {"make": "Chevrolet", "model": "Malibu", "year": 2020, "price": 24000, "mileage": 15000},
        {"make": "Chevrolet", "model": "Tahoe", "year": 2021, "price": 55000, "mileage": 5000},
        {"make": "Chevrolet", "model": "Traverse", "year": 2018, "price": 32000, "mileage": 22000},
        {"make": "Nissan", "model": "Altima", "year": 2020, "price": 26000, "mileage": 12000},
        {"make": "Nissan", "model": "Rogue", "year": 2021, "price": 28000, "mileage": 8000},
        {"make": "Nissan", "model": "Sentra", "year": 2019, "price": 20000, "mileage": 18000},
        {"make": "Nissan", "model": "Pathfinder", "year": 2018, "price": 30000, "mileage": 25000},
        {"make": "Nissan", "model": "Maxima", "year": 2020, "price": 34000, "mileage": 15000},
        {"make": "Hyundai", "model": "Elantra", "year": 2019, "price": 19000, "mileage": 20000},
        {"make": "Hyundai", "model": "Sonata", "year": 2020, "price": 25000, "mileage": 15000},
        {"make": "Hyundai", "model": "Tucson", "year": 2021, "price": 27000, "mileage": 10000},
        {"make": "Hyundai", "model": "Santa Fe", "year": 2018, "price": 30000, "mileage": 22000},
        {"make": "Hyundai", "model": "Kona", "year": 2020, "price": 22000, "mileage": 12000},
        {"make": "Kia", "model": "Optima", "year": 2019, "price": 21000, "mileage": 18000},
        {"make": "Kia", "model": "Sorento", "year": 2020, "price": 32000, "mileage": 15000},
        {"make": "Kia", "model": "Sportage", "year": 2021, "price": 26000, "mileage": 8000},
        {"make": "Kia", "model": "Forte", "year": 2018, "price": 18000, "mileage": 25000},
        {"make": "Kia", "model": "Telluride", "year": 2020, "price": 40000, "mileage": 12000},
        {"make": "BMW", "model": "3 Series", "year": 2020, "price": 45000, "mileage": 10000},
        {"make": "BMW", "model": "X5", "year": 2021, "price": 60000, "mileage": 5000},
        {"make": "BMW", "model": "5 Series", "year": 2019, "price": 50000, "mileage": 15000},
        {"make": "BMW", "model": "X3", "year": 2018, "price": 40000, "mileage": 20000},
        {"make": "BMW", "model": "7 Series", "year": 2020, "price": 80000, "mileage": 12000},
        {"make": "Mercedes-Benz", "model": "C-Class", "year": 2020, "price": 48000, "mileage": 10000},
        {"make": "Mercedes-Benz", "model": "E-Class", "year": 2021, "price": 60000, "mileage": 5000},
        {"make": "Mercedes-Benz", "model": "GLC", "year": 2019, "price": 45000, "mileage": 15000},
        {"make": "Mercedes-Benz", "model": "GLE", "year": 2018, "price": 55000, "mileage": 20000},
        {"make": "Mercedes-Benz", "model": "S-Class", "year": 2020, "price": 90000, "mileage": 12000},
        {"make": "Audi", "model": "A4", "year": 2020, "price": 42000, "mileage": 10000},
        {"make": "Audi", "model": "Q5", "year": 2021, "price": 50000, "mileage": 5000},
        {"make": "Audi", "model": "A6", "year": 2019, "price": 48000, "mileage": 15000},
        {"make": "Audi", "model": "Q7", "year": 2018, "price": 55000, "mileage": 20000},
        {"make": "Audi", "model": "A8", "year": 2020, "price": 85000, "mileage": 12000},
        {"make": "Lexus", "model": "RX", "year": 2020, "price": 50000, "mileage": 10000},
        {"make": "Lexus", "model": "ES", "year": 2021, "price": 45000, "mileage": 5000},
        {"make": "Lexus", "model": "NX", "year": 2019, "price": 40000, "mileage": 15000},
        {"make": "Lexus", "model": "GX", "year": 2018, "price": 55000, "mileage": 20000},
        {"make": "Lexus", "model": "LS", "year": 2020, "price": 80000, "mileage": 12000},
        {"make": "Tesla", "model": "Model 3", "year": 2020, "price": 45000, "mileage": 10000},
        {"make": "Tesla", "model": "Model S", "year": 2021, "price": 80000, "mileage": 5000},
        {"make": "Tesla", "model": "Model X", "year": 2019, "price": 85000, "mileage": 15000},
        {"make": "Tesla", "model": "Model Y", "year": 2020, "price": 50000, "mileage": 12000},
    ]

    # Let the user select a car
    selected_car = select_car(cars)
    car_price = selected_car["price"]
    print(f"\nYou selected: {selected_car['make']} {selected_car['model']} ({selected_car['year']})")
    print(f"Price: ${car_price:,.2f}")

    # Get loan details
    down_payment = get_positive_float("Enter the down payment: ")
    loan_term = int(get_positive_float("Enter the loan term in months: "))
    credit_score = get_credit_score()
    monthly_income = get_positive_float("Enter your monthly income: ")

    # Calculate interest rate based on credit score
    annual_interest_rate = calculate_interest_rate(credit_score)
    print(f"Your Annual Interest Rate: {annual_interest_rate:.2f}%")

    # Calculate the loan amount
    principal = car_price - down_payment

    # Calculate monthly payment and total interest
    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, loan_term)
    total_interest = (monthly_payment * loan_term) - principal

    # This will check the affordability of the car 
    affordability_status = affordability(monthly_payment, monthly_income)

    # Calculate required salary to afford the car
    required_salary = calc_required_salary(monthly_payment)

    # Calculate debt-to-income ratio
    monthly_debt = get_positive_float("Enter your total monthly debt payments: ")
    dti_ratio = debt_to_income_ratio(monthly_debt, monthly_income)

    # This will display the loan summary
    print("\n--- Loan Summary ---")
    print(f"Car: {selected_car['make']} {selected_car['model']} ({selected_car['year']})")
    print(f"Price: ${car_price:,.2f}")
    print(f"Down Payment: ${down_payment:,.2f}")
    print(f"Loan Term: {loan_term} months")
    print(f"Annual Interest Rate: {annual_interest_rate:.2f}%")
    print(f"Monthly Payment: ${monthly_payment:,.2f}")
    print(f"Total Interest Paid: ${total_interest:,.2f}")
    print(f"Total Cost of Loan: ${(car_price - down_payment + total_interest):,.2f}")
    print(f"Affordability: {affordability_status}")
    print(f"Required Annual Salary: ${required_salary:,.2f}")
    print(f"Debt-to-Income Ratio: {dti_ratio:.2f}%")

    # This will sggest is the car is comfortable to afford for you(may deete this feature later )
    max_car_price = budget_planner(monthly_income)
    print(f"\nBased on your income, you should consider cars priced under ${max_car_price:,.2f}.")

    # This is optional, but adds a nice touch to the end to allow users to visualize how this would go depending on the loan term selected 
    show_schedule = input("\nDo you want to see the amortization schedule? (yes/no): ").strip().lower()
    if show_schedule == "yes":
        generate_amortization_schedule(principal, annual_interest_rate, loan_term)

    # This allows users to save this to a file so that they can eventually come back to this 
    save_results = input("\nDo you want to save the results to a file? (yes/no): ").strip().lower()
    if save_results == "yes":
        filename = "loan_summary.txt"
        content = f"""
        --- Loan Summary ---
        Car: {selected_car['make']} {selected_car['model']} ({selected_car['year']})
        Price: ${car_price:,.2f}
        Down Payment: ${down_payment:,.2f}
        Loan Term: {loan_term} months
        Annual Interest Rate: {annual_interest_rate:.2f}%
        Monthly Payment: ${monthly_payment:,.2f}
        Total Interest Paid: ${total_interest:,.2f}
        Total Cost of Loan: ${(car_price - down_payment + total_interest):,.2f}
        Affordability: {affordability_status}
        Required Annual Salary: ${required_salary:,.2f}
        Debt-to-Income Ratio: {dti_ratio:.2f}%
        """
        save_to_file(filename, content)


if __name__ == "__main__":
    main()