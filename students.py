#question1.py
#By Gregory Cave (master programmer)
#On the 24th of November 2015

#function that displays the menu
def menu():
      print("\n\n*********MENU*********")
      print("1. Input data and save to a new, or already existing file.")
      print("2. Calculate and display average mark.")
      print("3. Display data.")
      print("4. Exit.")
      print("*********MENU*********")
      choice=input("\nEnter choice: ")
      return choice

def main():
    choice=menu()
    while choice!=4:
            if choice=='1':
                  saveToFile()
            elif choice=='2':
                  calculateAverage()
            elif choice=='3':
                  displayData()
            elif choice=='4':
                  Name=input("Enter the student's name (XXX) to end program: ")
                  if studentName=="XXX":
                        print("Good Bye")
                        break
                  else:
                        studentMark=input("Enter {0}'s test score: ".format(studentName))
                        studentRecords=[studentName,studentMark]
                        with open("testResultsFile.txt", mode="a",encoding="utf-8") as my_file:
                              for each in studentRecords:
                                    my_file.write(each+"\n")
            else:
                  print("Incorrect input, returning to menu.")
                  main()

def calculateAverage():
      total=0
      student_scores=[]
      with open("testResultsFile.txt", mode="r", encoding="utf-8") as myFile:
            students=myFile.read().splitlines()
            last_student=students[-1]
            last_position=students.index(last_student)
            counter=2
            while counter!=last_position:
                  each_student=students[counter]
                  student_scores.append(each_student)
                  counter=counter+2
            student_scores.append(last_student)
            for each in student_scores:
                  each=int(each)
                  total=total+each
            scores_length=len(student_scores)
            total=total/scores_length
            print(total)
            main()


def displayData():
      with open("testResultsFile.txt", mode="r", encoding="utf-8") as myFile:
        for eachLine in myFile:
            print(eachLine.rstrip("\n"))
      main()

def saveToFile():
    end=False
    while end!=True:
          studentName=input("Enter the student's name (XXX) to end program: ")
          if studentName=="XXX":
                end=False
                main()
          else:
                studentMark=input("Enter {0}'s test score: ".format(studentName))
                studentRecords=[studentName,studentMark]
                with open("testResultsFile.txt", mode="a",encoding="utf-8") as my_file:
                    for each in studentRecords:
                        my_file.write(each+"\n")

def calculateAverage():
      total=0
      student_scores=[]
      with open("testResultsFile.txt", mode="r", encoding="utf-8") as myFile:
            students=myFile.read().splitlines()
            last_student=students[-1]
            last_position=students.index(last_student)
            counter=2
            while counter!=last_position:
                  each_student=students[counter]
                  student_scores.append(each_student)
                  counter=counter+2
            student_scores.append(last_student)
            for each in student_scores:
                  each=int(each)
                  total=total+each
            scores_length=len(student_scores)
            total=total/scores_length
            print(total)
            main()


def displayData():
      with open("testResultsFile.txt", mode="r", encoding="utf-8") as myFile:
        for eachLine in myFile:
            print(eachLine.rstrip("\n"))
      main()
    
main()
