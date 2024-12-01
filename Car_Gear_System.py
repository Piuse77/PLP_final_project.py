# Define constants for maximum speeds of each gear
GEAR_MAX_SPEED = {
    'N': 0,   # Neutral
    '1': 20,  # Gear 1
    '2': 40,  # Gear 2
    '3': 60,  # Gear 3
    '4': 80,  # Gear 4
    '5': 100, # Gear 5
    '6': 120  # Gear 6
}

# Global variables for current state
current_gear = 'N'
current_speed = 0

# Function to change gear
def change_gear(target_gear):
    global current_gear
    global current_speed
    
    if target_gear not in GEAR_MAX_SPEED:
        print(f"Invalid gear: {target_gear}")
        return
    
    if current_gear == 'N' and target_gear != 'N':
        print("Starting the car...")
    
    if current_gear != 'N' and int(target_gear) < int(current_gear):
        print(f"Cannot shift directly from {current_gear} to {target_gear}. Shift sequentially.")
        return
    
    current_gear = target_gear
    print(f"Shifted to {current_gear}")

# Function to accelerate
def accelerate(speed_change):
    global current_speed
    
    if current_gear == 'N':
        print("Cannot accelerate in Neutral. Change to a gear first.")
        return
    
    target_speed = current_speed + speed_change
    
    if target_speed > GEAR_MAX_SPEED[current_gear]:
        print(f"Speed {target_speed} km/h exceeds max speed of {GEAR_MAX_SPEED[current_gear]} km/h for gear {current_gear}.")
    else:
        current_speed = target_speed
        print(f"Accelerated to {current_speed} km/h")

# Function to decelerate
def decelerate(speed_change):
    global current_speed
    
    if current_gear == 'N':
        print("Cannot decelerate in Neutral. Change to a gear first.")
        return
    
    target_speed = current_speed - speed_change
    
    if target_speed < 0:
        print("Speed cannot be negative. You are already stopped.")
    else:
        current_speed = target_speed
        print(f"Decelerated to {current_speed} km/h")

# Function to display current status
def display_status():
    print(f"\nCurrent Gear: {current_gear}")
    print(f"Current Speed: {current_speed} km/h")

# Main function to run the program
def main():
    print("Welcome to the Car Gear System!\n")
    
    while True:
        display_status()
        
        print("\nOptions:")
        print("1. Change Gear")
        print("2. Accelerate")
        print("3. Decelerate")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                target_gear = input("Enter gear choice (N, 1, 2, 3, 4, 5, 6): ").strip().upper()
                change_gear(target_gear)
            elif choice == 2:
                speed_change = int(input("Enter speed to increase (km/h): "))
                accelerate(speed_change)
            elif choice == 3:
                speed_change = int(input("Enter speed to decrease (km/h): "))
                decelerate(speed_change)
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":

    main()
