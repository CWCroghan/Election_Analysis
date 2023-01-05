#counties = ["Arapahoe","Denver","Jefferson"]
#if "Arapahoe" in counties and "El Paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not")

#dictionary    
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")