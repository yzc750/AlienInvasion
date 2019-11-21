import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_function as gf


def run_game():
    # 初始pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个子弹编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标时间
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船状态
        if stats.game_active:
            ship.update()
            # 更新子弹状态
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 更新外星人状态
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
