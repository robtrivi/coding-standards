"""
Module for managing student records and grades.
Provides functions to add grades, calculate averages, determine letter grades,
pass/fail status, and honor roll eligibility.
"""


class Student:
    """Represents a student and their grades."""

    def __init__(self, student_id: str, name: str) -> None:
        if not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not name.strip():
            raise ValueError("Student name cannot be empty.")
        self.id = student_id
        self.name = name
        self.grades: list[float] = []
        self.honor_roll: bool = False

    def add_grade(self, grade: float) -> None:
        """Add a numeric grade (0–100) to the student's record."""
        try:
            grade_value = float(grade)
        except (ValueError, TypeError):
            raise ValueError("Grade must be a numeric value.") from None
        if not 0 <= grade_value <= 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.grades.append(grade_value)

    def calculate_average(self) -> float:
        """Return the average of the student's grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self) -> str:
        """Convert the average grade to a letter grade."""
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"

    def is_passed(self) -> bool:
        """Return True if the student has passed (average >= 60)."""
        return self.calculate_average() >= 60

    def check_honor_roll(self) -> None:
        """Update the honor_roll flag based on average >= 90."""
        self.honor_roll = self.calculate_average() >= 90

    def remove_grade_by_index(self, index: int) -> None:
        """Remove a grade at the specified index."""
        try:
            del self.grades[index]
        except IndexError:
            raise IndexError("Grade index out of range.") from None

    def remove_grade_by_value(self, value: float) -> None:
        """Remove the first occurrence of the specified grade value."""
        try:
            self.grades.remove(float(value))
        except (ValueError, TypeError):
            raise ValueError("Grade value not found.") from None

    def summary_report(self) -> str:
        """Generate a formatted summary report for the student."""
        self.check_honor_roll()
        avg = self.calculate_average()
        letter = self.letter_grade()
        status = 'Passed' if self.is_passed() else 'Failed'
        honor = 'Yes' if self.honor_roll else 'No'

        report_lines = [
            '----- Student Summary -----',
            f"{'ID':<15}: {self.id:0>5}",
            f"{'Name':<15}: {self.name}",
            f"{'Grades Count':<15}: {len(self.grades):0>2}",
            f"{'Average Grade':<15}: {avg:0>6.2f}",
            f"{'Letter Grade':<15}: {letter}",
            f"{'Status':<15}: {status}",
            f"{'Honor Roll':<15}: {honor}",
            '----------------------------'
        ]
        return "".join(report_lines)


def main() -> None:
    """Demonstrate the Student class functionality."""
    student = Student("S001", "Alice")
    grades: list[float] = [95.0, 82.5, 77.0]
    for grade in grades:
        student.add_grade(grade)
    student.remove_grade_by_value(77.0)
    print(student.summary_report())


if __name__ == "__main__":
    main()
