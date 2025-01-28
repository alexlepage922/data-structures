# Problem 3
# Initialize dictionary
people = {"Alice": 25, "Bob": 30, "Charlie": 35, "Diana": 28, "Eve": 22}
# Add a new person
def add_person(name, age):
    people[name] = age
    print(f"Added {name} with age {age}.")
# Remove a person by name
def remove_person(name):
    if people.pop(name, None):
        print(f"Removed {name}.")
    else:
        print(f"{name} not found.")
# Print the average age
def print_average_age():
    if people:
        avg_age = sum(people.values()) / len(people)
        print(f"Average age: {avg_age:.2f}")
    else:
        print("No people in the dictionary.")
# Example usage
add_person("Frank", 27)
remove_person("Alice")
print_average_age()

# Problem 4
# Initialize dictionary
student_scores = {"John": 75, "Alice": 90, "Bob": 85, "Diana": 78, "Eve": 88}
# Print the student with the highest score
def highest_score():
    if student_scores:
        top_student = max(student_scores, key=student_scores.get)
        print(f"Highest score: {top_student} ({student_scores[top_student]})")
    else:
        print("No students in the dictionary.")
# Print names of students who scored above 80
def above_eighty():
    high_scorers = [name for name, score in student_scores.items() if score > 80]
    print("Students scoring above 80:", ", ".join(high_scorers) if high_scorers else "None")
# Example usage
highest_score()
above_eighty()
