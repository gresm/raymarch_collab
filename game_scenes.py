from game import BaseScene, game
from raymarch_engine import RayMarcher, ShapeExecutor, circle, union, move, rectangle, rotate

import pygame as pg


class MainMenuScene(BaseScene):
    pass


V_RIGHT = pg.Vector2(1, 0)
V_DOWN = pg.Vector2(0, 1)


class TestScene(BaseScene):
    ray_marcher: RayMarcher
    distance_func: ShapeExecutor
    pos: pg.Vector2
    vel: pg.Vector2
    speed: float

    def init(self):
        # self.distance_func = rectangle((20, 1), (2, 2), 1)
        self.distance_func = union(circle(10), move(circle(15), (30, 30)), move(rotate(rectangle((10, 10)), 45),
                                                                                (-20, -20)))
        self.ray_marcher = RayMarcher(self.distance_func)
        self.pos = pg.Vector2(0, 0)
        self.vel = pg.Vector2(0, 0)
        self.speed = 5

    def draw(self, surface: pg.Surface):
        image = self.ray_marcher.map.repeat(2, axis=0).repeat(2, axis=1)
        surface.blit(pg.surfarray.make_surface(image), (200, 200))

    def update(self):
        pressed = pg.key.get_pressed()

        if pressed[pg.K_LEFT]:
            self.vel += V_RIGHT * self.speed

        if pressed[pg.K_RIGHT]:
            self.vel -= V_RIGHT * self.speed

        if pressed[pg.K_UP]:
            self.vel += V_DOWN * self.speed

        if pressed[pg.K_DOWN]:
            self.vel -= V_DOWN * self.speed

        self.pos += self.vel
        self.vel *= 0.7
        self.ray_marcher.update(tuple(self.pos))
