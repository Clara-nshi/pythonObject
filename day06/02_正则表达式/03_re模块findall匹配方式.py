# findall：re.findall（正则表达式， 要匹配的字符串）
# 可以不从头开始匹配，可以匹配多个
# 1. 导包
import re
# 2. 匹配
result = re.findall('clara', 'clara is clara a beauty')
# 3. 查看结果类型
print(type(result))
# 4. 获取结果
print(result)

