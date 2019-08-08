print("Please enter your name, assignment 1 score, assignment 2 score, quiz score, and exam score using the following format:")
print("marks(" + '"name"' + ", ass1 (out of 10), ass2 (out of 30), quiz (out of 100), exam (out of 100)" + ")")

def marks(inputArray): #Marks function with inputArray set as the argument parameter
  inputArray = inputArray.split(",") #Splitting of inputArray with every comma

  name = str(inputArray[0]) #Name of student
  ass1 = int(inputArray[1]) #Assignment 1 out of 10 represented as 10%
  ass2 = int(inputArray[2]) #Assignment 2 out of 30 represented as 30%
  quiz = float(inputArray[3]) #Quizes out of 100 represented as 10%
  exam = float(inputArray[4]) #Exam out of 100
  finalMark = (ass1 + ass2 + quiz + exam) / 240 * 100 #Calculation of final mark

  quiz = quiz / 10
  
  if finalMark > 50: #If statement checking to see if the student received a passing mark
    print("['" + name + "', '" + str(ass1) + "', '" + str(ass2) + "', '" + str(quiz) + "', '" + str(exam) + "']")
    print(name + " has passed the course!")
    print("Assignment 1: " + str(ass1) + "/10")
    print("Assignment 2: " + str(ass2) + "/30")
    print("Quizzes: " + str(quiz) + "/10")
    print("Exam: " + str(exam) + "%")
    print("Final mark: "),
    print(round(finalMark, 1)),
    print("%")
    
  elif finalMark < 50: #Else statement checkign to see if the student received a failing mark
    print("['" + name + "', '" + str(ass1) + "', '" + str(ass2) + "', '" + str(quiz) + "', '" + str(exam) + "']")
    print(name + " has failed the course!!")
    print("Assignment 1: " + str(ass1) + "/10")
    print("Assignment 2: " + str(ass2) + "/30")
    print("Quizzes: " + str(quiz) + "/10")
    print("Exam: " + str(exam) + "%")
    print("Final mark: "),
    print(round(finalMark, 1)),
    print("%")