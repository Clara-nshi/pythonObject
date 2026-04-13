# 导包
import requests
# TODO: requests访问有效的地址
res = requests.get('https://baike.baidu.com/')
print(res, type(res))
# 查看状态码
print(res.status_code)
# 查看内容：默认二进制
print(res.content)
# TODO 解码
print(res.content.decode('utf8'))
# 查看内容， unicode解码，可能会乱码
print(res.text)

print('=============================')
a = '我喜欢你'.encode('utf8')
print(a)
b = a.decode('utf8')     # 如果解码和编码不一样，可以会报错或乱码
print(b)

# import requests
#
# res = requests.get('https://blog.csdn.net/weixin_60925698/category_13148885.html')
# print(res, type(res))
# # 查看状态码
# print(res.status_code)
# # 查看内容
# print(res.content)
# print(res.content.decode('utf8'))








