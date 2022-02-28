import random 
import sys
# MAGIC 8 BALL
print("Welcome to the Magic 8 ball!")
print("In this code, you can ask a question to the computer, and it will give you the answer!")
print("Then, the magic 8 ball will predict what happens!")
print("For example, you could say: Will I learn to code tomorrow? And then the 8 ball might say: 'I am almost perfectly sure.")
print("Lets get started!")
print("--------------------------------------------")
answer_list = ['I am almost perfectly sure.', 'I doubt it.', 'Ask again later.', 'You may rely on it.', 'Definitely', 'Outlook is not so good', 'Most likely']
def respond():
    global u_question
    u_question = str(input("What is the question you want to ask the ball?"))
    global ai_response
    ai_response = random.choice(answer_list)
    print("The Ball Says: ", ai_response)

respond()
sys.exit()