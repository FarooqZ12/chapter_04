# -------------------------------------------
# ✅ 1. Creating and Accessing a Dictionary
# -------------------------------------------

info = {
    "name": "Umar Farooq",
    "age": 22,
    "city": "Lahore"
}

print("Name:", info["name"])          # Accessing using []
print("City:", info.get("city"))      # Accessing using .get()


# -------------------------------------------
# ✅ 2. Updating and Deleting Dictionary Items
# -------------------------------------------

person = {"name": "Ali", "skills": "HTML"}

person["skills"] = "HTML & CSS"         # Update using []
person.update({"city": "Karachi"})      # Update using .update()

del person["skills"]                    # Delete using del
# person.pop("name")                    # You can also use .pop()

print("Updated Dictionary:", person)


# -------------------------------------------
# ✅ 3. Looping through a Dictionary
# -------------------------------------------

student = {
    "name": "Sara",
    "class": "10th",
    "grade": "A"
}

for key, value in student.items():
    print(f"{key}: {value}")


# -------------------------------------------
# ✅ 4. Nested Dictionary Example
# -------------------------------------------

students = {
    1: {"name": "Umar", "marks": {"math": 85, "english": 78, "science": 90}},
    2: {"name": "Ali", "marks": {"math": 75, "english": 88, "science": 80}},
    3: {"name": "Sara", "marks": {"math": 92, "english": 91, "science": 89}}
}

for sid, info in students.items():
    print("Student ID:", sid)
    print("Name:", info["name"])

    total = 0
    print("Marks:")
    for subject, mark in info["marks"].items():
        print(f"  {subject}: {mark}")
        total += mark

    print("Total Marks:", total)
    print("-" * 20)


# -------------------------------------------
# ✅ 5. Creating and Using Sets
# -------------------------------------------

my_set = {"apple", "banana", "cherry"}
print("Set:", my_set)

my_set.add("orange")        # Add element
my_set.remove("banana")     # Remove element (error if not found)
my_set.discard("grape")     # Safe remove (no error if not found)

for fruit in my_set:
    print("Fruit:", fruit)


# -------------------------------------------
# ✅ 6. Set Operations
# -------------------------------------------

skills1 = {"python", "html", "css"}
skills2 = {"python", "javascript", "react"}

print("Union:", skills1.union(skills2))
print("Intersection:", skills1.intersection(skills2))
print("Difference:", skills1.difference(skills2))
print("Symmetric Difference:", skills1.symmetric_difference(skills2))


# -------------------------------------------
# ✅ 7. Useful Set Methods
# -------------------------------------------

A = {1, 2, 3}
B = {3, 4, 5}

print("Is A disjoint B?", A.isdisjoint(B))    # No common element?
print("Is A subset of B?", A.issubset(B))     # A inside B?
print("Is A superset of B?", A.issuperset(B))  # A contains B?
