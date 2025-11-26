class Student:
  def lessons_schedule(self):
    with open('schedule.txt', 'r') as file:
      schedule = file.read()
      print(schedule)

  def average_grade(self):
    with open('grades.txt', 'r') as file:
      grades = file.read()

      grades_list = []

      tmp = ''

      for i in grades:
          if i.isdigit():
              tmp += i  
          else:
              if tmp:
                  grades_list.append(int(tmp))
                  tmp = ''

      if tmp:
          grades_list.append(int(tmp))

      total = 0

      for i in grades_list:
        total += i

      average = 0
      average = total / len(grades_list)
      print(average)
      return average


student = Student()
student.lessons_schedule()
print("=================================")


class Stipendia(Student):
  def if_stipendia(self, average):
    max = 12
    base = 1000
    coefficient = average / max
    average = 0

    stipendia = base * coefficient

    print(stipendia)


