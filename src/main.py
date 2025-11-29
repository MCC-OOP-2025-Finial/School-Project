import StudentScheduleSimulator as sim
from Utility import TooManyStudentsError
from Utility import generate_student, generate_teacher
import asyncio

if __name__ == "__main__":
    async def simulate():
        NumberOfStudents = input("Enter number of students to simulate: ")
        try:
            num_students = int(NumberOfStudents)
            if num_students <= 0:
                raise TooManyStudentsError("Number of students must be positive", 0)
            elif num_students > 100:
                raise TooManyStudentsError("Exceeded maximum number of students", 100)
        except ValueError:
            print("Invalid input. Please enter a valid integer for number of students.")
        except TooManyStudentsError as e:
            print(e)    
        else:
            PeriodLength = input("Enter period length in seconds (default 1 = 1 sim hour): ")
            input("Press Enter to start the simulation...")
            print(f"Simulating with {num_students} students...")
            students = generate_student(num_students)
            teachers = generate_teacher()
            period_length = int(PeriodLength) if PeriodLength.isdigit() else 1
            sim_instance = sim.StudentScheduleSimulator(students, teachers, period_length_seconds=period_length)
            await sim_instance.run_daily_simulation()


    asyncio.run(simulate())