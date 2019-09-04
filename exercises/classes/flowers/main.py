from arrangements import ValentinesDay
from flowers import Rose
from flowers import Daisy

if __name__ == "__main__":
    for_beth = ValentinesDay()
    red_rose = Rose("red", 10, 10, False, 10)
    blue_rose = Rose("blue", 8, 12, False, 4)
    pink_rose = Rose("pink", 12, 8, False, 6)
    yellow_daisy = Daisy("yellow", 5, 4, True, 6)

    for_beth.enhance(red_rose)
    for_beth.enhance(blue_rose)
    for_beth.enhance(pink_rose)
    for_beth.enhance(yellow_daisy)