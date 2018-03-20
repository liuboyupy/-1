#精灵类
import pygame
import random
#设置游戏屏幕大小(常量:牵一发动全身)
SCREEN_RECT =pygame.Rect(0, 0, 700, 480)
#敌机定时器事件常量
CREATE_ENEMY_EVENT= pygame.USEREVENT
#发射子弹
HERO_FIRE_EVENT = pygame.USEREVENT +1
#我们自己去定制的精灵类　需要继承　pygame提供的精灵类
#我们需要定义:
#image--图片
#rect--坐标
#speed--速度
class GameSprite(pygame.sprite.Sprite):
	'''游戏精灵的基础类'''
	def __init__(self,new_image,new_speed=2):
		#调用父类的初始化方法
		super().__init__()
		#需要三个属性
		#pygame.image.load pygame提供的方法　主要是加载图片
		self.image = pygame.image.load(new_image)
		#self.image.get_rect()获取图片的宽高 get_rect()是pygame提供
		self.rect = self.image.get_rect()
		#这是将来的精灵移动的速度　精灵有　：英雄　　背景　　敌机　子弹　
		self.speed = new_speed
	def update(self,*args):
		#默认垂直方向移动	(Ｙ轴控制垂直移动)
		#每一次加上我的默认速度
		self.rect.x += self.speed

class Background(GameSprite):
	def __init__(self,is_alt=False):
		super().__init__('/home/liuboyu/桌面/images/background.png')
		if is_alt:
			self.rect.right= 0

	def update(self):
		super().update()
		if self.rect.x >= self.rect.width:
			self.rect.x = -self.rect.width
		

	#背景类
	
class Enemy(GameSprite):
	#调用父类方法　创建敌机精灵　并制定敌机图像
	def __init__(self):
		super().__init__('/home/liuboyu/桌面/images/enemy1.png')
		#设置敌机初始速度
		self.speed=random.randint(3,5)
		#设置敌机的随机初始位置
		self.rect.x= -self.rect.left
		max_x =SCREEN_RECT.height-self.rect.height
		self.rect.y=random.randint(0,max_x)
	def update(self):
		#判断是否移出屏幕　如果移出　我们就把他设置到屏幕上方
		#SCREEN_RECT.height 这是自己设置的常量
		super().update()
		if self.rect.right<0:
			print('敌机飞出屏幕')
			self.kill()
	#英雄子弹类
class Hero (GameSprite):
	def __init__(self):
		#设置英雄的初始速度
		super().__init__('/home/liuboyu/桌面/images/me1.png',0)
		self.bullets = pygame.sprite.Group()
		#设置初始位置  让飞机的Ｘ轴等于屏幕的中心点
		self.rect.centerx=SCREEN_RECT.centerx + 230
		#这是飞机的Ｙ轴
		self.rect.bottom=SCREEN_RECT.bottom-220

		self.move = False
	def update(self):
		if not self.move:
			self.rect.x += self.speed
		else:
			self.rect.y += self.speed
		
		#控制英雄边界　
		if self.rect.left < 0:
			self.rect.left=0
		if self.rect.right>SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		# if self.rect.bottom < 0:
		# 	self.rect.top = SCREEN_RECT.height
		# if self.rect.top > SCREEN_RECT.height:
		# 	self.rect.bottom = 0

		if self.rect.top < 0:
			self.rect.top = 0

		if self.rect.bottom > SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height
	def fire(self):
		#英雄的方法
		print('发送子弹')
		for i in (1,2):
			#创建子弹精灵
			self.bullet = Bullet()
			#设置精灵位置
			self.bullet.rect.left = self.rect.left - i*20
			self.bullet.rect.centery = self.rect.centery
			#将子弹添加到精灵组
			self .bullets.add(self.bullet)

		#子弹精灵
class Bullet(GameSprite):
	def __init__(self):
		super().__init__('/home/liuboyu/桌面/images/bullet2.png',-6)
	def update(self):
		super().update()
		#判断是否超出屏幕
		if self.rect.right<0:
			self.kill()
