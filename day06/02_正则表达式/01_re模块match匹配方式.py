# match格式：re.match(正则表达式, 要匹配的字符)
# 只能从开头匹配， 只能返回匹配成功的一个
# 1. 导包
import re
# 2. 匹配
result = re.match('clara', '111clara is a beauty clara')
# 3. 查看结果类型
print(result, type(result))
# 4. 获取结果
# print(result.group())
# 加个判断：非空即为 True
if result:
    print(f'匹配成功：{result.group()}')
else:
    print(f'匹配失败')

