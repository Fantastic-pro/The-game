import Menu

bypass_pep8 = Menu


def main():  # Основная функция
    import random
    import pygame
    import Menu
    from Constants import WIDTH, HEIGHT, WHITE, BLACK, GREEN, \
        BLUE, BOT_LEVEL
    import Cut_of_sprites
    pygame.init()
    pygame.display.set_caption('DEhorses')
    pygame.mixer.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    # Группа спрайтов(Лошадей)
    all_sprites = pygame.sprite.Group()
    # Группа спрайтов(деревьев и камней)
    back_sprites = pygame.sprite.Group()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    # Загрузка музыки
    m = Cut_of_sprites.load_sound("backgroundmusic.mp3")
    pygame.mixer.music.load(m)
    pygame.mixer.music.play()

    # Класс камня
    class Rock(pygame.sprite.Sprite):
        def __init__(self, sheet, columns, rows, x, y):
            super().__init__(back_sprites)
            self.frames = []
            self.cut_sheet(sheet, columns, rows)
            self.cur_frame = random.randint(0, columns * rows - 1)
            self.image = self.frames[self.cur_frame]
            self.image = pygame.transform.scale(self.image,
                                                (self.image.get_width() // 10,
                                                 self.image.get_height() //
                                                 10))
            self.rect = self.rect.move(x, y)

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                    sheet.get_height() // rows)
            for j in range(rows):
                for ii in range(columns):
                    frame_location = (self.rect.w * ii, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pygame.Rect(
                        frame_location, self.rect.size)))

        # Функция перемещения камней
        def movee(self, x):
            self.rect.x -= x
            if self.rect.x < -10:
                self.rect.x = 1200 + random.randrange(0, 50)
                self.rect.y = random.randrange(0, 600)

    # Класс дерева
    class Tree(pygame.sprite.Sprite):
        def __init__(self, sheet, columns, rows, x, y):
            super().__init__(back_sprites)
            self.frames = []
            self.cut_sheet(sheet, columns, rows)
            self.cur_frame = random.randint(0, columns * rows - 1)
            self.image = self.frames[self.cur_frame]
            self.image = pygame.transform.scale(self.image,
                                                (self.image.get_width() // 5,
                                                 self.image.get_height() //
                                                 5))
            self.rect = self.rect.move(x, y)

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                    sheet.get_height() // rows)
            for j in range(rows):
                for ii in range(columns):
                    frame_location = (self.rect.w * ii, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pygame.Rect(
                        frame_location, self.rect.size)))

        # Функция перемещения деревьев
        def movee(self, x):
            self.rect.x -= x
            if self.rect.x < -20:
                self.rect.x = 1200 + random.randrange(0, 100)
                self.rect.y = 470 + random.randrange(0, 20)

    class Horse(pygame.sprite.Sprite):
        def __init__(self, sheet, columns, rows, x, y):
            super().__init__(all_sprites)
            self.frames = []
            self.cut_sheet(sheet, columns, rows)
            self.cur_frame = 6
            self.image = self.frames[0]
            self.rect = self.rect.move(x, y)
            self.cx = 0
            self.flag_of_contin = True
            self.timer = 3  # Таймер
            self.uskorenie = 0

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                    sheet.get_height() // rows)
            for j in range(rows):
                for ii in range(columns):
                    frame_location = (self.rect.w * ii, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pygame.Rect(
                        frame_location, self.rect.size)))

        def update(self):
            self.image = self.frames[self.cur_frame]

        # Функция статичной лошади
        def update_2(self):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[0]

        def movee(self):
            if self.uskorenie > 0:
                self.rect.x += 1
                self.uskorenie -= 1
            if self.uskorenie >= 0:
                self.rect.x += 1
            else:
                self.uskorenie += 1

        # Функция ускорения, если пользователь успел нажать
        def movee_super(self):
            self.uskorenie = 40

        # Функция торможения, если пользователь нажал не в тот момент
        def tormoz(self):
            self.uskorenie = -40

    # Функция таймера и старта
    def draw(timer):
        timer = int(timer)
        font = pygame.font.Font(None, 50)
        if timer >= 1:
            text = font.render(str(timer), 1, (100, 255, 100))
        else:
            text = font.render("START", 1, (100, 255, 100))
        text_x = WIDTH // 2 - text.get_width() // 2
        text_y = 10
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)

    # Функция сдвига финишной черты
    def draw_of_finish(f_line):
        if f_line > 0:
            pygame.draw.line(screen, GREEN, [f_line, 0], [f_line, 600])

    # Функция прорисовки победы
    def draw_of_win(c, flag):
        if flag:
            font = pygame.font.Font(None, 50)
            text = font.render("", 1, (100, 255, 100))
            if c == 1:
                text = font.render("Победа первой лошади", 1, (100, 255, 100))
            if c == 2:
                text = font.render("Победа второй лошади", 1, (100, 255, 100))
            if c == 3:
                text = font.render("Победа третьей лошади", 1, (100, 255, 100))
            text_x = WIDTH // 2 - text.get_width() // 2
            text_y = 10
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            pygame.draw.rect(screen, (0, 255, 0),
                             (text_x - 10, text_y - 10,
                              text_w + 20, text_h + 20), 1)

    clock = pygame.time.Clock()

    running = True

    horse1 = Horse(Cut_of_sprites.load_image("hor3.png", WHITE), 4, 4, 50, 50)
    horse2 = Horse(Cut_of_sprites.load_image("hor3.png", WHITE), 4, 4, 50, 200)
    horse3 = Horse(Cut_of_sprites.load_image("hor3.png", WHITE), 4, 4, 50, 350)
    rocks = []
    for i in range(10):
        rocks.append(Rock(Cut_of_sprites.load_image(
            "rock-sprite-png-3.png"), 8, 8, random.randrange(0, 1200),
            random.randrange(0, 600)))
    for i in range(5):
        rocks.append(Tree(Cut_of_sprites.load_image(
            "tree2.png"), 6, 4, random.randrange(0, 1200),
            470 + random.randrange(0, 20)))
    start_line = 230
    finish_line = 0

    timer1 = random.randrange(3, 5)
    timer3_for_start = 8
    dt = 0  # Delta time (time since last tick).
    if Menu.flag_of_starting_display:
        while 0 <= timer3_for_start < 20:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    timer3_for_start = "EXIT"
                horse1.update()
                horse2.update()
                horse3.update()
            back_sprites.update()
            all_sprites.update()
            screen.fill(WHITE)
            back_sprites.draw(screen)
            all_sprites.draw(screen)
            pygame.draw.line(screen, BLACK, [0, 60], [1200, 60])
            pygame.draw.line(screen, BLACK, [0, 210], [1200, 210])
            pygame.draw.line(screen, BLACK, [0, 360], [1200, 360])
            pygame.draw.line(screen, BLACK, [0, 510], [1200, 510])
            pygame.draw.line(screen, BLUE, [230, 0], [230, 600])
            draw(timer3_for_start)
            timer3_for_start -= dt
            dt = clock.tick(30) / 1000  # / 1000 Перевести в секунды
            pygame.display.flip()

    count = 0
    win = False
    pauza = False
    while running and timer3_for_start <= 0:
        leader = 0  # Координата лидера гонки
        if horse1.rect[0] > leader:
            leader = horse1.rect[0]
        if horse2.rect[0] > leader:
            leader = horse2.rect[0]
        if horse3.rect[0] > leader:
            leader = horse3.rect[0]
        if leader >= 900 and finish_line == 0:
            finish_line = 1200
        if win is False and finish_line > 0:
            if horse1.rect[0] >= finish_line - 180:
                count = 1
                win = True
            if horse2.rect[0] >= finish_line - 180:
                count = 2
                win = True
            if horse3.rect[0] >= finish_line - 180:
                count = 3
                win = True
        if random.randrange(0, 1) == 0:
            horse1.update_2()
        if random.randrange(0, 1) == 0:
            horse2.update_2()
        if random.randrange(0, 1) == 0:
            horse3.update_2()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pauza:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            else:
                clock.tick(30)
                continue
        horse1.movee()
        horse2.movee()
        horse3.movee()

        timer1 -= dt
        back_sprites.update()
        all_sprites.update()
        screen.fill(WHITE)
        back_sprites.draw(screen)
        all_sprites.draw(screen)
        # Прорисовка дорожек
        pygame.draw.line(screen, BLACK, [0, 60], [1200, 60])
        pygame.draw.line(screen, BLACK, [0, 210], [1200, 210])
        pygame.draw.line(screen, BLACK, [0, 360], [1200, 360])
        pygame.draw.line(screen, BLACK, [0, 510], [1200, 510])
        pygame.draw.line(screen, BLUE, [start_line, 0], [start_line, 600])
        draw_of_finish(finish_line)
        draw_of_win(count, win)
        # Остановка забега
        if leader >= 1000:
            pauza = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            # Выход из забега
            running = False
        if timer1 > 1:
            # Не вовремя нажата кнопка, лошадь замедляется
            if horse1.uskorenie == 0 and keys[pygame.K_z]:
                horse1.tormoz()
            if horse2.uskorenie == 0 and keys[pygame.K_v]:
                horse2.tormoz()
            if horse3.uskorenie == 0 and keys[pygame.K_m]:
                horse3.tormoz()

        if timer1 <= 1:
            r_num2 = random.randrange(0, 3)
            r_num3 = random.randrange(0, 3)
            pygame.draw.circle(screen, GREEN, (leader + 150, 30), 25)
            # Для одного игрока
            if Menu.flag_of_game1:
                if keys[pygame.K_z]:
                    # Вовремя нажата кнопка
                    horse1.movee_super()
                    timer1 = random.randrange(3, 5)
                if r_num2 == 0 and timer1 < BOT_LEVEL:
                    # Бот нажимает кнопку
                    horse2.movee_super()
                    timer1 = random.randrange(3, 5)
                if r_num3 == 0 and timer1 < BOT_LEVEL:
                    # Бот нажимает кнопку
                    horse3.movee_super()
                    timer1 = random.randrange(3, 5)
            # Для двух игроков
            if Menu.flag_of_game2:
                if keys[pygame.K_z]:
                    horse1.movee_super()
                    timer1 = random.randrange(3, 5)
                if keys[pygame.K_v]:
                    horse2.movee_super()
                    timer1 = random.randrange(3, 5)
                if r_num3 == 0 and timer1 < BOT_LEVEL:
                    horse3.movee_super()
                    timer1 = random.randrange(3, 5)
            # Для трех игроков
            if Menu.flag_of_game3:
                if keys[pygame.K_z]:
                    horse1.movee_super()
                    timer1 = random.randrange(3, 5)
                if keys[pygame.K_v]:
                    horse2.movee_super()
                    timer1 = random.randrange(3, 5)
                if keys[pygame.K_m]:
                    horse3.movee_super()
                    timer1 = random.randrange(3, 5)
        if timer1 <= 0:
            # Задаем новый таймер для круга
            timer1 = random.randrange(3, 5)
        pygame.display.flip()
        dt = clock.tick(30) / 1000  # / 1000 Перевести в секунды
        start_line = start_line - dt * 100
        # Перемещение камней и деревьев
        for i in range(len(rocks)):
            rocks[i].movee(dt * 100)
        # Рисование линии старта
        if finish_line > 0:
            finish_line = finish_line - dt * 100
    pygame.quit()
