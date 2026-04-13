# search：re.search（正则表达式， 要匹配的字符串）
# 可以不从头开始匹配，但只能匹配一个
# 1. 导包
import re
# 2. 匹配
result = re.search('clara', '111clara is clara a beauty')
# 3. 查看结果类型
print(result, type(result))
# 4. 获取结果
# 非空即为 True
if result:
    print(f'匹配成功{result.group()}')
else:
    print('匹配失败')

