import pygame
from plane_sprites import *

#导入音乐
#pygame.init()
#加载
#pygame.mixer.music.load('./Jam - 差三岁.mp3')
#播放
#pygame.mixer.music.play()
class PlaneGame(object):
	'''飞机大战 主游戏类'''
	#初始化方法
	def __init__(self):
		print ('游戏初始化')
		# 1 创建游戏窗口
		# ２　创建游戏时钟
		# ３　调用创建精灵和精灵组的方法
		#　设置游戏窗口背景的大小
		self.screen=pygame.display.set_mode(SCREEN_RECT.size)
		#1创建游戏时钟
		self.clock=pygame.time.Clock()
		#2调用精灵的方法
		self.__create_sprites()
		#设置定时器事件　每秒创建一架敌机
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		#设置发射子弹的定时器事件
		pygame.time.set_timer(HERO_FIRE_EVENT,1000)
		#开始游戏
	def start_game(self):
		while True:
			pygame.init()
			#设置帧率
			self.clock.tick(60)
			#监听事件
			self.__event_handler()
			#碰撞检测
			self.__chenck_collide()
			#更新精灵
			self.__update_sprites()
			#刷新
			pygame.display.update()


		# 创建精灵　和精灵组　封装成一个方法
	def __create_sprites(self):
		#背景组
		bg1 = Background()
		bg2 = Background(True)
		self.hero = Hero()
		#将背景图片滚动连贯
		#竖屏无所谓
		#bg2.rect.y = -bg2.rect.height
		self.back_group = pygame.sprite.Group(bg1,bg2)
		#敌机组
		self.enemy_group=pygame.sprite.Group()
		#英雄组
		self.hero_group=pygame.sprite.Group(self.hero)
		

	#事件监听
	def __event_handler(self):
						#获取所有的事件
		for event in pygame.event.get():
			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_SPACE]:
				self.hero.fire()
			if keys_pressed[pygame.K_RIGHT]:
				print('向右边移动')
				#给英雄定义移动速度
				self.hero.move = False
				self.hero.speed = 8
			elif keys_pressed[pygame.K_LEFT]:
				self.hero.move = False
				self.hero.speed = -8
				print('英雄向左边移动')
			elif keys_pressed[pygame.K_UP]:
				self.hero.move = True
				self.hero.speed = -8
				print('向上移动')
			elif keys_pressed[pygame.K_DOWN]:
				self.hero.move = True
				self.hero.speed = 8
				print('向下移动')
			else :
				self.hero.speed = 0
			if event.type == pygame.QUIT:
				self.__game_over()
			if event.type==CREATE_ENEMY_EVENT:
				print('敌机出厂')
				self.enemy_group.add(Enemy())
			# elif event.type==HERO_FIRE_EVENT:
			# 	self.hero.fire()	
				#捕获英雄事件
			# elif event.type==pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			# 	print('向右移动')
	#更新精灵和精灵组
	def __update_sprites(self):
		#先更新更新精灵组
		for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
			#刷新位置
			group.update()
			# #绘制到屏幕上
			group.draw(self.screen) 

	#碰撞检测
	def __chenck_collide(self):
		#子弹摧毁飞机
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		#敌机撞毁飞机
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		#判断列表
		if len(enemies)>0:
			#让英雄牺牲
		 	self.hero.kill()
		 	#结束游戏
		 	PlaneGame.__game_over()
		 	
	#退出游戏
	@staticmethod
	def __game_over():
		print ('游戏结束')
		#卸载功能
		pygame.quit()
		#脚本退出
		exit()
#只在本类生效
if __name__=='__main__':
	#创建游戏对象
	game = PlaneGame()
	#开始游戏
	game.start_game()

