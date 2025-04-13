class Clovek:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def pohybuje_se(self):
        pass

class Student(Clovek):
    def __init__(self, jmeno, vek, prospech):
        super().__init__(jmeno, vek)
        self.prospech = prospech

    def uceni_se(self):
        print(f"Student : {self.jmeno} se učí.Je mu {self.vek} a má prospěch {self.prospech}.")


student = Student("Jakub", 18, "vyznamenání")
student2 = Student("Tonda", 18, "propadl")

print(student.jmeno)
student.uceni_se()
student2.uceni_se()