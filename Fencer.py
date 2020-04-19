import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
LEFT_SPACING = 200


class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Fencer")
        arcade.set_background_color(arcade.color.WHITE)
        # 14 MAX
        self.chain = FenceChain("КОРОВА")
        self.top_chain = TopFenceChain()
        self.background = arcade.Sprite("sprites\\background.png")
        self.background.alpha = 200
        self.background.center_x = SCREEN_WIDTH / 2
        self.background.center_y = SCREEN_HEIGHT / 2

    def update(self, delta_time: float):
        self.chain.update(self._mouse_x, self._mouse_y)
        pass

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.chain.draw()
        self.top_chain.draw()
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        pass


class Fence:

    def __init__(self, letter: str):
        self._letter = letter
        self.sprite = arcade.Sprite("sprites\\fence.png")

    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self, value):
        self._letter = value

    def draw(self, x: float, y: float):
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.sprite.draw()
        arcade.draw_text(self.letter, x, y - 8, arcade.color.BLACK, font_size=40, font_name="arial", anchor_x="center",
                         anchor_y="center")
        pass

    def is_hovered(self, x: float, y: float):
        return self.sprite.center_x - self.sprite.width / 2 < x < self.sprite.center_x + self.sprite.width / 2 and \
               self.sprite.center_y - self.sprite.height / 2 < y < self.sprite.center_y + self.sprite.height / 2

    def on_mouse_pressed(self):

        pass


class TopFence(Fence):

    pass


class TopFenceChain:

    def __init__(self):
        self.fence_list = []

    def draw(self):
        for i in range(0, len(self.fence_list)):
            fence = self.fence_list.__getitem__(i)
            fence.draw(i * fence.sprite.width + LEFT_SPACING, SCREEN_HEIGHT - 128)

    def add_fence(self, letter: str):
        if len(self.fence_list) < 15:
            self.fence_list.append(TopFence(letter))

    def remove_last_fence(self):
        if len(self.fence_list) > 0:
            self.fence_list.__delitem__(len(self.fence_list) - 1)

    def clear_fences(self):
        self.fence_list.clear()

    def update(self, mouse_x: float, mouse_y: float):
        for fence in self.fence_list:
            if fence.is_hovered(mouse_x, mouse_y):
                fence.sprite.color = arcade.color.COLUMBIA_BLUE
            else:
                fence.sprite.color = arcade.color.WHITE


class FenceChain:

    def __init__(self, word: str):
        self.fence_list = []
        for letter in word:
            self.fence_list.append(Fence(letter))

    def draw(self):
        for i in range(0, len(self.fence_list)):
            fence = self.fence_list.__getitem__(i)
            first_fence_x = (SCREEN_WIDTH / 2) - (fence.sprite.width / 2) * (len(self.fence_list) - 1)
            fence.draw(i * fence.sprite.width + first_fence_x, 128)
        pass

    def update(self, mouse_x: float, mouse_y: float):
        for fence in self.fence_list:
            if fence.is_hovered(mouse_x, mouse_y):
                fence.sprite.color = arcade.color.COLUMBIA_BLUE
            else:
                fence.sprite.color = arcade.color.WHITE


def main():
    Game()
    arcade.run()


if __name__ == "__main__":
    main()
