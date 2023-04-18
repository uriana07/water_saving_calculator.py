print("Water Saving Calculator")

shower_time = int(input("How many minutes do you spend in the shower each day? "))
shower_flow_rate = float(input("What is the flow rate of your showerhead (in gallons per minute)? "))
toilet_flushes = int(input("How many times do you flush the toilet each day? "))
toilet_flush_volume = float(input("What is the volume of water per flush (in gallons)? "))
hand_washing = int(input("How many times do you wash your hands each day? "))
hand_washing_volume = float(input("What is the volume of water you use to wash your hands (in gallons)? "))

shower_water_use = shower_time * shower_flow_rate * 7
toilet_water_use = toilet_flushes * toilet_flush_volume * 7
hand_washing_water_use = hand_washing * hand_washing_volume * 7

total_water_use = shower_water_use + toilet_water_use + hand_washing_water_use

print("You use", total_water_use, "gallons of water per week.")
print("Here are some ways you can save water:")
print("- Take shorter showers.")
print("- Install a low-flow showerhead.")
print("- Don't flush the toilet unnecessarily.")
print("- Install a low-flow toilet.")
print("- Turn off the faucet when washing your hands.")
