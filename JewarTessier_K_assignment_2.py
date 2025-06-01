# SIMPLE DATA TYPES

name = "Kassius"
print(f"name: {name} type: {type(name)}")
has_license = False
print(f"has license: {has_license} type: {type(has_license)}")
this_year = 2025
print(f"this year: {this_year} type: {type(this_year)}")
this_year += 1
print(f"next year: {this_year} type: {type(this_year)}")

# MATHEMATICAL OPERATIONS

GST_RATE = 0.05 
PST_RATE = 0.07
vehicle_price = 88888.88
provincial_tax = vehicle_price * PST_RATE
federal_tax = vehicle_price * GST_RATE
total_cost = vehicle_price + provincial_tax + federal_tax
print("Purchase price:", vehicle_price, "Provincial Tax:", provincial_tax, "Federal Tax:", federal_tax, "Total:", total_cost)
print(f"Purchase Price: ${vehicle_price:,.2f} Provincial Tax: ${provincial_tax:,.2f} Federal Tax: ${federal_tax:,.2f} Total: ${total_cost:,.2f}")

# LIST

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Type:", type(numbers))
print("List:", numbers)
numbers.insert(5, "Kassius")
print("List with name:", numbers)
numbers.remove(9)
print("List without 9:", numbers)
letters = ['A', 'B', 'C']
combined = numbers + letters
print("Combined list:", combined)

# TUPLES
 
provinces = ("British Columbia", "Yukon", "Nova-Scotia", "Manitoba")
print("Type:", type(provinces))
print("Tuple:", provinces)

# DICTIONARIES

coins = {'nickel': 0.05, 'dime': 0.10, 'quarter': 0.25}
print("Type:", type(coins))
print("Dictionary:", coins)
coins['nickel'] = 5
coins['dime'] = 10
coins['quarter'] = 25
print("Dictionary with whole numbers:", coins)
coins['Loonie'] = 100
coins['Toonie'] = 200
print("Dictionary with Loonie and Toonie:", coins)