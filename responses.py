import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 6))
    
    if message == 'Are You ChatBot':
        return 'Yes I am'
    
    if message == 'Good':
        return 'Ty'
    
    if message == 'roll100':
        return str(random.randint(1, 100))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'

    return 'I didn\'t understand what you wrote. Try typing "!help".'