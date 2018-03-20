import random
class Liu_BO_Yu_caishuzi(object):
	#一共猜的次数
	liuboyu_all_cishu = []
	#猜中的次数
	liuboyu_OK = 0
	#单局游戏猜的次数
	liuboyu_cishu = 0
	#开始游戏
	def liuboyu_game(self):
		print("游戏开始")
		
		a = True
		b = True
		while a:
			liuboyu_shuzi = random.randint(0,99)
			while b:
				liuboyu_cai = int(input("请输入一个数字："))
				Liu_BO_Yu_caishuzi.liuboyu_cishu+=1
				if liuboyu_cai > liuboyu_shuzi:
					print("数猜大了")
				elif liuboyu_cai == liuboyu_shuzi:
					#如果猜中，记录猜中的次数
					Liu_BO_Yu_caishuzi.liuboyu_OK+=1
					#将单局猜的次数放到列表了
					Liu_BO_Yu_caishuzi.liuboyu_all_cishu.append(Liu_BO_Yu_caishuzi.liuboyu_cishu)
					#判断用户是否继续游戏
					liuboyu_again = input("你猜对了，是否继续游戏1继续,2退出")
					if liuboyu_again == 1:
						Liu_BO_Yu_caishuzi.liuboyu_cishu =0		
						b = False
					else:
						print("你一共玩了%d把游戏"%Liu_BO_Yu_caishuzi.liuboyu_OK)
						for i in range(0,len(Liu_BO_Yu_caishuzi.liuboyu_all_cishu)):
							print("第%d把游戏你用了%d猜中"%(i+1,Liu_BO_Yu_caishuzi.liuboyu_all_cishu[i]))
						self.liuboyu_pingjun = sum(Liu_BO_Yu_caishuzi.liuboyu_all_cishu)/Liu_BO_Yu_caishuzi.liuboyu_OK
						print("你平均%d次猜中数字"%self.liuboyu_pingjun)
						b = False
						a = False
				else:
					print("数猜小了")
q = Liu_BO_Yu_caishuzi()
q.liuboyu_game()

