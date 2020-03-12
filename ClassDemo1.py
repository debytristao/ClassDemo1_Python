#Demo working with OOP in Python
from pip._vendor.distlib.compat import raw_input


class Student:
    __doc__ = """
        Student Class
    """

    Name = ''
    Term = 0
    Grades = [0,0,0,0]

    def __init__(self, Name, Term):
        __doc__ = """
            Instantiate the Student Class
            Parameters
            Name: String with student Name
            Term: Integer with the term (1 to 9)
        """
        self.Name = Name
        self.Term = Term

    def get_name(self):
        __doc__ = """
            This function return a string with the student name
        """
        return self.Name

    def get_grades(self, Term, Grades):
        __doc__ = """
            This function will get the grade 
            Parameters
            Term: Integer between 1 to 4
            Grade: Float between 0 to 10
        """
        self.Grades[Term] = Grades

    def calculate_average(self):
        __doc__ = """
            This function get the averaga and reutn a float
        """
        Grades = 0
        Average = 0
        i = 0
        while (i < 4):
            Grades += self.Grades[i]
            i += 1
        Average = Grades / 4
        return Average


# Start the application
name = str(raw_input("Enter the student Name: "))
term = int(raw_input("Term: "))
student = Student(Name=name, Term=term)

i = 0

while (i < 4):
    grade = float(raw_input("Enter the %sª grade: " % str(i+1)))
    student.get_grades(Term=i, Grades=grade)
    i += 1

print("The student %s finished o term with an average %f" % (student.get_name(),student.calculate_average()))