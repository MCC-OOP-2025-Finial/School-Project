#Caleb
## Store error handling
import traceback
import sys

class DeniedRoleMethod(Exception):

    """Custom exception for denied role methods in Staff subclasses.
    Captures detailed context about where the exception was raised.
    
    Attributes:
        
        message: Explanation of the error.
        line_number: Line number where the exception was raised.
        filename: Filename where the exception was raised.
        function_name: Function name where the exception was raised.
    
    @example:
        raise DeniedRoleMethod("This role cannot perform this action")
    """

    def __init__(self, message="A custom error occurred", line_number=None, filename=None, function_name=None):
            self.message = message
            super().__init__(self.message) # Call the base class constructor
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb_list = traceback.extract_tb(exc_traceback)
            # The last element of tb_list corresponds to the point where the exception was raised
            line_info = tb_list[-1]
            self.line_number = line_info.lineno
            self.filename = line_info.filename
            self.function_name = line_info.name

    def __str__(self):
        return f"DeniedRoleMethod: {self.message} file: {self.filename}, function: {self.function_name}, on line: {self.line_number} "
    



class InvalidScheduleError(Exception):
    """Custom exception for invalid schedules.
    
    Attributes:
        message: Explanation of the error.
        schedule: The invalid schedule that caused the error.

    @example:
        raise InvalidScheduleError("Schedule format is invalid", schedule)
    """
    
    def __init__(self, message="Invalid schedule format", schedule=None):
        self.message = message
        self.schedule = schedule
        super().__init__(self.message)  # Call the base class constructor
    def __str__(self):
        return f"InvalidScheduleError: {self.message} | Schedule: {self.schedule} \n Schedule must be a list of strings representing locations. Ex: ['Art', 'Library', 'Gym']"
    

class TooManyStudentsError(Exception):
    """Custom exception for exceeding maximum number of students.
    
    Attributes:
        message: Explanation of the error.
        max_students: The maximum allowed number of students.
    @example:

        raise TooManyStudentsError("Exceeded maximum number of students", max_students)
    """
    
    def __init__(self, message="Too many students enrolled", max_students=None):
        self.message = message
        self.max_students = max_students
        super().__init__(self.message)  # Call the base class constructor
    def __str__(self):
        return f"TooManyStudentsError: {self.message} | Max Students Allowed: {self.max_students}"
    

def generate_student(numStudents):
    """Generate a list of dummy student for simulation purposes.
    
    Args:
        numStudents: Number of student to generate.

    Returns:

        List of generated student.
    """
    from Actors.Student import Student
    students = []
    for _ in range(numStudents):
        student = Student()
        students.append(student)
    return students

def generate_teacher():
    """Generate a list of dummy staff for simulation purposes."""
    from Actors.Staff import Staff
    # Instead of using class-type names (e.g. "Math"), create teachers only for
    # actual classroom locations defined in Data.Rooms.Rooms. This ensures
    # teachers are placed in real rooms like "Math Classroom" or "Computer Lab".
    from Data.Rooms import Rooms

    teachers = []
    # Treat rooms that look like classrooms: contain Classroom, Room, or Lab
    classroom_keywords = ("Classroom", "Room", "Lab")
    classroom_rooms = [r for r in Rooms if any(k in r for k in classroom_keywords)]

    for room_name in classroom_rooms:
        # Let ActorMain generate a realistic personal name; set location to the room name
        teacher = Staff(role="Teacher", location=room_name)
        teachers.append(teacher)

    return teachers


def generate_other_staff():
    """Generate staff members per non-teacher role, assigned to specified rooms.
    
    Roles and room assignments:
    - Principal (1) -> Principal Office
    - Vice Principal (1) -> Main Office
    - Custodian (2) -> Cafeteria
    - Resource Officer (2) -> Main Office
    - IT (1) -> Computer Lab
    - Nurse (1) -> Nurse Office
    - Guidance Counselor (1) -> Guidance Office
    - Librarian (1) -> Library
    - Cafeteria Worker (3) -> Cafeteria
    - Coach (1) -> Gymnasium
    - Secratary (1) -> Main Office
    
    Returns:
        List of Staff objects.
    """
    from Actors.Staff import Staff
    
    # Explicit role -> (room, count) assignment
    role_room_count_map = {
        "Principal": ("Principal Office", 1),
        "Vice Principal": ("Main Office", 1),
        "Custodian": ("Cafeteria", 2),
        "Resource Officer": ("Main Office", 2),
        "IT": ("Computer Lab", 1),
        "Nurse": ("Nurse Office", 1),
        "Guidance Counselor": ("Guidance Office", 1),
        "Librarian": ("Library", 1),
        "Cafeteria Worker": ("Cafeteria", 3),
        "Coach": ("Gymnasium", 1),
        "Secratary": ("Main Office", 1),
    }
    
    staff_list = []
    for role, (room, count) in role_room_count_map.items():
        for _ in range(count):
            staff_member = Staff(role=role, location=room)
            staff_list.append(staff_member)
    
    return staff_list


def generate_rooms(teachers=None):
    """Create Room objects for every name listed in `Data.Rooms.Rooms`.

    If `teachers` is provided, teachers whose `location` matches a room
    name will be attached to that Room as its teacher.
    Returns a dict mapping room name -> Room instance.
    """
    from Enviroment.Room import Room
    from Data.Rooms import Rooms

    rooms = {}
    for name in Rooms:
        # find a teacher assigned to this location (if given)
        teacher = None
        if teachers:
            for t in teachers:
                if getattr(t, 'location', None) == name:
                    teacher = t
                    break

        room = Room(name=name, description=f"{name} in the school.", actors=[], teacher=teacher)
        rooms[name] = room

    return rooms