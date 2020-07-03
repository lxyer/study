class Game(object):
    top_score = 0

    @staticmethod
    def show_help():
        print("帮助信息")
    def __init__(self,player_name):
        self.player_name = player_name
    @classmethod
    def show_top_score(cls):
        print("游戏的最高分是 %d" % cls.top_score)
    def start_game(self):
        print("[%s] 开始游戏..." % self.player_name)
        # 使用类名.修改历史最高分
        Game.top_score = 999

Game.show_help()
game = Game("lxyer")
game.start_game()
Game.show_top_score()
print(eval("43+33"))


