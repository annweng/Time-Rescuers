from Questions import Question
# import question class
welcome = """                                         
                                                                                     ________________                     
                                                             _________        .---+++                +++---.              
                                                            :______.-':      :  .------------------------.  :             
                                                            | ______  |      | :                          : |             
                                                            |:______B:|      | |                          | |             
                                                            |:______B:|      | | WELCOME TO HOW MUCH DO   | |
                                                            |         |      | |   YOU KNOW(LOVE) Kirill：| |
                                                            |         |      | |                          | |
                                                            |         |      | | "A " to start the Quiz   | |                              
                                                            |:______B:|      | |                          | |             
                                                            |         |      | | "B "  to end the game    | |             
                                                            |:_____:  |      | |                          | |             
                                                            |    ==   |      | :                          : |             
                                                            |       O |      :  '------------------------'  :             
                                                            |       o |      :'---...________________...---'              
                                                            |       o |-._.-i___/'             \._              
                                                            |'-.____o_|   '-.   '-..._________________...-'  `-._          
                                                            :_________:      `.____________________   `-.___.-. 
                                                                             .'.eeeeeeeeeeeeeeeeeeeeeeeeeeee.'.      
                                                                           .'.eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.'.         
                                                                          :_______________________________________:
"""
time_clock = """


                                                                                   ___
                                                                           _______(_@_)_______
                                                                           | POLICE      BOX |
                                                                           |_________________|
                                                                            | _____ | _____ |
                                                                            | |###| | |###| |
                                                                            | |###| | |###| | 
                                                                            | _____ | _____ |
                                                                            | || || | || || |
                                                                            | ||_|| | ||_|| |
                                                                            | _____ |$_____ |
                                                                            | || || | || || |
                                                                            | ||_|| | ||_|| |
                                                                            | _____ | _____ |
                                                                            | || || | || || | 
                                                                            | ||_|| | ||_|| | 
                                                                            |       |       | 
                                                                            *****************
"""
# array of questions
questions_prompts = [
     "What is Kirill's preferred operating system? \n (a) Windows \n (b) Linux \n (c) I have no idea what an operating system is \n\n >> ",
     "Which does Kirill prefer, Star Wars or Star Trek? \n (a) Star Wars \n (b) Star Trek \n (c) They both horrible \n\n >> ",
     "Kirill's Favourite Music Genre? \n (a) Pop \n (b) Heavy metal \n（c) Classical \n\n >> ",
     "Does Kirill like pineapple on pizza? \n (a) Yes \n (b) No \n (c) maybe \n\n >> ",
     "What is Kirill's favourite movie? \n (a) Avengers Endgame \n (b) Shrek 2 \n (c) The Hunt of Red October \n\n >> ",
     "Is Kirill a cat or dog person? \n (a) cat \n (b) dog \n (c)neither \n\n >> ",
     "What's Kirill's ideal holiday trip? \n (a) Visit Friends in Bermuda Triangle \n (b) Visit Friends in Atlantis \n (c) Visit Friends in Russia \n\n >> ",
     "What's the one thing Kirill will NOT do in his first date \n (a) Dress up as Pikachu \n (b) Explaining what a variable means \n (c) Mention Star Trek in his conversation randomly \n\n >> ",
     "Does Kirill prefer restaurants or takeaway? \n (a) Restaurants \n (b) Takeaway \n (c) Hate both\n\n >> ",
     "Kirill: Are you going to fail your end of year exam? \n (a) Yes \n (b) No \n (c) Don't know \n\n >> "
]
# creating question objects
questions = [
     Question(questions_prompts[0], "b"),
     Question(questions_prompts[1], "b"),
     Question(questions_prompts[2], "c"),
     Question(questions_prompts[3], "b"),
     Question(questions_prompts[4], "c"),
     Question(questions_prompts[5], "b"),
     Question(questions_prompts[6], "c"),
     Question(questions_prompts[7], "c"),
     Question(questions_prompts[8], "a"),
     Question(questions_prompts[9], "a")

              
]
# asking if the user want to play the game
def start_game_intro():
     print(welcome)
     user_input = input("Your option? \n >> ").lower()
     while user_input not in ["a","b"]:
          print("invalid, please try again")
          user_input = input("Your option \n >> ")
     if user_input == "a":
          start_test(questions)
     elif user_input == "b": 
          exit() 

       
def start_test(questions):
# take the list of questions as the parameter
     score = 0
     #set score to 0
     for question in questions:
     # loop through the question array
          answer = input(question.prompt)
          while answer not in ["a", "b", "c"]:
          # verification
               print("Invalid input, please try again.")
               answer = input(question.prompt)
          # display questions in the array
          if answer == question.answer:
          #check the answer
               score += 1
               #increment score
     print("You got " + str(score) + "/" + str(len(questions)) + " correct. \n")
     #display result 
     if score < 6:
     #what happens when failed the test
          print("Kirill: You clearly have not watched my lectures properly, try again when you are ready. \n")
          try_again = input("Try again? (Y/N) \n >> ").lower()
          while try_again not in ["y","n"]:
          #validation 
               print("Invalid input.")
               try_again = input("Try again? (Y/N) \n >> ").lower()
          if try_again == "y":
               start_test(questions)
               #restart the quiz
          else:
               return
     else:
          print("Kirill: You have definitely paid attention in my lectures, well done.")
          print(time_clock)
          print("I can tell you are worthy of my friendship.")
          print("Feel free to use my time machine.")
          print("However, be careful, you will need a time specific password to get back to the present...!\n")
