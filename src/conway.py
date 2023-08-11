import pyxel
from copy import deepcopy
from sum_neighbors import sum_neighbors

# grid options
RECT_SIZE = 4
MAX_RECT = 128

# game states
MENU = -1
SET_UP = 0
PLAYING = 1

# UI
TEXT_COLOR = 10

class Conway:
    def __init__(self):
        pyxel.init(256, 256, "Conway's Game of Life")
        self.rect_color = [[0 for i in range(MAX_RECT)]
                           for j in range(MAX_RECT)]

        self.game_state = MENU
        self.frame_set = 1

        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update_state(self):
        new_array = deepcopy(self.rect_color)

        for i in range(MAX_RECT):
            for j in range(MAX_RECT):
                neighbors_alive = int(sum_neighbors(
                    self.rect_color, i, j, MAX_RECT - 1) / 7)

                if self.rect_color[i][j] == 7:
                    # the grid is alive
                    if (neighbors_alive < 2) or (neighbors_alive > 3):
                        # die
                        new_array[i][j] = 0
                else:
                    if neighbors_alive == 3:
                        # resurrect
                        new_array[i][j] = 7

        self.rect_color = new_array

    def check_mouse_input(self):
        i = pyxel.mouse_x // RECT_SIZE
        j = pyxel.mouse_y // RECT_SIZE

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            self.rect_color[i][j] = 7
        elif pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            self.rect_color[i][j] = 0

    def update(self):

        if self.game_state == MENU and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.game_state = SET_UP

        if pyxel.btnp(pyxel.KEY_1):
            self.frame_set = 1
        if pyxel.btnp(pyxel.KEY_2):
            self.frame_set = 5
        if pyxel.btnp(pyxel.KEY_3):
            self.frame_set = 10
        if pyxel.btnp(pyxel.KEY_4):
            self.frame_set = 15

        if pyxel.btnp(pyxel.KEY_R):
            self.game_state = PLAYING
        if pyxel.btnp(pyxel.KEY_S):
            self.game_state = SET_UP

        if self.game_state == PLAYING and pyxel.frame_count % self.frame_set == 0:
            self.update_state()
        elif self.game_state == SET_UP:
            self.check_mouse_input()

    def draw_menu(self):
        pyxel.text(64, 64, "Conway's Game of Life", TEXT_COLOR)
        pyxel.text(64 + 20, 84, "Controls", TEXT_COLOR)
        pyxel.text(64 + 20, 90, "1-4 to change speed", TEXT_COLOR)
        pyxel.text(64 + 20, 98, "R to run the game", TEXT_COLOR)
        pyxel.text(64 + 20, 106, "S to run the game", TEXT_COLOR)
        pyxel.text(64 + 20, 114, "Left/Right Click on a cell to draw", TEXT_COLOR)

        pyxel.text(64, 145, "Click to start", TEXT_COLOR)

    def draw_state(self):
        if self.game_state == PLAYING:
            pyxel.text(2, 2, "Mode: Playing", TEXT_COLOR)
        elif self.game_state == SET_UP:
            pyxel.text(2, 2, "Mode: Set Up", TEXT_COLOR)

    def draw(self):

        if self.game_state == MENU:
            pyxel.cls(0)
            self.draw_menu()
        else:
            for i in range(MAX_RECT):
                for j in range(MAX_RECT):
                    pyxel.rect(i * RECT_SIZE, j * RECT_SIZE, RECT_SIZE,
                               RECT_SIZE, self.rect_color[i][j])
            self.draw_state()

Conway()
