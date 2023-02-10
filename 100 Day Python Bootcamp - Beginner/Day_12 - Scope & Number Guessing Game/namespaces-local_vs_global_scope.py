
# NameSpaces Local vs Global Scope

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
# Local scope exists within functions

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) # Won't work because it's not global

# Global Scope

player_health = 10 # Defined outside the function, can be called inside or outside a function - Global Variable

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# Modifying Global Scope

enemies = 1

def increase_enemies():
    # global enemies # DO NOT USE GLOBAL IF NOT NEEDED
    print(f"enemies inside function: {enemies}")
    return enemies + 2 # Access and call global variables with the return statement

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159 # Global Constants are usually done with capital leters

def calc():
    PI

