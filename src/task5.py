import csv
import random

def PART2(n):

    with open(file='part2.csv', mode='r', encoding='utf-8-sig') as part2:
        question_list = []  # list of dict
        csvfile = csv.DictReader(part2)
        for row in csvfile:
            question_dict = {}
            question_dict['question'] = row['question']
            question_dict['option1'] = row['option1']
            question_dict['option2'] = row['option2']
            question_dict['answer'] = row['answer']
            question_dict['info'] = row['info']

            question_list.append(question_dict)

    random_num = random.choices(range(30), k = n)

    final_question = []
    for num in random_num:
        final_question.append(question_list[num])
    
    return final_question

# print(PART2(5))