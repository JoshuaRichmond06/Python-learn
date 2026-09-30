def calculate_force(mass, acceleration):

    return mass * acceleration


mass_kg = float(input("Enter the mass in kg: "))

acceleration_m_s2 = float(input("Enter the acceleration in m/s^2: "))

force_n = calculate_force(mass_kg, acceleration_m_s2)

weight_n = calculate_force(mass_kg, 9.81)

print(f"Force: {force_n:.2f} N, weight: {weight_n:.2f} N")