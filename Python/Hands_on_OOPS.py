class Students:
    Roll_no = 1
    Name = " " 
    Marks = " "

    def set_values(self, name1, marks1):
     self.Name = name1
     self.Marks = marks1

    def get_values(self):
        print(f"Student information: \nRoll no is: {self.Roll_no}\nName is: {self.Name} \nMarks are: {self.Marks}")

if __name__ == '__main__':
    student = Students()
    student.set_values(name1="Dipika", marks1=95)

student.get_values()
    
