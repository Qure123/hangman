from time import sleep
from random import choice
x = open('C:\\Users\\user\\Desktop\\проекты Аллочки заечки\\words.txt', encoding = 'UTF-8') 
quized_w = (choice(x.readlines()).strip()).upper()
x.close()
def display_hangman(tries):
    stages = [# финальное состояние: голова, торс, обе руки, обе ноги - 0
'''
______________________
|                     |\\  
|     +----+          |_\\
|     |    |             |
|     |    Ọ             |
|     |   /Ť\\           |
|     |  ዖ Ѿ የ           |
|     |    ⎭⎩           |
|     |                  |
|     +========+         |
|     +==========+       |
|                        |
|________________________|
''',
# голова, торс, обе руки, одна нога - 1
'''
______________________
|                     |\\  
|     +----+          |_\\
|     |    |             |
|     |    Ọ             |
|     |   /Ť\\           |
|     |  ዖ Ѿ የ           |
|     |    ⎭             |
|     |                  |
|     +========+         |
|     +==========+       |
|                        |
|________________________|
''',
#голова, торс, обе руки - 2
'''
______________________
|                     |\\  
|     +----+          |_\\
|     |    |             |
|     |    Ọ             |
|     |   /Ť\\           |
|     |  ዖ Ѿ የ           |
|     |                  |
|     |                  |
|     +========+         |
|     +==========+       |
|                        |
|________________________|
''',
#голова, торс и одна рука -3
'''
______________________
|                     |\\  
|     +----+          |_\\
|     |    |             |
|     |    Ọ             |
|     |   /Ť             |
|     |  ዖ Ѿ             |
|     |                  |
|     |                  |
|     +========+         |
|     +==========+       |
|                        |
|________________________|
''',
# голова, торс - 4
'''
______________________
|                     |\\  
|     +----+          |_\\
|     |    |             |
|     |    Ọ             |
|     |    Ť             |
|     |    Ѿ             |
|     |                  |
|     |                  |
|     +========+         |
|     +==========+       |
|                        |
|________________________|
''',
# голова - 5
'''
______________________
|                     |\\  
|     +----+          |_\\
|     |    |             |
|     |    Ọ             |
|     |                  |
|     |                  |
|     |                  |
|     |                  |
|     +========+         |
|     +==========+       |
|                        |
|________________________|
''',
# начальное состояние - 6
'''
______________________
|                     |\\  
|     +----+          |_\\
|     |    |             |
|     |                  |
|     |                  |
|     |                  |
|     |                  |
|     |                  |
|     +========+         |
|     +==========+       |
|                        |
|________________________|
'''
]
    return stages[tries]
def is_valid(y): #checking letters for validity
    while True:
        if len(y) == 1:
            if y in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-':
                return y
        elif len(y) > 2:
            for c in y:
                if y not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-':
                    break
        y = input('Не место для шуток, отвечай как велено. Если ты не понял, то буквы должны быть русскими: \n').upper()
        continue   
def play_word(word): #mechanic of  the game hangman
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Начнем игру!', word_completion, display_hangman(6), sep = '\n')
    while True:
        char  = is_valid(input(f'Назови букву или слово, коли осмелишься гадать. Подсказка: в некоторых словах присутствует дефис ("-").\nВот список букв, что ты уже использовал - {guessed_letters}:\n').upper())
        if len(char) == 1:
            if char not in guessed_letters:
                if char in word:
                    for c in range(len(word)):
                        if word[c] == char:
                            word_completion = word_completion[:c] + char + word_completion[c+1:]
                            if word.count(char) == 1:
                                break   
                    if word_completion == word:
                        return (print('Я надеялся, что сегодня ты поплатишься за свое пьянство...мы еще обязательно встретимся', 
                                                                        word, display_hangman(tries), sep = '\n'))
                    guessed_letters.append(char)
                    print('Какая жалость, ты угадал букву. Надеюсь, тебе больше везти не будет', 
                                            word_completion, display_hangman(tries), sep = '\n')
                    sleep(1)
                    print()
                else:
                    tries -= 1
                    if tries == 0:
                        break
                    guessed_letters.append(char)
                    print(f'Ты на один шаг ближе к проигрышу, поздравляю. У тебя осталось {tries} попыток', word_completion, guessed_letters,
                                                        display_hangman(tries), sep = '\n')
            else:
                print('Ты уже называл эту букву, у тебя память как у рыбки? Напомню тебе буквы, что ты уже называл',
                                                                                            guessed_letters, sep = '\n')
                sleep(1)
                print()
        elif char == word:
            return (print('Я надеялся, что сегодня ты поплатишься за свое пьянство...мы еще обязательно встретимся', 
                                                                        word, display_hangman(tries), sep = '\n'))
        else:
            tries -= 1
            if tries == 0:
                break
            guessed_words.append(char)
            print('Неверное слово', guessed_words, display_hangman(tries), sep = '\n')
    print(f'Ты проиграл. Если тебе интересно, то загаданное слово: {word}')
    sleep(2)
    print(display_hangman(tries))
print("\x1B[3m"+'вы просыпаетесь в незнакомом месте — вы сидите за столом со связанными руками. \nнад вами лишь один источник света - старый прикоптелый медный фонарь. \nон медленно раскачивается, создавая тем самым устрашающий звук, от которого все опускается внутри \nчувствуете, как ужасно сильно болит ваша спина; все-таки стул — не лучшее место для сна'+"\x1B[0m")
sleep(10)
print()
print("\x1B[3m"+'появляется закономерный вопрос — каким образом вы вчера умудрились напиться до чертиков, завалиться к кому-то "домой", \nесли это место можно назвать домом. вы пытаетесь разглядеть вашу спальню на сегодня, но жалкий фонарный свет \nедва ли позволяет заглянуть дальше вашего носа. cудя по темноте и эху, вы находитесь либо в ангаре, \nлибо в пристанище одинокого вампира, предпочитающего кровь пьяниц - одно из двух.'+"\x1B[0m")
sleep(10)
print()
print("\x1B[3m"+'возникло чувство огромной усталости от бытия — давно же вы не находились так долго в трезвом состоянии. \nцарство морфея не собирается вас отпускать'+"\x1B[0m")
sleep(5)
print("\x1B[3m"+'вдруг вы слышите голос'+"\x1B[0m")
sleep(3)
print()
print('- Грешник, сейчас тебе предстоит сыграть в игру: победишь - уйдешь живым; проиграешь - ответишь за грехи.')
sleep(2)
print('В чем суть: я загадываю слово на русском, ты его угадываешь, буква за буквой.')
sleep(3)
print('Также рисуется виселица. Назвал букву, которой нет в слове - постепенно, конечность за конечностью, \nрисуется висельник - по части тела за каждую ошибку.\nНазвал букву верно - все ее повторения в слове откроются. Всего у тебя 6 возможностей ошибиться')
sleep(5)
print()
print('- Угадываешь слово - твоя жалкая душонка в безопасности; проигрываешь.. а потом сам все узнаешь.')
sleep(1)
print()
play_word(quized_w)