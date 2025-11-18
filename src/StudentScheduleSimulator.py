from Enviroment.Room import Room
from Actors.Student import Student

import asyncio

import time

class StudentScheduleSimulator:
    """
    Runs a simple simulation that moves students through their daily schedule.
    """
    def __init__(self, students=None, period_length_seconds=1):
        self.students = students or []
        self.period_length_seconds = period_length_seconds  

    def add_student(self, student):
        """Add a student to the simulation."""
        self.students.append(student)

    async def run_daily_simulation(self):
        """Run the full day simulation for all students."""
        print("📚 Starting Student Schedule Simulation...\n")
        print(f"⌛ Each period will last {self.period_length_seconds} second(s)." )


        max_periods = max(len(student.schedule) for student in self.students)

        for period in range(max_periods):
            time.sleep(self.period_length_seconds)
            print(f"\n=== Period {period + 1} ===")

            for student in self.students:

                if student.schedule:
                    student.next_period()

                    student.go_to(student.current_class)

                   
                    student.attend_class()

                else:
                    print(f"{student.name} has no class this period.")

        print("\n🏁 Simulation Complete!\n")

