# StickMan_Running
import random, time
from tkinter import *

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr.Stick Man Dashes to W.C for preventing Disaster! (500x550)")
        self.tk.resizable(1,1)
        self.tk.wm_attributes("-topmost",1)
        self.canvas = Canvas(self.tk, height=550, width=500,highlightthickness=0)
        self.canvas.pack()
        
        self.tk.update()
        self.canvas_height = 500; self.canvas_width = 500   # ....N0 NEED.
        self.bg = PhotoImage(file="../static/img_stickman/bground_sq060.png")
        w = self.bg.width()     # What's this ?
        h = self.bg.height()
        for x in range(0,10):
            for y in range(0,10):
                self.canvas.create_image(x*w,y*h,image=self.bg, anchor='nw')
                self.sprites =[]
                self.running = True
        self.obj_text0 = self.canvas.create_text(10,540,text='REMAIN TIME: 50 sec.',
            font=('normal',12,'bold','underline',), anchor='sw' )

        self.obj_text1 = self.canvas.create_text(250,20,text='Stickman-The Deadliest POOP DASH!',
            font=('normal',14,'bold','underline',), )

    def mainloop(self):
        while 1:                # meaning it is infinite loop while True.
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)
class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1; self.y1 = y1
        self.x2 = x2; self.y2 = y2  # Automatically initialize all Var.=0

    def within_x(co1, co2):
        if (co1.x1 > co2.y1 and co1.y1 < co2.x2) \
                or (co1.x2 > co2.y1 and co1.x2 < co2.x2) \
                or (co2.x1 > co1.y1 and co2.x1 < co1.x2) \
                or (co2.x2 > co1.y1 and co2.x2 < co1.x1):
            return True
        else:
            return False

    def within_y(co1, co2):
        if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
                or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
                or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
                or (co2.y2 > co1.y1 and co2.y2 < co1.y1):
            return True
        else:
            return False

    def collided_left(co1, co2):
        if within_y(co1, co2):
            if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
                return True
        return False

    def collided_right(co1, co2):
        if within_y(co1, co2):
            if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
                return True
        return False

    def collided_top(co1, co2):
        if within_x(co1, co2):
            if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
                return True
        return False

    def collided_bottom(y, co1, co2):
        if within_x(co1,co2):
            y_calc = co1.y2 + y
            if y_calc >= co2.y1 and y_calc <= co2.y2:
                return True
        return False
class Sprite:
    def __init__(self, game):
        self.game = game;   self.endgame = False
        self.coordinates = None
    def move(self):
        pass
    def coords(self):
        return self.coordinates
class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, \
            image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x+width, y+height)
class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
        self.images_left=[PhotoImage(file="../static/img_stickman/sman_01.png"),
            PhotoImage(file="../static/img_stickman/sman_02.png"),
            PhotoImage(file="../static/img_stickman/sman_03.png")]
        self.images_right=[PhotoImage(file="../static/img_stickman/sman_04.png"),
            PhotoImage(file="../static/img_stickman/sman_05.png"),
            PhotoImage(file="../static/img_stickman/sman_06.png")]
        self.image = game.canvas.create_image(300,470,\
            image=self.images_left[0],anchor='nw')
        self.x = -2;    self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords()
        game.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        game.canvas.bind_all('<space>',self.jump)

    def turn_right(self,evt):
        if self.y == 0: self.x = +2

    def turn_left(self,evt):
        if self.y == 0: self.x = -2

    def jump(self,evt):
        if self.y == 0: self.y = -4; self.jump_count = 0

    def animate(self):
        if self.x != 0 and self.y ==0:
            if time.time() - self.last_time > 0.1:
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = +1
        if self.x < 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_left[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_right[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_right[self.current_image])

    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates

    def move(self):
        self.animate()
        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4
        if self.y > 0:
            self.jump_count -= 1
        co = self.coords()
        left = True; right = True; top = True; bottom = True
        falling = True
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0; bottom = False
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0; top = False
        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0; right = False
        elif self.x < 0 and co.x1 <=0:
            self.x =0; left = False
        for sprite in self.game.sprites:
            if sprite == self:
                continue
            sprite_co = sprite.coords()
            if top and self.y < 0: # and collided_top(co,sprite_co):
                self.y = -self.y; top = False
            if bottom and self.y > 0 and collided_bottom(self.y, co, sprite_co):
                self.y = sprite_co.y1 - co.y2
                if self.y < 0: self.y = 0
                bottom = False; top = False
            if bottom and falling and self.y == 0 \
                    and co.y2 < self.game.canvas_height and collided_bottom(1, co, sprite_co):
                falling = False
            if left and self.x < 0: # and collided_left(co, sprite_co):
                self.x = 0; left = False
                if sprite.endgame:
                    self.game.running = False
            if right and self.x > 0: # and collided_right(co, sprite_co):
                self.x = 0; right = False
                if sprite.endgame:
                    self.game.running = False
            if falling and bottom and self.y ==0 and co.y2 < self.game.canvas_height:
                self.y = 4
            self.game.canvas.move(self.image, self.x, self.y)
class DoorSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self,game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + (width /2), y + height)
        self.endgame = True

g = Game()          # Automatically run __init__() when it's' called

platform1 = PlatformSprite(g, PhotoImage(file="../static/img_stickman/Platform_03.png"),0, 480, 100, 10 )
platform2 = PlatformSprite(g, PhotoImage(file="../static/img_stickman/Platform_03.png"),150, 440, 100, 10 )
platform3 = PlatformSprite(g, PhotoImage(file="../static/img_stickman/Platform_03.png"),300, 400, 100, 10 )
platform4 = PlatformSprite(g, PhotoImage(file="../static/img_stickman/Platform_03.png"),300, 160, 100, 10 )
platform5 = PlatformSprite(g, PhotoImage(file="../static/img_stickman/Platform_02.png"),175, 350, 100, 10 )
platform6 = PlatformSprite(g, PhotoImage(file="../static/img_stickman/Platform_02.png"),50, 300, 100, 10 )
platform7 = PlatformSprite(g, PhotoImage(file="../static/img_stickman/Platform_02.png"),170, 120, 100, 10 )
platform8 = PlatformSprite(g, PhotoImage(file="../static/img_stickman/Platform_02.png"),45, 60, 100, 10 )
platform9 = PlatformSprite(g, PhotoImage(file="../static/img_stickman/platform_01.png"),170, 250, 32, 10 )
platform10 = PlatformSprite(g,PhotoImage(file="../static/img_stickman/platform_01.png"),230, 200, 32, 10 )

g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)

door = DoorSprite(g, PhotoImage(file="../static/img_stickman/door_01.png"), 45, 30, 40, 35)
sf = StickFigureSprite(g)

g.sprites.append(door)
g.sprites.append(sf)
g.mainloop()
