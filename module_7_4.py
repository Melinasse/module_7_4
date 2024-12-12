# Оператор %

team1_num = 5 #Мастера кода
team2_num = 6 #Волшебники данных
print('В команде Мастера кода участников %s!' % team1_num)
print('Итого сегодня в командах участников %s и %s!' %(team1_num, team2_num))

# Оператор .format()
score_1 = 40
score_2 = 42
print('Команда Волшебники данных решила задач:{}'.format(score_2))
team1_time = 1552.512
team2_time = 2153.31451
# print('Волшебники данных решили задачи за {:.1f}с!'.format(team1_time))
print('Волшебники данных решили задачи за {0}с!'.format('1552.512'))

# f-строки
print(f'Команды решили: {score_1} и {score_2} задачи.')

def challenge_result(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    print(f'Результат битвы: {result}')

challenge_result(score_1, score_2, team1_time, team2_time)


all_score = [score_1, score_2]
task_total = sum(all_score)
# print(task_total)
all_time = [team1_time, team2_time]
time_avg = sum(all_time) / len(all_time)
# print(all_time)
print(f'Сегодня было решено {task_total} задачи, в среднем по {time_avg} секунды на задачу!')