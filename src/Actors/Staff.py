from Actors.Actor_Main import ActorMain
import random


class Staff(ActorMain):
    def __init__(self, role, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        # Allow passing actor fields like name, age, etc. via kwargs
        super().__init__(**kwargs)
        self.role = role
        self.salary = salary or "0"
        self.hoursWorkedWeek = hoursWorkedWeek or 0
        self.experienceYears = experienceYears or 0

# Role subclasses
class teacher(Staff):
    def __init__(self, role="Teacher", salary="63,000", hoursWorkedWeek=40, experienceYears=0, homeroom=None, subject=None, **kwargs):
        super().__init__(role, salary, hoursWorkedWeek, experienceYears, **kwargs)
        self.homeroom = homeroom
        self.subject = subject or "General"

    def teach(self, topic=None, duration_minutes=45):
        """Simulate teaching a topic.

        - topic: optional topic string
        - duration_minutes: approximate class length
        Returns a short summary string.
        """
        topic = topic or f"{self.subject} lesson"
        msg = f"{self.name} (role={self.role}) teaches '{topic}' for {duration_minutes} minutes in {self.homeroom or 'their assigned room'}."
        print(msg)
        return msg

    def prepareLesson(self, topic=None):
        """Prepare materials for a lesson and return a brief status."""
        topic = topic or f"{self.subject}"
        msg = f"{self.name} prepares lesson materials for {topic}."
        print(msg)
        return msg

    def recordAttendance(self, students_list=None):
        """Record attendance for a list of student names.

        - students_list: optional list of names; if None, returns a template string.
        """
        if students_list is None:
            msg = f"{self.name} is ready to take attendance for {self.homeroom or 'the class'}."
            print(msg)
            return msg

        present = len(students_list)
        msg = f"{self.name} recorded attendance: {present} present ({', '.join(students_list)})."
        print(msg)
        return msg

    def getSalary(self):
        return self.salary

class principal(Staff):
    salary = "104,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Principal", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def sendAnnouncement(self):
        announcement = input("Enter announcement: ")
        return f"Announcement: {announcement}"

    def evaluateTeacher(self):
        return f"Teacher has been evaluated."

    def getSalary(self):
        return self.salary

class vicePrincipal(Staff):
    salary = "86,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Vice Principal", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

class custodian(Staff):
    salary = "30,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Custodian", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def cleanRoom(self):
        return f"{self.location} was cleaned."

    def resupplyRoom(self):
        return f"{self.location} was resupplied."

    def getSalary(self):
        return self.salary

class resourceOfficer(Staff):
    salary = "79,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Resource Officer", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

    def apprehend(self, location, name):
        return f"{name} has been apprehended."

    def search(self, location, name):
        return f"{name} has been searched."

class coach(Staff):
    salary = "43,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Coach", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

class it(Staff):
    salary = "54,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "IT", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

    def fixComputer(self):
        return f"{self.name} fixes a computer."

class nurse(Staff):
    salary = "67,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Nurse", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

    def checkHealth(self, name):
        return f"{name} had their health checked."

    def tendTo(self, name):
        return f"{name} has been tended to."

class guidanceCounsler(Staff):
    salary = "60,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Guidance Counselor", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

    def counsel(self, name=None):
        name = name or self.name
        return f"{name} has been counseled"

class secratary(Staff):
    salary = "55,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Secretary", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

    def greet(self):
        return f"Person greeted."

    def doClericalDuty(self):
        return f"Clerical duty done."

class cafetieriaWorker(Staff):
    salary = "30,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Cafeteria Worker", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

    def serveFood(self):
        return f"Lunch is served."

    def cleanCafetieria(self):
        return f"Cafetieria is cleaned."

    def assistStudent(self, name):
        return f"{name} assisted."
    
class librarian(Staff):
    salary = "69,000"
    def __init__(self, role=None, salary=None, hoursWorkedWeek=None, experienceYears=None, **kwargs):
        super().__init__(role or "Librarian", salary or self.salary, hoursWorkedWeek, experienceYears, **kwargs)

    def getSalary(self):
        return self.salary

    def checkOutBook(self):
        return f"Book checked out."

# Creates the roles
def createStaffRoles(role, salary, hoursWorkedWeek, experienceYears):
    mapping = {
        "Teacher": teacher,
        "Principal": principal,
        "Vice Principal": vicePrincipal,
        "Custodian": custodian,
        "Resource Officer": resourceOfficer,
        "Coach": coach,
        "IT": it,
        "Nurse": nurse,
        "Guidance Counsler": guidanceCounsler,
        "Cafetieria Worker": cafetieriaWorker,
        "Secratary": secratary,
        "Librarian": librarian,
    }

    return mapping[role](role, salary, hoursWorkedWeek, experienceYears)
