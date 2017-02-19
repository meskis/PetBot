import PetBot
import sys


def main():
    try:
        PetBot.start()
    except KeyboardInterrupt:
        PetBot.stop()
        print "Keyboard interrupt detected, stopping..."
    except:
        print "Unexpected error:", sys.exc_info()[0]


# start your engines
if __name__ == '__main__':
    main()
