import pygame


class Player:

    def __init__(self, map):
        self.x = 400
        self.y = 400
        self.width = 30
        self.height = 30
        self.color = (255, 0, 0)
        self.map = map
        self.isJumping = False
        self.velocity = 0;
        self.x_velocity = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def set_map(self, map):
        self.map = map

    def handle_key_presses(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.isJumping <= 12:
            self.velocity-=1.5
            print("works")
            self.isJumping += 2
        if pygame.key.get_pressed()[pygame.K_a] and self.x_velocity.__abs__() <= 10:
            self.x_velocity -= 2;
        if pygame.key.get_pressed()[pygame.K_d] and self.x_velocity.__abs__() <= 10:
            self.x_velocity += 2;

    def act(self):
        oldx = self.x
        oldy = self.y
        self.handle_key_presses()
        self.velocity -= self.map.get_gravity()
        self.y += self.velocity
        self.x += self.x_velocity
        if self.x_velocity < 0:
            self.x_velocity += 0.5
        if self.x_velocity > 0:
            self.x_velocity -= 0.5
        if self.where_map_collision()== "bottom":
            self.y = oldy
            if self.velocity < 0.1:
                self.velocity = 0
            else:
                self.velocity *= -1 / 2
            self.isJumping = 0
        if self.where_map_collision()== "top":
            self.y = oldy
            if self.velocity < 0.1:
                self.velocity = 0
            else:
                self.velocity *= -1 / 2
        if self.where_map_collision() == "left" or self.where_map_collision() == "right":
            self.x=oldx
            self.x_velocity=0
            if self.velocity<0:
                self.isJumping = 2
        return (self.x, self.y)


    def jump(self):
        if self.isJumping <= 12:
            self.velocity -= 6
            print("works")
            self.isJumping += 2

    def mvr(self):
        if self.x_velocity.__abs__() <= 10:
            self.x_velocity -= 2;

    def mvl(self):
        if self.x_velocity.__abs__() <= 10:
            self.x_velocity += 2;

    def is_map_collision(self):
        plat = self.map.get_hit_boxes()
        for p in plat:
            if p.get_rect().colliderect(pygame.Rect(self.x, self.y, self.width, self.height)):
                return True
        return False
    def coin_col(self):
        myHitBox = pygame.Rect(self.x, self.y, self.width, self.height)
        coins = self.map.get_coins()
        for i in range(len(coins)):
            if coins.g(i).get_rect().colliderect(pygame.Rect(self.x, self.y, self.width, self.height)):
                Map.remc(i)


    def where_map_collision(self):
        myHitBox=pygame.Rect(self.x, self.y, self.width, self.height)
        myBottomY=self.y+self.height
        diffInYBottom=0
        diffInYTop=0
        diffInXLeft=0
        diffInXRight=0
        plat = self.map.get_hit_boxes()
        for p in plat:
            if p.get_rect().colliderect(pygame.Rect(self.x, self.y, self.width, self.height)):
                diffInYBottom = (self.y+self.height-p.get_rect().y)
                diffInXLeft = (self.x+self.width-p.get_rect().x)
                diffInYTop = (p.get_rect().height + p.get_rect().y-self.y)
                diffInXRight = (p.get_rect().width + p.get_rect().x-self.x)
                if diffInYBottom<diffInYTop:
                    if diffInXRight<diffInYBottom:
                        return "right"
                    else:
                        if diffInXLeft<diffInYBottom:
                            return "left"
                        else:
                            return "bottom"
                else:
                    if diffInXRight<diffInYTop:
                        return "right"
                    else:
                        if diffInXLeft<diffInYTop:
                            return "left"
                        else:
                            return "top"

        return "none"






class Platform:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())


class Map:
    def __init__(self, gravity=-0.5):
        self.platforms = []
        self.coins = []
        self.gravity = gravity

    def get_hit_boxes(self):
        return self.platforms

    def get_coins(self):
        return self.coins

    def add(self, platform):
        self.platforms.append(platform)

    def addc(self, coin):
        self.coins.append(coin)

    def remc(self, int):
        print()
        self.coins.remove(self.coins.__getitem__(int))


        # Precondition: homogeneous list of platform objects

    def get_gravity(self):
        return self.gravity

    def set_gravity(self, gravity):
        self.gravity = gravity;

    def draw(self, screen):
        for p in self.platforms:
            p.draw(screen)
        for c in self.coins:
            c.draw(screen)
class coin:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def get_rect(self):
        return pygame.Rect(self.x, self.y, 30, 30)
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,0, 10), self.get_rect())

