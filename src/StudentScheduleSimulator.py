from Enviroment.Room import Room
from Actors.Student import Student
from Actors.Staff import Staff
import asyncio

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
            await asyncio.sleep(self.period_length_seconds)
            print(f"\n=== Period {period + 1} ===")

            # determine which classes will run this period (peek at students' next class)
            upcoming_classes = set()
            for student in self.students:
                if student.schedule:
                    upcoming_classes.add(student.schedule[0])

            # 1) Teachers prepare lesson materials for active classes only
            for staff_member in self.staff:
                if staff_member.role == "Teacher" and staff_member.location in upcoming_classes:
                    try:
                        if period == 0:
                            staff_member.Goto(staff_member.location)
                        print(staff_member.prepareLesson())
                    except Exception as e:
                        print(f"{staff_member.name} error (prepare): {e}")

            # 2-3) Students move to next class and attend
            # Keep mapping of class -> students for teacher attendance info
            class_attendance = {}
            for student in self.students:
                if student.schedule:
                    current = student.next_period()
                    student.Goto(student.current_class)
                    student.attend_class()
                    class_attendance.setdefault(current, []).append(student)
                else:
                    print(f"{student.name} has no class this period.")

            # 4-6) Teachers for active classes record attendance, start, then stop the lesson
            for staff_member in self.staff:
                if staff_member.role == "Teacher" and staff_member.location in class_attendance:
                    try:
                        # Optionally include the number of students present
                        attendance_msg = staff_member.recordAttendance()
                        # replace placeholder with count if present
                        if "#LIST OF STUDENTS" in attendance_msg or "#LIST OF STUDENTS PRESENT IN ROOM" in attendance_msg:
                            attendance_msg = f"{staff_member.role} {staff_member.name} is recording attendance for their class. Students present: {len(class_attendance[staff_member.location])}."
                        print(attendance_msg)
                        print(staff_member.startTeaching())
                        print(staff_member.stopTeaching())
                    except Exception as e:
                        print(f"{staff_member.name} error (class): {e}")

        print("\n🏁 Simulation Complete!\n")

