import json
import random
import time
import os

'''

-------------------------------------------------------------------------------

Name:  main.py

Purpose: A adventure game that involves answers questions about topic we learned this year

Author:   John Szewczyk

Created:  09/05/2023

------------------------------------------------------------------------------
'''


user_status = ""
business_bucks = 40
score = 0
has_double_score = False
has_ability_two = False
has_ability_three = False
item_1_cost = 10
item_2_cost = 20
item_3_cost = 30
incorrect_questions = []


class question():
    # Opens Json file
    question_list = open('misc_data.json')
    data = json.load(question_list)
    chosen_question = ""
    question = ""
    question_giver = ""
    score_gain = 0
    business_buck_gain = 0

    def randomize(self):
        self.chosen_question = random.randint(0, len(self.data["questions"]) - 1)
        chosen_question = self.chosen_question
        self.question = self.data["questions"][chosen_question]
        self.question_giver = self.data["question_givers"][random.randint(0, len(self.data["question_givers"]) - 1)]
        self.score_gain = random.randrange(10, 100, 10)
        self.business_buck_gain = random.randint(1,10)
    # Randomly assigns question and question giver to class



def clear_console():
    # TODO - John take a look at this, Alex
    #  https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    # print(chr(27) + "[2J")
    # Thanks for help - John
    os.system('cls' if os.name == "nt" else 'clear')


def open_store():
    global business_bucks
    global has_double_score
    global has_ability_two
    global has_ability_three
    global item_1_cost
    global item_2_cost
    global item_3_cost
    clear_console()
    purchase_status = ""
    print("LOCATION: STORE")
    while purchase_status != "/e":
        purchase_status = input(f"What would you like to buy, you currently have {business_bucks} business bucks ("
                                f"enter /e to exit): \n 1: Double score {item_1_cost}$ \n 2: Ability two {item_2_cost}$"
                                f"\n 3: Ability three {item_3_cost}$ \n")
        if purchase_status == "1" and business_bucks >= item_1_cost:
            has_double_score = True
            business_bucks = business_bucks - item_1_cost
            print("Bought double points!")

        elif purchase_status == "2" and business_bucks >= item_2_cost:
            has_ability_two = True
            business_bucks = business_bucks - item_2_cost
            print("Bought ability two!")

        elif purchase_status == "3" and business_bucks >= item_3_cost:
            has_ability_three = True
            business_bucks = business_bucks - item_3_cost
            print("Bought ability three!")
        elif purchase_status == "/e":
            print("Goodbye")
        else:
            print("Enter a valid option")

        time.sleep(1)
        clear_console()

    clear_console()


def request_question():
    global has_double_score
    global score
    global business_bucks
    global incorrect_questions
    question_list = open('misc_data.json')
    data = json.load(question_list)
    print("What is your desired location")
    for i in range(len(data["locations"])):
        print(f"{i + 1}) {data['locations'][i]}")
    desired_location = input()
    desired_location = data["locations"][int(desired_location) - 1]



    clear_console()
    new_question = question
    question.randomize(question)
    print(f"LOCATION: {desired_location}")
    print(f"{question.question_giver} has a question for you")
    print(question.question["contents"])
    for i in range(len(question.question["choices"])):
        print(f"{i + 1}) {question.question['choices'][i]}")
    choice = int(input())
    if question.question['choices'][choice - 1] == question.question['correct'][0]:
        if has_double_score == True:
            question.score_gain = question.score_gain * 2
            question.business_buck_gain = question.business_buck_gain * 2
            has_double_score = False
        print(f'Correct! +{question.score_gain} score and +{question.business_buck_gain} business bucks')
        score += question.score_gain
        business_bucks += question.business_buck_gain
        time.sleep(2)
    else:
        print(f"Sorry, That was not correct. The correct answer was {question.question['correct'][0]} \n (Press ENTER to continue)")
        index = question.chosen_question
        incorrect_questions.append(index)
        input()
    clear_console()


def answer_key():
    clear_console()
    questions = open("misc_data.json")
    data = json.load(questions)
    data = data["questions"]
    for i in range(len(data) - 1):

        print(data[i]["contents"])
        for x in range(len(data[i]["choices"])):
            print(f"{x + 1}) {data[i]['choices'][x]}")
        print(f"Answer: {data[i]['correct'][0]}\n")
    input()


def prev_wrong():
    clear_console()
    global incorrect_questions
    buff = []
    questions = open("misc_data.json")
    data = json.load(questions)
    data = data["questions"]
    if len(incorrect_questions) == 0:
        print("Congrats! So far you have gotten no questions wrong!")
    else:
        buff.append(incorrect_questions[0])
        for i in range(1, len(incorrect_questions)):
            if buff.count(incorrect_questions[i]) == 0:
                buff.append(incorrect_questions[i])
        for i in buff:
            print(f'''--> You got "{data[i]['contents']}" with the correct choice being "{data[i]['correct'][0]}" wrong {incorrect_questions.count(i)} time/s\n''')
    input()
    clear_console()






print("COMPUTER STUDIES GAME".center(50, "-"),"\n"," ICS201a".center(43, " "), "\n", "Due Date".center(44," "), "\n", "John Szewczyk".center(44, " "))

time.sleep(3)

clear_console()


print("Welcome to the computer science game.\n"
      "Your objective is to get your score as high as possible while collecting \n"
      "business bucks so you can buy new items.\n"
      "You obtain business bucks and points by completing questions and \n"
      "answering them correctly.")

time.sleep(5)

clear_console()

print("LOCATION: HUB")
print("Welcome to your hub, here you can type /l to change your location, /b to open your shop,\n /a for the answer key, /w for questions you previously got wrong, and /q to quit your game.")
time.sleep(4)


while user_status != "/q":
    print("LOCATION: HUB")
    user_status = input("Enter your desired command hub command (/h for command list): ")

    if user_status == "/l":
        request_question()
    elif user_status == "/b":
        open_store()
    elif user_status == "/a":
        answer_key()
    elif user_status == "/w":
        prev_wrong()
    elif user_status == "/q":
        pass
    elif user_status == "/h":
        clear_console()
        print("/l to change your location\n/b to open your shop\n/a for the answer key\n/w for questions you previously got wrong\n/q to quit your game")
    else:
        print("Error, please enter a valid command")
        time.sleep(0.5)

print("Thanks for playing!")