investor_age = int(input("Enter your age: "))
liquid_capital = float(input("Enter your liquid capital (in USD): "))
experience_years = float(input("Enter your years of investment experience: "))
has_prior_closure = bool(input("Have you had any prior investment closures? (True/Leave blank if False): "))
location_name = input("Enter your location (city, state, or country): ")
location_population = int(input("Enter the population of your location: "))
franchise_tier = input("Enter the franchise tier (gold, silver, bronze): ").lower().strip()

franchise_fee__rate = 0

if franchise_tier not in ["gold", "silver", "bronze"]:
    print("Invalid franchise tier. Please enter 'gold', 'silver', or 'bronze'.")
    exit()

if investor_age >= 24 and experience_years >= 1.5 and liquid_capital >= 30000 and has_prior_closure == False:
    print("")
    print("You meet the basic requirements for investing in a franchise.")
    if franchise_tier == "gold":
        print("")
        print("You have chosen the gold franchise tier.")
        if liquid_capital >= 150000 and location_population >= 200000:
            print("You meet the requirements for a gold franchise.")
            if experience_years >= 5:
                franchise_fee__rate = 0.08
                print(f"Your franchise fee is {franchise_fee__rate * 100}%.")
                franchise_fee = liquid_capital * franchise_fee__rate
                print(f"Your base franchise fee is: ${franchise_fee:.2f}")
            else:
                franchise_fee__rate = 0.12
                print(f"Your franchise fee is {franchise_fee__rate * 100}%.")
                franchise_fee = liquid_capital * franchise_fee__rate
                print(f"Your base franchise fee is: ${franchise_fee:.2f}")

            base_fee = liquid_capital * franchise_fee__rate
            print(f"Your base franchise fee is: ${base_fee:.2f}")
            if liquid_capital % 5000 != 0:
                base_fee += 750
                print("An additional $750 fee has been added due to your liquid capital not being a multiple of $5,000.")
                print(f"Your total franchise fee is: ${base_fee:.2f}")
            else:
                print(f"Your total franchise fee is: ${base_fee:.2f}")
    else:
        print("")
        print("You do not meet the requirements for a gold franchise.")
        

    if franchise_tier == "silver":
        print("")
        print("You have chosen the silver franchise tier.")
        if liquid_capital >= 75000 and location_population >= 100000:
            print("You meet the requirements for a silver franchise.")
            if experience_years >= 3:
                franchise_fee__rate = 0.06
                print(f"Your franchise fee is {franchise_fee__rate * 100}%.")
                franchise_fee = liquid_capital * franchise_fee__rate
                print(f"Your base franchise fee is: ${franchise_fee:.2f}")
            else:
                franchise_fee__rate = 0.09
                print(f"Your franchise fee is {franchise_fee__rate * 100}%.")
                franchise_fee = liquid_capital * franchise_fee__rate
                print(f"Your base franchise fee is: ${franchise_fee:.2f}")

        base_fee = liquid_capital * franchise_fee__rate
        print(f"Your base franchise fee is: ${base_fee:.2f}")
        if liquid_capital % 5000 != 0:
            base_fee += 750
            print("An additional $750 fee has been added due to your liquid capital not being a multiple of $5,000.")
            print(f"Your total franchise fee is: ${base_fee:.2f}")
        else:
            print(f"Your total franchise fee is: ${base_fee:.2f}")
    else:
        print("")
        print("You do not meet the requirements for a silver franchise.")
        

    if franchise_tier == "bronze":
        print("")
        print("You have chosen the bronze franchise tier.")
        if liquid_capital >= 30000:
            print("You meet the requirements for a bronze franchise.")
            if experience_years >= 1.5:
                franchise_fee__rate = 0.05
                print(f"Your franchise fee is {franchise_fee__rate * 100}%.")
                franchise_fee = liquid_capital * franchise_fee__rate
                print(f"Your base franchise fee is: ${franchise_fee:.2f}")
            else:
                franchise_fee__rate = 0.05
                print(f"Your franchise fee is {franchise_fee__rate * 100}%.")
                franchise_fee = liquid_capital * franchise_fee__rate
                print(f"Your base franchise fee is: ${franchise_fee:.2f}")

        base_fee = liquid_capital * franchise_fee__rate
        print(f"Your base franchise fee is: ${base_fee:.2f}")
        if liquid_capital % 5000 != 0:
            base_fee += 750
            print("An additional $750 fee has been added due to your liquid capital not being a multiple of $5,000.")
            print(f"Your total franchise fee is: ${base_fee:.2f}")
        else:
            print(f"Your total franchise fee is: ${base_fee:.2f}")
    else:
        print("")
        print("You do not meet the requirements for a bronze franchise.")
else:
    print("You do not meet the basic requirements for investing in a franchise.")

if location_population >= 5000:
    print("")
    print(f"Location {location_name} is APPROVED for franchise opportunities.")
else:
    print("")
    print(f"Location {location_name} is NOT APPROVED for franchise opportunities.")
    
print("")
print("===============================")
print("Summary of Your Franchise Investment:")
print(f"Investor Age: {investor_age}")
print(f"Liquid Capital: ${liquid_capital:.2f}")
print(f"Years of Investment Experience: {experience_years}")
print(f"Prior Investment Closures: {'Yes' if has_prior_closure else 'No'}")
print(f"Location: {location_name} (Population: {location_population})")
print(f"Franchise Tier: {franchise_tier.capitalize()}")
print(f"Franchise Fee Rate: {franchise_fee__rate * 100}%")
print(f"Base Franchise Fee: ${franchise_fee:.2f}") 
print(f"Total Franchise Fee: ${base_fee:.2f}")
print("===============================")
print("This is an educational program for beginners")
