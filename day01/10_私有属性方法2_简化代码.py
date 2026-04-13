# 银行取钱动作：插卡->用户认证->取款->打印账单
# 1. 先定义类
class ATM(object):
    # 私有方法，保证安全，同时简化用户操作
    # 插卡
    def __card(self):
        print('插卡...识别...此处省略1k行代码')

    # 用户认证
    def __auth(self):
        print('用户认证...此处省略1k行代码')

    # 取款
    def __get_money(self):
        print('一系列的判断操作')
        # print(f'已经取出{money}元...此处省略1k行代码')

    # 打印账单
    def __pnf(self):
        print('打印账单...此处省略1k行代码')

    # 对外提供公共的接口
    def get_money(self):
        self.__card()
        self.__auth()
        self.__get_money()
        self.__pnf()


# 2. 根据类创建对象
a = ATM()
a.get_money()
