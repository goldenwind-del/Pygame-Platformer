from random import randint
width, height = 960, 540

def level_gen():
    final_platformx, final_platformy = randint(600,700), randint(50,150)
    finnish_x, finnish_y = final_platformx, final_platformy - 110
    return{
    "platforms": [
        (randint(200,400), randint(350,450), 120, 20, (0, 255, 0)),
        (randint(300,500), randint(250,300), 120, 20, (0, 255, 0)),
        (randint(500,600), randint(150,200), 120, 20, (0, 255, 0)),
        (final_platformx, final_platformy, 120, 20, (0, 255, 0)),
    ],
    "walls": [
    ],
    "finnish": [
        (finnish_x, finnish_y, 110, 110)
    ],
    "player": [
        (0, 490, 25, 25, (255, 0, 0),width, height)
    ],
    }

levels = {
    1: {
        "platforms": [
            (850, 200, 120, 20, (0, 255, 0)),
            (525, 200, 100, 20, (0, 255, 0)),
            (325, 300, 100, 20, (0, 255, 0)),
            (125, 400, 100, 20, (0, 255, 0)),
        ],
        "walls": [
            (800,200,50, 400, (0, 0, 255)),
        ],
        "finnish": [
            (850,430,110,110)
        ],
        "player": [
            (0, 490, 25, 25, (255, 0, 0),width, height)
        ],
    },
    2: level_gen()

    }
