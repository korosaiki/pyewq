# 有一个学校，8个老师随机分配工位三个办公室，
school = [[],[],[]]

def create_teachername():


    teacher_list = []
    i = 1
    while i < 9:
        teacher_name = '老师' + str(i)
        teacher_list.append(teacher_name)
        i += 1
    return teacher_list

teachers = create_teachername()
print(teachers)