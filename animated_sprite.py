import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, rows, columns, pos, group):
        super().__init__(group)
        self.frames = []
        self.index = 0
        self.cut_sheet(sheet, rows, columns)  # разрежем таблицу на картинки
        self.image = self.frames[self.index]
        self.rect.center = pos  # установим спрайта по центру

    def cut_sheet(self, sheet, rows, columns):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                cur_frame = sheet.subsurface(pygame.Rect(frame_location, self.rect.size))
                self.frames.append(cur_frame)

    def update(self):
        self.index = (self.index + 1) % len(self.frames)
        self.image = self.frames[self.index]