#Caleb/James/Elijah/Wilfried
import asyncio
from Data.Rooms import Rooms
from Data.Classes import Classes

# Define the StudentScheduleSimulator class
class StudentScheduleSimulator:
    """
    Runs a simple simulation that moves students through their daily schedule.
    Includes a lunch period between periods 2 and 3.
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
    
    """
    Add staff to their assigned rooms
    Add students to their current locations
    Print all rooms and occupants
    """
    def _print_room_occupancy_report(self):
        """Print room occupancy report showing all staff and students by location."""
        print("\nRoom Occupancy Report:")
        room_occupants = {room: [] for room in Rooms}
        
        
        for staff_member in self.staff:
            if staff_member.location in room_occupants:
                room_occupants[staff_member.location].append(
                    f"{staff_member.role} {staff_member.name}"
                )
        
        
        for student in self.students:
            if student.location in room_occupants:
                room_occupants[student.location].append(
                    f"Student {student.name}"
                )
        
        
        for room_name in Rooms:
            occupants = room_occupants[room_name]
            if occupants:
                print(f"  {room_name}: {', '.join(occupants)}\n")
            else:
                print(f"  {room_name}: (empty)\n")
    
    async def run_daily_simulation(self):
        """Run the full day simulation for all students."""
        print("Starting Student Schedule Simulation...\n")
        print(f"Each period will last {self.period_length_seconds} second(s)." )

        max_periods = max(len(student.schedule) for student in self.students)

        """
        # Build mapping from short class name (e.g. "Math") -> room name
        # (e.g. "Math Classroom") so we can match teacher locations to
        # student schedule entries. Prefer rooms containing "Classroom", then
        # "Room", then fallback to the first matching room.
        """
        class_to_room = {}
        for c in Classes:
            matches = [r for r in Rooms if c in r]
            if matches:
                # preference order
                preferred = None
                for m in matches:
                    if "Classroom" in m:
                        preferred = m
                        break
                if not preferred:
                    for m in matches:
                        if "Room" in m:
                            preferred = m
                            break
                if not preferred:
                    preferred = matches[0]
                class_to_room[c] = preferred

        # Ensure Physical Education maps to the Gymnasium
        if 'Physical Education' not in class_to_room and 'Gymnasium' in Rooms:
            class_to_room['Physical Education'] = 'Gymnasium'

        # Explicit mappings for classes without direct substring matches
        explicit_mappings = {
            'Literature': 'English Classroom',
            'Biology': 'Science Lab',
            'Chemistry': 'Science Lab',
        }
        for class_name, room_name in explicit_mappings.items():
            if class_name not in class_to_room and room_name in Rooms:
                class_to_room[class_name] = room_name

        # reverse mapping: room -> class short name
        room_to_class = {v: k for k, v in class_to_room.items()}

        period_num = 0
        for period in range(max_periods):
            await asyncio.sleep(self.period_length_seconds)
            
            # Insert lunch period after period 2
            if period == 2:
                await self._run_lunch_period(3)
            else:
                period_num += 1
                print(f"\n=== Period {period_num} ===")

                # determine which classes will run this period (peek at students' next class)
                upcoming_classes = set()
                for student in self.students:
                    if student.schedule:
                        upcoming_classes.add(student.schedule[0])

                # convert short class names -> room names for teacher matching
                upcoming_rooms = set()
                for c in upcoming_classes:
                    room = class_to_room.get(c)
                    if room:
                        upcoming_rooms.add(room)

                # 1) Teachers (and Coaches for PE) prepare lesson materials for active classes only
                for staff_member in self.staff:
                    room = staff_member.location
                    if room not in upcoming_rooms:
                        continue
                    class_name = room_to_class.get(room)
                    # Physical Education must be taught by a Coach in the Gymnasium
                    if class_name == 'Physical Education':
                        if staff_member.role != 'Coach':
                            continue
                    else:
                        if staff_member.role != 'Teacher':
                            continue
                    try:
                        if period == 0:
                            staff_member.Goto(room)
                        print(staff_member.prepareLesson())
                    except Exception as e:
                        print(f"{staff_member.name} error (prepare): {e}")
                """
                Students move to next class and attend
                Keep mapping of class -> students for teacher attendance info
                """
                class_attendance = {}
                for student in self.students:
                    if student.schedule:
                        current = student.next_period()
                        # Move student to the room corresponding to the class (if known)
                        room = class_to_room.get(current)
                        student.Goto(room or student.current_class)
                        student.attend_class()
                        class_attendance.setdefault(current, []).append(student)
                    else:
                        print(f"{student.name} has no class this period.")
                """
                Teachers for active classes record attendance, start, then stop the lesson
                map staff member's room back to the short class name
                Enforce that Physical Education is taught by a Coach
                Non-PE classes must be taught by Teachers
                """
                for staff_member in self.staff:
                    class_name = room_to_class.get(staff_member.location)
                    if not class_name:
                        # no mapping available, skip
                        continue
                    if class_name not in class_attendance:
                        continue
                    if class_name == 'Physical Education' and staff_member.role != 'Coach':
                        continue
                    if class_name != 'Physical Education' and staff_member.role != 'Teacher':
                        continue
                    try:
                        # Optionally include the number of students present
                        attendance_msg = staff_member.recordAttendance()
                        if "#LIST OF STUDENTS" in attendance_msg or "#LIST OF STUDENTS here" in attendance_msg:
                            attendance_msg = f"{staff_member.role} {staff_member.name} is recording attendance for their class. Students present: {len(class_attendance[class_name])}."
                        print(attendance_msg)
                        print(staff_member.startTeaching())
                        print(staff_member.stopTeaching())
                    except Exception as e:
                        print(f"{staff_member.name} error (class): {e}")

                # Print room occupancy report after period activities
                self._print_room_occupancy_report()

        print("\nSimulation Complete!\n")
    """
    Lunch Period
    All students go to cafeteria
    Print students attending lunch
    Cafeteria Worker serves food after all students arrive
    Cafeteria Worker cleans after students finish lunch
    # Print room occupancy report after lunch
    """
    async def _run_lunch_period(self, lunch_period_num):
        """
        Run a lunch period where all students go to the Cafeteria.
        Cafeteria Worker serves food after all students arrive, then cleans after.
        """
        print(f"\n=== Lunch Period ===")
        
        print("\nStudents heading to Cafeteria:")
        for student in self.students:
            student.Goto("Cafeteria")
            print(f"{student.name} is going to Cafeteria.")
        
        print("\nStudents attending lunch:")
        for student in self.students:
            print(f"{student.name} is attending lunch in the Cafeteria.")
        
        print("\nCafeteria Worker serving food:")
        for staff_member in self.staff:
            if staff_member.role == "Cafeteria Worker":
                try:
                    print(f"{staff_member.serveFood()}")
                except Exception as e:
                    print(f"{staff_member.name} error (serve): {e}")

        print("\n🧹 Cafeteria Worker cleaning:")
        for staff_member in self.staff:
            if staff_member.role == "Cafeteria Worker":
                try:
                    print(f"{staff_member.cleanCafeteria()}")
                except Exception as e:
                    print(f"{staff_member.name} error (clean): {e}")
        
        self._print_room_occupancy_report()
