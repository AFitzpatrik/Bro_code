class Clovek:
    def __init__(self, jmeno, vek, vaha):
        self.jmeno = jmeno
        self.vek = vek
        self.vaha = vaha

    def pohybuje_se(self):
        pass

class Student(Clovek):
    def __init__(self,jmeno, vek, vaha, prospech):
        super().__init__(jmeno, vek, vaha)
        self.prospech = prospech

    def uceni_se(self):
        print(f"Student : {self.jmeno} se učí.Je mu {self.vek}, váží {self.vaha} a má prospěch {self.prospech}.")




student = Student("Petr", 20, 80, "výborný")
student2 = Student("Eva", 22, 60, "dobrý")
student.uceni_se()
student2.uceni_se()
