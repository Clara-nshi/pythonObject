import re


# 提前定义一个函数用于提取结果
def get_data(result):
    if result:
        print(f'匹配成功, {result.group()}')
    else:
        print('匹配失败')


# 字符 * ： 匹配前一个字符出现 0 次或无数次      次数 >= 0
result_xing = re.match('.*', 'banisud')
result_xing1 = re.match('.*', '')
result_xing2 = re.match('.*', 'ban\nisud')        # 到 \n 结束
# TODO： re.S代表让 . 匹配到 \n 达到， 真正匹配任意一个字符
result_xing3 = re.match('.*', 'ban\nisud', re.S)        # 到 \n 结束
get_data(result_xing)
get_data(result_xing1)
get_data(result_xing2)
get_data(result_xing3)
print('=============================================')
# 字符 + ： 匹配前一个字符出现 1 次或无数次      次数 >= 1
result_jia = re.match('.+', 'bz_666\n黑马')
get_data(result_jia)
result_jia1 = re.match('.+', '')
get_data(result_jia1)
print('=============================================')
# 字符 ？ ： 匹配前一个字符出现 0 次或 1 次     次数 == 0 或 次数 == 1
result_wenhao = re.match('https?:.*', 'http://www.baidu.com')        # 到 \n 结束
result_wenhao1 = re.match('https?:.*', 'https://www.baidu.com')        # 到 \n 结束
get_data(result_wenhao)
get_data(result_wenhao1)
print('=============================================')
# 字符 {x} ： 匹配{x}前一个字符出现 x 次        次数 == x
# 只能多不能少
result_x = re.match('\d{6}', '14837293864')        # 到 \n 结束
get_data(result_x)
print('=============================================')
# 字符 {x, y} ： 匹配{x, y}前一个字符出现在 x 和 y 之间       x <= 次数 <= y
# 只能多不能少
result_xy = re.match('[a-zA-Z0-9_]{8,12}', '132456775432')
get_data(result_xy)

