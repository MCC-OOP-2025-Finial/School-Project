"""
Main entry point for the School Simulation Project
"""

from Actors.Student import Student
from Actors.Staff import Staff
from Environment.Room import Room
from StudentScheduleSimulator import StudentScheduleSimulator


# -------------------------------------------------------
# 1. Create sample staff members
# -------------------------------------------------------
print("\n--- Creating Staff Members ---")

teacher = Staff(role="Teacher")
principal = Staff(role="Principal")

print(teacher)
print(principal)


# -------------------------------------------------------
# 2. Create sample students
# -------------------------------------------------------
print("\n--- Creating Students ---")

student1 = Student(name="Alice Johnson", major="Math", gpa=3.4)
student2 = Student(name="Michael Torres", major="History", gpa=2.9)

print(student1)
print(student2)


# -------------------------------------------------------
# 3. Assign schedules for simulation
# (must be lists, because StudentScheduleSimulator pops in order)
# -------------------------------------------------------
print("\n--- Assigning Schedules ---")

schedule1 = [
    "Homeroom",
    "Math",
    "English",
    "Science",
    "Lunch",
    "Gym",
    "History"
]

schedule2 = [
    "Homeroom",
    "History",
    "Science",
    "English",
    "Lunch",
    "Math",
    "Art"
]

student1.set_schedule(schedule1)
student2.set_schedule(schedule2)


# -------------------------------------------------------
# 4. Run Simulation
# -------------------------------------------------------
print("\n--- Running Student Schedule Simulation ---")

sim = StudentScheduleSimulator()
sim.add_student(student1)
sim.add_student(student2)

sim.run_daily_simulation()

print("\n--- Simulation Complete ---")
