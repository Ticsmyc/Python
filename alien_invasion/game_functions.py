import sys #QUIT 依赖模块sys

import pygame

from bullet import Bullet

from alien import Alien

from time import sleep

from button import Button

def fire_bullet(ai_settings,screen,ship,bullets):
	"""如果子弹没有用完，就发射一颗子弹"""
	if len(bullets)<ai_settings.bullet_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def check_keydown_events(event,ai_settings,screen,ship,bullets,stats,aliens,sb):
	"""按下按键"""
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	if event.key==pygame.K_LEFT:
		ship.moving_left=True
	if event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	if event.key==pygame.K_q:
		sys.exit()
	if event.key==pygame.K_p:
		if not stats.game_active:
			#隐藏光标
			pygame.mouse.set_visible(False)
			#重置游戏速度
			ai_settings.initialize_dynamic_settings()
			#重置游戏统计信息
			stats.reset_stats()
			stats.game_active=True
			#重置记分牌图像
			sb.prep_score()
			sb.prep_high_score()
			sb.prep_level()
			sb.prep_ships()
			#清空外星人列表和子弹列表
			aliens.empty()
			bullets.empty()
			#创建新的外星人，让飞船居中
			create_fleet(ai_settings,screen,ship,aliens)
			ship.center_ship()

def check_keyup_events(event,ship):
		if event.key==pygame.K_RIGHT:
			ship.moving_right=False
		if event.key==pygame.K_LEFT:
			ship.moving_left=False

def check_play_button(ai_settings,screen,ship,aliens,bullets,stats,play_button,mouse_x,mouse_y,sb):
	"""在玩家单击play按钮时开始新游戏"""
	button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active: #只有当游戏不活动时，点击才有效
		#隐藏光标
		pygame.mouse.set_visible(False)
		#重置游戏速度
		ai_settings.initialize_dynamic_settings()
		#重置游戏统计信息
		stats.reset_stats()
		stats.game_active=True
		#重置记分牌图像
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()
		#清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()
		#创建新的外星人，让飞船居中
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

def check_events(ai_settings,screen,stats,play_button,ship,bullets,aliens,sb):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN: ##检测到的事件是 按键被按下
			check_keydown_events(event,ai_settings,screen,ship,bullets,stats,aliens,sb)	
		elif event.type==pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,ship,aliens,bullets,stats,play_button,mouse_x,mouse_y,sb)

def get_number_aliens_x(ai_settings,alien_width):
	"""计算每行可容纳多少外星人"""
	available_space_x=ai_settings.screen_width-2*alien_width
	number_aliens_x=int(available_space_x / (2*alien_width))
	return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
	"""计算屏幕可容纳多少行外星人"""
	available_space_y=(ai_settings.screen_height - (3*alien_height)-ship_height)
	number_rows=int(available_space_y / (2*alien_height))
	return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""创建一个外星人，并将其放在当前行"""
	alien=Alien(ai_settings,screen)
	alien_width=alien.rect.width
	alien.x=alien_width+2*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height + 2* alien.rect.height *row_number
	aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
	"""创建外星人群"""
	#创建一个外星人，并计算一行可容纳多少外星人
	#外星人间距设为一个alien的宽度
	alien=Alien(ai_settings,screen)
	number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	# 创建第一行alien
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			#创建一个外星人并加入当前行
			create_alien(ai_settings,screen,aliens,alien_number,row_number)

def update_bullets(bullets,aliens,ai_settings,screen,ship,sb,stats):
	"""更新子弹位置，并删除消失的子弹"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,sb,stats)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,sb,stats):
		"""响应子弹和外星人的碰撞"""
		#检查是否有子弹击中了外星人
		#如果击中了，就删除相应的子弹和外星人（两个True）
		collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
		if collisions:
			for aliens in collisions.values():
				stats.score += ai_settings.alien_points*len(aliens)
				sb.prep_score()
			check_high_score(stats,sb)
		if len(aliens)==0:
			#删除现有的子弹并新建一群外星人,并加快游戏节奏
			bullets.empty()
			ai_settings.increase_speed()
			#提高等级
			stats.level+=1
			sb.prep_level()
			create_fleet(ai_settings,screen,ship,aliens)

def check_fleet_edges(ai_settings,aliens):
	"""有外星人到达边缘时采取相应的措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	"""整群外星人下移，并改变方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
	if stats.ships_left > 0:
		"""响应被外星人撞到的飞船"""
		#print(stats.ships_left)		
		stats.ships_left-=1
		#更新记分牌
		sb.prep_ships()
		#清空外星人列表和子弹列表，开始新的游戏
		aliens.empty()
		bullets.empty()
		#创建新的外星人，将飞船移到屏幕底部
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		#延迟
		sleep(0.5)
	else:
		stats.game_active=False
		pygame.mouse.set_visible(True)

def update_aliens(ai_settings,aliens,ship,stats,screen,bullets,sb):
	"""更新外星人群中所有外星人的位置"""
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	#检测外星人和飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets,sb)
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets,sb)

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
	"""更新图像，并使屏幕可见"""
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	#让最近绘制的屏幕可见
	aliens.draw(screen) #对编组调用 draw() 时， Pygame 自动绘制编组的每个元素，绘制位置由元素的属性 rect 决定
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#bullets.draw(screen) #因为bullets存的bullet只是一个rect矩形，所以不能直接用draw
	
	#显示得分
	sb.show_score()
	#如果游戏处于非活动状态，就绘制一个play按钮
	if not stats.game_active:
		play_button.draw_button()


	pygame.display.flip()

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
	"""检查是否有外星人到达屏幕底端"""
	screen_rect=screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom>=screen_rect.bottom:
			#像飞船被撞到一样去处理即可
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
			break

def check_high_score(stats,sb):
	"""检查是否诞生了新的最高分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()