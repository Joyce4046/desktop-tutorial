import csv

# 讀取問題存進dict
file = "C:\\Users\\sherry liu\\Desktop\\sherry\\大四下\\python\\question_part1.csv"
filesopen = open(file, 'r', newline='')
rows = csv.reader(filesopen)
question_dict = dict()
for row in rows:
    question_dict[int(row[0])] = row[1:]

# 讀取貓咪資料存進dict
file1 = "C:\\Users\\sherry liu\\Desktop\\sherry\\大四下\\python\\貓咪.csv"
filesopen = open(file1, 'r', newline='')
rows = csv.reader(filesopen)
cat_dict = dict()
for row in rows:
    cat_dict[int(row[0])] = row[1:]

# print(question_dict)
# print(cat_dict)
    

def get_question(question_dict, q_id, color_list):
    '''取出問題及答案文字'''
    if q_id <= 12:
        q_content = question_dict[q_id][0]
        ans_1 = question_dict[q_id][1]
        ans_2 = question_dict[q_id][2]
    else:
        if q_id == 13:
            q_content = question_dict[q_id][0]+color_list[0]+"還是"+color_list[1]+"？"
            ans_1 = color_list[0]
            ans_2 = color_list[1]
        elif q_id == 14:
            q_content = question_dict[q_id][0]+color_list[1]+"還是"+color_list[2]+"？"
            ans_1 = color_list[1]
            ans_2 = color_list[2]
        else:
            q_content = question_dict[q_id][0]+color_list[0]+"還是"+color_list[2]+"？"
            ans_1 = color_list[0]
            ans_2 = color_list[2]
    return q_content, ans_1, ans_2

def click_ans1(question_dict, q_id):
    '''按第一個鈕'''
    ans = question_dict[q_id][6]
    adjust_type = question_dict[q_id][5]
    next_q_id = question_dict[q_id][3]
    
    return ans, adjust_type, next_q_id

def click_ans2(question_dict, q_id):
    '''按第二個鈕'''
    ans = question_dict[q_id][7]
    adjust_type = question_dict[q_id][5]
    next_q_id = question_dict[q_id][4]
    return ans, adjust_type, next_q_id


# 創建貓咪分數字典
cat_score = {}
for cat_id in cat_dict.keys():
    cat_score[int(cat_id)] = 60 # 分數60起跳    
    
def calculate_score(question_dict, cat_dict, cat_score, q_id, ans, adjust_type):
    '''計算分數加減並更新'''
    if q_id <= 9:
        for cat_id in cat_score.keys():
            if ans == cat_dict[cat_id][int(adjust_type)]:
                cat_score[cat_id] += int(question_dict[q_id][8])
            else:
                cat_score[cat_id] += int(question_dict[q_id][9])
    else:
        for cat_id in cat_score.keys():
            if ans == cat_dict[cat_id][int(adjust_type)]:
                cat_score[cat_id] += 2
    return cat_score

def get_3_cat(cat_score):
    '''找分數前三高貓咪'''
    max_id_all = []
    for i in range(3):
        max = -1
        max_id = []
        for cat_id in cat_score:
            if cat_score[cat_id] > max:
                max_id = []
                max = cat_score[cat_id]
                max_id.append(cat_id)
            elif cat_score[cat_id] == max:
                max_id.append(cat_id)
            else:
                pass
        for id in max_id:
            max_id_all.append(id)
        if len(max_id_all)>3:
            break
    return(max_id_all)
    
q_id = 1
next_q_id = 1
color_list = []
while q_id != 0:
    q_content, ans_1, ans_2 = get_question(question_dict, q_id, color_list)
    ans, adjust_type, next_q_id = click_ans2(question_dict, q_id)
    cat_score = calculate_score(question_dict, cat_dict, cat_score, q_id, ans, adjust_type)
    q_id = int(next_q_id)
    print(q_content)
    if q_id >= 11:
        if q_id <= 13:
            color_list.append(ans_1)

print(cat_score)

max_id_all = get_3_cat(cat_score)
print(max_id_all)
