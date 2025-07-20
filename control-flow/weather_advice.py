# weather_advice.py

# 1. Ask for input, strip extra spaces, and convert to lowercase
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# 2. Conditional logic
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    # 3. This else catches everything else
    print("Sorry, I don't have recommendations for this weather.")
