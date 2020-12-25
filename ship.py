import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 使飞船（矩形）的中心x坐标等于整个屏幕的中心x坐标
        self.rect.bottom = self.screen_rect.bottom  # 使飞船（矩形）的底部y坐标等于整个屏幕的底部y坐标
        self.center = float(self.rect.centerx)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)  # blit接受的参数是（源图， 处理后的对象）
        # 其中rect方法后的属性centerx、center、bottom、top之类默认都不读取，在手动设置值之后，self.rect拥有这些属性

    def update(self):
        #  根据移动标志调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.y = self.y
