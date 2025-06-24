# In this app i ask my user to input a character name and a power. The user can add as many characters and powers as they want. The user can also exit the app by entering 'e' or 'E'. The app will then display the character that wins
# based on the power of the characters. The app will also display the total power of all the characters.
# The app will also display the character with the highest power.
# I have demonstrated the use of lists, loops, and functions in this app. I have also demonstrated the use of if statements to check for the exit condition. I have also demonstrated the use of the input function to get user input. I have also demonstrated the use of the print function to display output to the user and imported the random function.

import random
def scale_power(power):
    multiplier = random.uniform(0.5,1.5, 2.5,3.0)  # Random multiplier between variable scope
   
    return  power * multiplier, multiplier  # Scale the power and round to 2 decimal places

characters ={}

while True :
    name = input("Input character name or (type 'fight' to iniate fight sequence)")
    if name.lower() == 'fight':
        break
    power_input = (f"Enter base power level for {name}:  ")
    
try:
    power = float(power_input)
    scaled ,multiplier  = scale_power(power)
    characters[name] = {
    'base' : power,
    'scaled' : scaled,
    'multiplier' : multiplier
    } 
    print(f"{name} got a multiplier of {multiplier:.2f} → scaled power: {scaled:.2f}\n")
except ValueError:
    print("⚠️ Please enter a valid number for power level.\n")

    
def determine_winner(characters):
     if not characters:
        return None
     return max(characters.items(), key=lambda item: item[1]['scaled'])

# Show everyone’s stats
print("\n📊 Final Results:")
for name, stats in characters.items():
    print(f"{name} → Base: {stats['base']} | Multiplier: {stats['multiplier']:.2f} | Scaled: {stats['scaled']:.2f}")

# Declare winner
winner = determine_winner(characters)
if winner:
    name, stats = winner
    print(f"\n🏆 Winner: {name} with a scaled power of {stats['scaled']:.2f}!")
else:
    print("No characters to compare.")
    
