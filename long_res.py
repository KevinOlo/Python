import random

yo = 'whhhhaaaattttt'
pyans = 'Learning Python is great! '
libcar = 'Having fun is never hard, when you have a library card '
bball = ' hey personally I dont care what anyone says, LeBron is the Greatest of all Time in Basketball'
fball = ' Did you know Steelers fans wave their terrible towels at football games? '

r_eat = "I don't like eating anything because I'm a bot obviously!"
r_advice = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown():
    response = ['could you please say that again',
    '...', 
    'what does that mean', 
    'not getting ya'][random.randrange(0,4)]

    return response
    