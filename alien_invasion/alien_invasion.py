import sys

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

#from alien import Alien

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#来一艘飞船
	ship=Ship(ai_settings,screen)
	#子弹的group
	bullets=Group()
	#外星人的group
	aliens=Group()
	#创建一群外星人。。。
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#创建一个统计信息
	stats=GameStats(ai_settings)
	#创建一个开始按钮
	play_button=Button(ai_settings, screen, "Play")
	#创建一个记分牌
	sb=Scoreboard(ai_settings,screen,stats)
	#游戏主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,play_button,ship,bullets,aliens,sb)

		if stats.game_active:
			#调整飞船位置
			ship.update()
			#调整子弹位置、控制子弹数量
			gf.update_bullets(bullets,aliens,ai_settings,screen,ship,sb,stats)
			#调整外星人位置
			gf.update_aliens(ai_settings,aliens,ship,stats,screen,bullets,sb)
		#重新绘制屏幕
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
		
run_game()



