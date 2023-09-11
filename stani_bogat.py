import random

print('<<<---Добре дошли в Стани Богат--->>>\n')
questions = ['Кога е основана България?', 'Колко е 2 * 2?', 'Коя е най-голямата държава по площ в света?']
questions_asked = []
guess_question_counter = 0
wrong_question_counter = 0

for _ in range(10):
    question = random.choice(questions)

    if question not in questions_asked:
        print(f'{question}')
    else:
        continue

    if question == 'Кога е основана България?':
        user_answer = input('Въведете отговора: ')

        if user_answer == '681':
            print('Ти позна!!!\n')
            guess_question_counter += 1
            questions_asked.append(question)
        else:
            wrong_question_counter += 1
            print('Грешен отговор\n')

    elif question == 'Колко е 2 * 2?':
        user_answer = input('Въведете отговора: ')

        if user_answer == '4':
            print('Ти позна!!!\n')
            guess_question_counter += 1
            questions_asked.append(question)
        else:
            wrong_question_counter += 1
            print('Грешен отговор\n')

    elif question == 'Коя е най-голямата държава по площ в света?':
        user_answer = input('Въведете отговора: ')

        if user_answer == 'Русия':
            print('Ти позна!!!\n')
            guess_question_counter += 1
            questions_asked.append(question)
        else:
            wrong_question_counter += 1
            print('Грешен отговор\n')

    if guess_question_counter == 2:
        print('Ти спечели играта!')
        break

    if wrong_question_counter == 2:
        print('Ти загуби играта!!!')
        break