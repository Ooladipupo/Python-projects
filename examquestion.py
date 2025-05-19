### exam question and answer project
### we need to create a turpel of questions containinng 5 question (,,,,,)
### we also need to crate a 2 D dimentioanl answer option A,B,C,D for each question all within an option tuple
### we need to create a turple of the correct answer for the 5 questions
### finally a list of guesses picked by the examiner. we decided to use a list here cos it allows for duplication of characters 
# and is changeable unlike a tuple that is unchangeable. we will be appending our answer quess for each question to the guesses variable
### lets crate another score variable to keep track of our score starting from 0
###we would need to create another question_num variable to keep track of the question number we are on

#pseudocode
#we need a for loop to print out the questions one after the other
#----we need an inner for loop nested within the above outer for loop to print out the options wihich is a 2D. meaning the for loop need to have an index [question_num]
#----an index [question_num] has been created as a varaible earlier. the index needs to be incremented to move the inner for loop above to the next question. 
#--within the outer for loop, We nned an input for the examiner to enter the answer options (A OR B OR C OR D). This is creates as a variable guess
#--then append the guess answer to the guesses[] collector.

#--we need an if statement to increament the score. if the examiner guess == answers[]. also print the answer is CORRECT, else: print INCORRECT



questions = ("How many elemants are in a periodic table?:", 
             "Which animal lays the largest eggs?:", 
             "What is the most abundant gas in earcths atmosphere?:", 
             "How many bones are in the human body?:", 
             "Whcih planet in the solar system is the hottest?:")

options = (("A: 116", "B: 117", "C: 118", "D: 119"), 
           ("A: Whale", "B: Corcodile", "C: Elephant", "D: Ostrich"), 
           ("A: Nitrogen", "B: Oxygen", "C: carbon-Dioxide", "D: Hydrogen"), 
           ("A: 206", "B: 207", "C: 208", "D: 209"), 
           ("A: Mercury", "B: Venus", "C: Earth", "D: Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0  # created to serve as index for moveing to the next question



for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:      #options is a 2D collection, hence we need to add an index []. we already created a variable question_num for this
        print(option)

    guess = input("Enter option A or B or C or D as answer: ").upper()
    guesses.append(guess)   # append the guess response to the guessses collector

    if guess == answers[question_num]:  #if guess equal answers[index], then increase score by 1
        score +=1
        print("CORRECT Answer")
    else:
        print("INCORRECT")
        print(f"the correct answer is {answers[question_num]} ")
    question_num += 1                        # we needed to increament our index [question_num]. but before we increment, 
                                                #we need to ask the examiner to enter their enswer for the first question

print("------------------------------------")
print(f'your guesses are {guesses}')
print("------------------------------------")
print(f' the correct answers are {answers}')
print("------------------------------------")
print(score)
print("------------------------------------")
result = (score / 5) * 100
print(f'YOU SCORE IS {result}%')
print("------------------------------------")