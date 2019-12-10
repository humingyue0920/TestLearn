def print_student_file(name, age=7, sex='男', college='人民小学'):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')
    print('我是'+sex+'生')
    print('我在'+college+'上学')

print_student_file('小张')
print('------------------')
# 只改变年龄
print_student_file('小胡', age=6)
# 改变年龄和性别,并且不按照默认顺序传递,是否可行,实验证明不可行
# print_student_file('小胡', '女', 7)
print('------------------')
print_student_file('小胡', 7, '女',)
print('------------------')
print_student_file('小胡', 7, sex='女',)
# print_student_file('小胡', age=7, '女', college = '光明小学')  代码报错,因为在调用时同样不能非默认参数在默认参数后面




