import re


# 提前定义一个函数用于提取结果
def get_data(result):
    if result:
        print(f'匹配成功, {result.group()}')
    else:
        print('匹配失败')


# TODO ^和$一般一起配合使用，限定要匹配字符串长度必须满足要求
# 字符 {x} ： 匹配{x}前一个字符出现 x 次        次数 == x
# 只能多不能少
result_x = re.match('^\d{6}$', '148372')        # 到 \n 结束
get_data(result_x)
print('=============================================')
# 字符 {x, y} ： 匹配{x, y}前一个字符出现在 x 和 y 之间       x <= 次数 <= y
# 只能多不能少
result_xy = re.match('^[a-zA-Z0-9_]{8,12}$', '13312332')
get_data(result_xy)

