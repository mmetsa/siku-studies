import time

class Bomb:

    def go_off(self, timer):
        # count down from timer to 0 and print BOOM!
        for number in reversed(range(timer + 1)):
            print(number)
            time.sleep(1)
        print("BOOM!")

