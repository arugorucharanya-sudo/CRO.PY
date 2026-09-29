 CRO Measurement Calculation

 Input values
volts_per_div = float(input("Enter Volts/Division: "))
vertical_div = float(input("Enter number of vertical divisions: "))

time_per_div = float(input("Enter Time/Division (s): "))
horizontal_div = float(input("Enter number of horizontal divisions: "))

 Calculate voltage
voltage = volts_per_div * vertical_div

 Calculate time period
time_period = time_per_div * horizontal_div

 Calculate frequency
frequency = 1 / time_period

 Display results
print("\n--- CRO Calculation ---")
print("Peak Voltage =", round(voltage, 4), "V")
print("Time Period =", round(time_period, 6), "s")
print("Frequency =", round(frequency, 2), "Hz")
