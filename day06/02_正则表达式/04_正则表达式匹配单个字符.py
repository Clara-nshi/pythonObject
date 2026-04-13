import re


# 提前定义一个函数用于提取结果
def get_data(result):
    if result:
        print(f'匹配成功, {result.group()}')
    else:
        print('匹配失败')


# . :匹配任意 1 个字符（除了 \n）
# 宁可少，不能多
result = re.match('.', '1Aa_中')
result = re.match('.....', '1Aa_中')
get_data(result)
# [x] : 匹配括号中任意 1 个字符，最后结果只有 1 个
result1 = re.match('[cbaasdas][naskdjl][iabsda]', 'clara')
get_data(result1)
result2 = re.match('[a-z][0-9]', 'c0809')
get_data(result2)
# [^x] : 匹配括号中除了 x 之外的任意字符
result3 = re.match('[^a]', 'claibe')
get_data(result3)
