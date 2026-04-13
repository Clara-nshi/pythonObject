# 1. 导包
"""
0 48
A 65
a 97
"""
import re
# 需求1：匹配验证码，忽略大小写
yzm = 'Soi2'
result = re.match('SOI2', yzm, re.I)
if result:
    print(f'匹配成功：{result.group()}')
else:
    print('匹配失败')


# 需求2：.匹配任意内容， 使用re.S让.匹配到\n，实现真正的匹配任意字符
text = '\n宁宁\n美女\n哈哈哈'
result = re.match('.*', text, re.S)
if result:
    print(f'匹配成功：{result.group()}')
else:
    print('匹配失败')
