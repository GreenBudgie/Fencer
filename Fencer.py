import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Fencer")
        arcade.set_background_color(arcade.color.WHITE)
        # 14 MAX
        self.chain = FenceChain("CASFASFASFASSF")
        self.background = arcade.Sprite("sprites\\background.png")
        self.background.alpha = 200
        self.background.center_x = SCREEN_WIDTH / 2
        self.background.center_y = SCREEN_HEIGHT / 2

    def update(self, delta_time: float):
        pass

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.chain.draw()
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


def main():
    Game()
    arcade.run()


if __name__ == "__main__":
    main()
