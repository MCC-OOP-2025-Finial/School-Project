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
    teachers = []
    teacher = Staff(role="Teacher")
    teachers.append(teacher)
    return teachers