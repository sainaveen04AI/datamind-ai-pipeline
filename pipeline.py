import random
import json
from datetime import datetime

print("Hello! This is my data pipeline.")

# This creates fake data
def make_data():
    data = []
    for i in range(10):
        record = {
            "id": i,
            "name": "User" + str(i),
            "age": random.randint(20, 60),
            "city": random.choice(["New York", "London", "Tokyo"])
        }
        data.append(record)
    return data

# This breaks the data randomly
def break_data(data):
    broken = data.copy()
    # Randomly change a city to a number (wrong type)
    if random.random() > 0.5:
        broken[0]["city"] = 12345  # Wrong! Should be text
        print("💥 I BROKE THE DATA! City is now a number.")
        return broken, True
    else:
        print("✅ Data is clean.")
        return broken, False

# This checks if data is good
def check_data(data):
    errors = []
    for i, record in enumerate(data):
        if not isinstance(record["city"], str):
            errors.append(f"Record {i}: City should be text, not number")
    
    if errors:
        print("❌ ERRORS FOUND:")
        for error in errors:
            print("  - " + error)
        return False
    else:
        print("✅ All good!")
        return True

# Run everything
print("=" * 40)
print("STEP 1: Making data...")
my_data = make_data()
print(f"Made {len(my_data)} records")

print("\nSTEP 2: Maybe breaking data...")
my_data, was_broken = break_data(my_data)

print("\nSTEP 3: Checking data...")
is_good = check_data(my_data)

print("\n" + "=" * 40)
if was_broken and not is_good:
    print("RESULT: Pipeline broke and we caught it!")
elif not was_broken and is_good:
    print("RESULT: Pipeline ran perfectly!")
else:
    print("RESULT: Something unexpected happened")