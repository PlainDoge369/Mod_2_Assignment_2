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

