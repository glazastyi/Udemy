def logging(fn):
    def realisation(self):
        print("\nThis feature is only available to teachers, please log in")
        login = input("Login: ")
        password = input("Password: ")
        if login == self.login and password == self.password:
            print("\nSuccess!\n")
            fn(self)
        else:
            print("\nFailed!\n")

    return realisation


class GradingSystem(object):
    def __init__(self):
        self.login = str(input("Please set a login for teacher: "))
        self.password = str(input("Please set a password for teacher: "))
        self.flag = 1
        self.grade_system = {}
        self.func_dictionary = {1: self.enter_grades,
                                2: self.remove_student,
                                3: self.get_student_average_grades,
                                4: self.exit}

    def run(self):
        while self.flag:
            key = int(input("Welcome to Grade Central"
                            "\n\t[1] - Enter grades"
                            "\n\t[2] - Remove Student"
                            "\n\t[3] - Student average grades"
                            "\n\t[4] - Exit "
                            "\nWhat would you like to do today?"))

            if key <= 0 or key > 4:
                print("It seems you are sealed up. \n"
                      "You must enter a number between 1 and 4\n")
            else:
                self.func_dictionary[key]()

    @logging
    def enter_grades(self):
        student = input("Student name: ")
        grade = input("Student grade: ")
        print("Adding grade...")
        if self.grade_system.get(student) is None:
            self.grade_system[student] = []
        self.grade_system[student].append(int(grade))
        print(self.grade_system)

    @logging
    def remove_student(self):
        student = input("What student to remove?: ")
        if student not in self.grade_system.keys():
            print("This student is not in the system")
        else:
            print("Removing student...")
            self.grade_system.pop(student)
            print(self.grade_system)

    def get_student_average_grades(self):
        if len(self.grade_system):
            print("Student average grades:")
            for student in self.grade_system.keys():
                scores = self.grade_system[student]
                print("{}: {}\n".format(student, float(sum(scores)) /
                                        len(scores)))
        else:
            print("\nNo students!\n")

    def exit(self):
        print("Goodbue!")
        self.flag = 0


project = GradingSystem()
project.run()
