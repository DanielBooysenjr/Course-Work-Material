from flask import Flask
import random

random_int = random.randint(1,9)
print(random_int)

app = Flask(__name__)

def text_decorator(function):
    def wrapper():
        return "<h1><b>" + function() + "</b></h>"
    return wrapper

def image_decorator(function):
    def wrapper():
        return function() + '<br><img style="display:inline; margin:auto;" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

    return wrapper

@app.route('/')
@image_decorator
@text_decorator
def hello_world():
    return 'Guess the number from 1-9'

@app.route('/<int:number>')
def number_guessed(number):
    if number < random_int:
        return "<h1 style='color: blue'> You can go Higher </h1>" \
                '<img src="https://media.giphy.com/media/D52PyP7vIl2vGrNFL1/giphy.gif">'
    elif number > random_int:
        return "<h1 style='color: red'> You can go Lower </h1>" \
                '<img src="https://media.giphy.com/media/azHp1od1Z3MGUjWDp0/giphy.gif">'
    elif number == random_int:
        return f"<h1 style='color: green'> You Found me! The number was: {number}</h1>" \
                '<img src="https://media.giphy.com/media/3oKHWeG1Z8lk1ap1nO/giphy.gif">'
      

if __name__ == "__main__":
    app.run(debug=True)