import re
# 1. 需求：已知以下内容，要求匹配出所有的标题
html_str = '<h1>python</h1><h1>AI</h1><h1>大模型</h1>'
# 添加 \n 到</h1>\n后就匹配不到，重新开始扫描<h1>
html_str1 = '<h1>python</h1>\n<h1>AI</h1>\n<h1>大模型</h1>'
# findall 贪婪匹配
result = re.findall('<h1>(.*)</h1>', html_str)
result = re.findall('<h1>(.*)</h1>', html_str1)
print(result)
# findall 非贪婪匹配：在量词后加 ?，变为非贪婪：满足规则就停止，尽可能少匹配
result = re.findall('<h1>(.*?)</h1>', html_str)
print(result)
