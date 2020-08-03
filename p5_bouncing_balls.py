from p5 import *

class Mover:

    def __init__(self, loc, size):
        self.loc = loc
        self.vel = Vector(random_uniform(-10, 10), random_uniform(-10, 10))
        self.acl = Vector(0,0)

        self.size = size
        self.mass = self.size / 1.5

    def update(self):
        # self.air_drag()
        self.vel += self.acl
        self.loc += self.vel

        self.at_side()

        self.acl *= 0

    def apply_force(self, f):
        force = f / self.mass
        self.acl += force

    def air_drag(self, mu=0.05):
        drag_mag = self.vel.magnitude * mu
        drag = Vector.from_angle(self.vel.angle) * -1 * drag_mag
        self.apply_force(drag)

    def at_side(self):
        if(self.loc.x <= self.size/2):
            self.loc.x = self.size/2
            self.vel.x *= -1

        if(self.loc.x >= width - self.size/2):
            self.loc.x = width - self.size/2
            self.vel.x *= -1

        if (self.loc.y <= self.size/2):
            self.loc.y = self.size/2
            self.vel.y *= -1

        if(self.loc.y >= height - self.size/2):
            self.loc.y = height - self.size/2
            self.vel.y *= -1

    def show(self):
        fill(200, 50, 50)
        no_stroke()
        circle(self.loc, self.size)



movers = []
mover_num = 5

for i in range(mover_num):
    movers.append(Mover(Vector(random_uniform(width, 0), random_uniform(height, 0)), random_uniform(50, 5)))


def setup():
    size(600, 600)
    title("p5 bouncing balls")


def draw():
    background(204)

    gravity = Vector(0, 0.98)
    wind = Vector(0.1, 0)

    for mover in movers:
        mover.apply_force(gravity)
        mover.apply_force(wind)
        mover.update()
        mover.show()
    # if (prev_vel != None):
    #     if (mover.vel == prev_vel and hit_terminal_vel == False):
    #         hit_terminal_vel = True
    #     else:
    #         hit_terminal_vel = False

    #     if(hit_terminal_vel == True):
    #         print("Hit terminal velocity at " + str(i))
    # prev_vel = mover.vel

    # if (frame_count >= 1200):
    #     exit()


run()