# 1.
class Game(object):
    # 定义一个类属性存储总积分
    ALL_SCORE = 0

    # 定义成员属性
    def __init__(self, player_name):
        self.player_name = player_name
        # 成员属性: 每个玩家自己的分数
        self.player_score = 0

    # 定义静态方法:显示帮助信息
    @staticmethod
    def show_help():
        print("这是一个帮助信息")

    # 定义类方法:显示历史总结分的方法
    @classmethod
    def show_all_score(cls):
        print(f'总分为: {cls.ALL_SCORE}')

    # 定义成员方法: 玩家玩游戏
    def start_game(self):
        print(f'{self.player_name}玩了一局游戏')
        # 自己的分数＋1
        self.player_score += 1
        Game.ALL_SCORE += 1

    def show_my_score(self):
        print(f'{self.player_name}的个人积分是{self.player_score}')


# 2. 显示帮助信息
Game.show_help()
# 3. 先查看总积分
Game.show_all_score()
# 4. 创建玩家并开始游戏
game = Game('clara')
game.start_game()
game.start_game()
game.start_game()
Game.show_all_score()
game.show_my_score()

game1 = Game('mike')
game1.start_game()
game1.start_game()
Game.show_all_score()
game1.show_my_score()





