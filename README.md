# Elijah

# School Project — Student Schedule Simulator

A small Python simulation that models a school's daily activity: students moving through schedules, teachers and staff occupying rooms, and simple period/lunch logic. The codebase contains actor classes (students/staff), environment rooms, utilities to generate sample data, and a simulator that runs a day for all students.

## Diagram Layout (LucidChart UML)

- School Activity Diagram — Activity diagram showing the main flows for a typical school day (student movement between rooms, period transitions, and lunch flows).
- School Actor Diagram 2 — UML actor/class diagram showing primary actors (Student, Staff, Teacher) and their relationships used by the simulator.
- School Actor Diagram — Earlier actor/class diagram.
- School Overview — Overview of school components and data flows.

## Key features

- Simulate students moving through a daily schedule with period and lunch handling.
- Staff roles with role-guarded methods (Teacher, Principal, Custodian, Nurse, etc.).
- Room objects that keep track of present actors and an assigned teacher.
- Small utility helpers to generate sample students, teachers, staff, and rooms.

## Repository layout

Top-level (relevant files and folders):

- `src/`
- `main.py` — (entry point; see below)  
- `StudentScheduleSimulator.py` — simulation driver for moving students through schedules and running periods/lunch.  
- `Utility.py` — helper functions to generate students, teachers, rooms and custom exceptions.  
- `Actors/Actor_Main.py` — base actor class (common fields/methods).  
- `Actors/Student.py` — Student actor, schedule handling.  
- `Actors/Staff.py` — Staff actor with role-specific methods and salary calculation.  
- `Data/Rooms.py` — list of room names used by the simulator.  
- `Data/Classes.py` — list of class short-names (Math, Science, etc.).  
- `Enviroment/Room.py` — Room class that tracks actors and teacher.

## Requirements

- Python 3.8+ (3.10 recommended).  
- The `names` package is used to generate realistic person names. Install with pip:

```bash
pip install names
```

You can also pin dependencies to a `requirements.txt` file if you wish; this project currently only requires `names` beyond the Python stdlib.

## Quick start

1. Install dependency:

```bash
pip install names
```

2.Run the (example) entry point. From the repository root:

```bash
python3 src/main.py
```

If `src/main.py` is not present or you want to exercise the simulator directly, you can create a short script like:

```python
import asyncio
from src.StudentScheduleSimulator import StudentScheduleSimulator
from src.Utility import generate_student, generate_teacher, generate_other_staff, generate_rooms

students = generate_student(10)
teachers = generate_teacher()
other_staff = generate_other_staff()

sim = StudentScheduleSimulator(students=students, staff=teachers + other_staff, period_length_seconds=1)

asyncio.run(sim.run_daily_simulation())
```

The utilities (`Utility.generate_student`, `generate_teacher`, `generate_other_staff`, `generate_rooms`) make it easy to build demo data.

## Important implementation notes

- Staff methods are guarded by role checks and raise `Utility.DeniedRoleMethod` if called by an inappropriate role.  
- `Actor_Main` provides common fields: id, name, email, location, and a `Goto()` method to move actors between rooms.  
- `Room` objects accept an optional `teacher` at creation; the teacher is automatically added to the room's actor list if provided.  

## License

This repository includes a `LICENSE` file — see it for license details.
