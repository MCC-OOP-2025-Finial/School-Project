from Enviroment.Room import Room
from Actors.Student import Student
from Actors.Staff import Staff
import asyncio
import time

# Define the StudentScheduleSimulator class
class StudentScheduleSimulator:
    """
    Runs a simple simulation that moves students through their daily schedule.
    """
    def __init__(self, students=None, staff=None, period_length_seconds=1):
        self.students = students or []
        self.staff = staff or []
        self.period_length_seconds = period_length_seconds  

    def add_student(self, student):
        """Add a student to the simulation."""
        self.students.append(student)
    
    def add_staff(self, staff_member):
        """Add a staff member to the simulation."""
        self.staff.append(staff_member)
    
    async def run_daily_simulation(self):
        """Run the full day simulation for all students."""
        print("📚 Starting Student Schedule Simulation...\n")
        print(f"⌛ Each period will last {self.period_length_seconds} second(s)." )

        max_periods = max(len(student.schedule) for student in self.students)

        for period in range(max_periods):
            time.sleep(self.period_length_seconds)
            print(f"\n=== Period {period + 1} ===")

            # Staff actions
            for staff_member in self.staff:
                if staff_member.role == "Teacher":
                    try:
                        if period == 0:
                            staff_member.Goto(staff_member.location)
                        print(staff_member.prepareLesson())
                        print(staff_member.recordAttendance())
                        print(staff_member.startTeaching())
                        print(staff_member.stopTeaching())
                    except Exception as e:
                        print(f"{staff_member.name} error: {e}")

            # Student actions
            for student in self.students:

                if student.schedule:
                    student.next_period()

                    student.Goto(student.current_class)

                   
                    student.attend_class()

                else:
                    print(f"{student.name} has no class this period.")

        print("\n🏁 Simulation Complete!\n")

