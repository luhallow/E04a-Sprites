#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Random Animal Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.blue_4)

        self.animal_list = arcade.SpriteList()
        


    def setup(self):
        animals = ['bear','buffalo','chick','chicken','cow','crocodile','dog','duck','elephant','frog','giraffe','goat','gorilla','hippo','horse','monkey','moose','narwhal','owl','panda','parrot','penguin','pig','rabbit','rhino','sloth','snake','walrus','whale','zebra']

        animal = 'panda'
        x = 400
        y = 300
        self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y
        self.animal_list.append(self.animal_sprite)

        animal = 'bear'
        x = 430
        y = 310
        self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y
        self.animal_list.append(self.animal_sprite)

        animal = 'chicken'
        x = 230
        y = 200
        self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y
        self.animal_list.append(self.animal_sprite)

        animal = 'moose'
        x = 400
        y = 100
        self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y
        self.animal_list.append(self.animal_sprite)

        animal = 'hippo'
        x = 200
        y = 130
        self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y
        self.animal_list.append(self.animal_sprite)

        animal = 'narwhal'
        x = 100
        y = 100
        self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y
        self.animal_list.append(self.animal_sprite)

        animal = 'cow'
        x = 120
        y = 500
        self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y
        self.animal_list.append(self.animal_sprite)

        animal = 'crocodile'
        x = 250
        y = 500
        self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y
        self.animal_list.append(self.animal_sprite)

        animal = 'panda'
        x = 200
        y = 200
        self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y
        self.animal_list.append(self.animal_sprite)

        animal = 'duck'
        x = 110
        y = 530
        self.animal_sprite = arcade.Sprite("assets/{animal}.png".format(animal=animal), 0.5)
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y
        self.animal_list.append(self.animal_sprite)








      

    def on_draw(self):
        arcade.start_render()
        self.animal_list.draw()


    def update(self, delta_time):
        pass


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()