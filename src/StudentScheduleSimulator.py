from Actors.Student import Student

class StudentScheduleSimulator:
    """
    Runs a simple simulation that moves students through their daily schedule.
    """

    def __init__(self, students=None):
        self.students = students or []

    def add_student(self, student):
        """Add a student to the simulation."""
        self.students.append(student)

    def run_daily_simulation(self):
        """Run the full day simulation for all students."""
        print("📚 Starting Student Schedule Simulation...\n")

        # Determine how many class periods exist at most
        max_periods = max(len(student.schedule) for student in self.students)

        for period in range(max_periods):
            print(f"\n=== Period {period + 1} ===")

            for student in self.students:

                if student.schedule:
                    # Move to next class
                    student.next_period()

                    # Simulate moving to class
                    student.go_to(student.current_class)

                    # Simulate attending class
                    student.attend_class()

                else:
                    print(f"{student.name} has no class this period.")

        print("\n🏁 Simulation Complete!\n")


# --------------------------------------------------------------
# Standalone testing (only runs if this file is executed directly)
# --------------------------------------------------------------

if __name__ == "__main__":
    s1 = Student(
        name="Alice",
        major="Math",
        gpa=3.5,
        schedule=["Room 101", "Room 203", "Library"]
    )

    s2 = Student(
        name="Bob",
        major="Science",
        gpa=3.1,
        schedule=["Gym", "Room 102"]
    )

    sim = StudentScheduleSimulator([s1, s2])
    sim.run_daily_simulation()
