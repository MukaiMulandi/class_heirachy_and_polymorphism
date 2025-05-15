# class_heirachy_and_polymorphism
 Designing  a Class with Inheritance and a Polymorphism Challenge


# 🦸‍♂️ Superhero & Vehicle Polymorphism Project

This project consists of two fun and educational activities that explore **object-oriented programming** concepts in Python, including:

- Class design and instantiation
- Encapsulation and inheritance
- Polymorphism using method overriding

---

## 📦 Contents

### 🔹 Assignment 1: Design Your Own Class – Superhero System

We define a class hierarchy to represent **superheroes**, each with special abilities and encapsulated data.

### Classes:
- `Superhero`: Base class with common attributes and private power level
- `FlyingHero`: Inherits from `Superhero` and adds `flight_speed`
- `StrengthHero`: Inherits from `Superhero` and adds `max_lift`

#### Example Usage:
```python
hero1 = FlyingHero("Clark Kent", "Superman", 3000)
hero2 = StrengthHero("Bruce Banner", "Hulk", 100)

hero1.use_power()  # Superman soars through the skies!
hero2.train()      # Hulk increases power level
```


🔹 Activity 2: Polymorphism Challenge – Vehicles in Motion
We demonstrate polymorphism by creating a group of vehicles, each with a different version of the move() method.

Classes:
Vehicle (Base class)

Car: Overrides move() to print "Driving 🚗"

Plane: Overrides move() to print "Flying ✈️"

Boat: Overrides move() to print "Sailing 🚢"

Example Usage:

vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()

    
🔧 How to Run
Clone or download the project

Open main.py or copy the code into a Python environment

Run the script to see superheroes in action and polymorphic vehicles moving



🧠 Concepts Demonstrated
Encapsulation: Private variables like __power_level

Inheritance: Shared behavior via superclass Superhero

Polymorphism: Each subclass overrides move() or use_power()

Constructor Usage: Initialization of unique attributes with __init__()



📁 File Structure

bash
superhero_project/
│
├── main.py         # Contains all class definitions and test code
└── README.md       # This file
✨ Future Ideas
Add a Villain class for battles

Track experience or levels with methods

Expand vehicle system with fuel management or passengers



🐍 Requirements
Python 3.6+

No external libraries required

👨‍💻 Author
Created as a fun OOP exercise demonstrating class design, inheritance, and polymorphism in Python.

yaml

---

Would you like me to package this with the code into files and upload them for you?






