from PetBot import PetBot
import sys


def main():
    global bot

    try:
        bot = PetBot()
        bot.start()
    except KeyboardInterrupt:
        bot.stop()
        print "Keyboard interrupt detected, stopping..."
    except:
        print "Unexpected error:", sys.exc_info()[0]


# start your engines
if __name__ == '__main__':
    main()
