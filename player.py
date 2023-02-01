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
        self.velocity=0;
        self.x_velocity=0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def set_map(self, map):
        self.map = map

    def handle_key_presses(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.isJumping <= 4:
            self.jump()
            print("works")
            self.isJumping+=1
        if pygame.key.get_pressed()[pygame.K_a] and self.x_velocity.__abs__() <= 5:
            self.x_velocity-=2;
        if pygame.key.get_pressed()[pygame.K_d] and self.x_velocity.__abs__() <= 5:
            self.x_velocity+=2;

    def act(self):
        oldx=self.x
        oldy=self.y
        self.handle_key_presses()
        self.velocity-=self.map.get_gravity()
        self.y += self.velocity
        self.x +=self.x_velocity
        if self.x_velocity<0:
            self.x_velocity+=0.5
        if self.x_velocity>0:
            self.x_velocity-=0.5
        if self.is_map_collision():
            self.y = oldy
            if self.velocity<0.1:
                self.velocity=0
            else:
                self.velocity*=-1/2
            self.isJumping=0

    def jump(self):
        self.velocity-=1.5

    def is_map_collision(self):
        plat =self.map.get_hit_boxes()
        for p in plat:
            if p.get_rect().colliderect(pygame.Rect(self.x,self.y,self.width,self.height)):
                return True
        return False



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
        self.gravity = gravity

    def get_hit_boxes(self):
        return self.platforms

    def add(self, platform):
        self.platforms.append(platform)

        # Precondition: homogeneous list of platform objects
    def get_gravity(self):
        return self.gravity
    def set_gravity(self, gravity):
        self.gravity=gravity;
    def draw(self, screen):
        for p in self.platforms:
            p.draw(screen)
