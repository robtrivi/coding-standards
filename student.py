class Student:
    """Represents a student and their grades."""

    def __init__(self, student_id: str, name: str) -> None:
        self.id = student_id
        self.name = name
        self.grades: list[float] = []
        self.is_passed: bool = False
        self.honor: bool = False

    def add_grade(self, grade: float) -> None:
        """Add a grade to the student's record."""
        try:
            grade_value = float(grade)
        except (ValueError, TypeError):
            raise ValueError("Grade must be a number") from None
        self.grades.append(grade_value)

    def calculate_average(self) -> float:
        """Calculate and return the average grade."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def check_honor(self) -> None:
        """Set honor status if average is above 90."""
        self.honor = self.calculate_average() > 90

    def delete_grade(self, index: int) -> None:
        """Delete a grade by index."""
        try:
            del self.grades[index]
        except IndexError:
            raise IndexError("Grade index out of range") from None

    def report(self) -> None:
        """Print a report of the student's information."""
        average = self.calculate_average()
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average Grade: {average:.2f}")
        print(f"Honor Roll: {'Yes' if self.honor else 'No'}")


def main() -> None:
    """Demonstrate Student class functionality."""
    student_instance = Student("X123", "John Doe")
    student_instance.add_grade(100)
    student_instance.add_grade(50)
    student_instance.check_honor()
    try:
        student_instance.delete_grade(5)
    except IndexError as error:
        print(error)
    student_instance.report()


if __name__ == "__main__":
    main()
