# White Elephant Gift Exchange Name Generator
# About the game: https://en.wikipedia.org/wiki/White_elephant_gift_exchange

#!/usr/bin/python
# Hand-crafted with love by Sandeep Rao

import random
import os

class Elephant:

    defaultFileLocation = '~/Downloads/elephant.txt'
    names = []
    index = 0

    def run(self):
        print "Welcome to White Elephant! \n"
        
        while 1:
            fileLocation = str(raw_input("Enter path for file with names [Press enter for default location (~/Downloads/elephant.txt)] > "))
            if (fileLocation is ''):
                fileLocation = self.defaultFileLocation
            if os.path.exists(fileLocation):
                break
            else:
                print "File not found."
                continue
        
        print "Reading names from " + str(fileLocation)
        f = open(fileLocation, 'r')
        rawNames = f.read().split('\n')
        print "Here are the participants today: "
        for name in rawNames:
            print name

        # Randomize names
        self.names = rawNames
        random.shuffle(self.names)

        print "\n\nBeginning game. You can use the following commands:\n n - generate next name \n b - play from beginning (reshuffle names again) \n q - quit game (this will lose the order if you quit mid game) \n\n"
        while 1:
            cmd = str(raw_input("command [n/b/q]> "))
            if (cmd == 'q'):
                while 1:
                    cmd2 = str(raw_input("Quit Game. Are you sure [y/n]? "))
                    if (cmd2 == 'y' or cmd == 'yes'):
                        exit(0)
                    elif (cmd2 == 'n' or cmd == 'no'):
                        break
                    else:
                        continue
            elif (cmd == 'n'):
                print "Next Name: " + self.names[self.index].upper()
                self.index = self.index + 1
                if (self.index >= len(self.names)):
                    print "\nAll names are drawn! Hope you had fun!!"
                    exit(0)
            elif (cmd == 'b'):
                while 1:
                    cmd2 = str(raw_input("Play from beginning. Are you sure [y/n]? "))
                    if (cmd2 == 'y' or cmd == 'yes'):
                        self.index = 0
                        random.shuffle(self.names)
                        print "Game reset. Beginning from the top!"
                        break
                    elif (cmd2 == 'n' or cmd == 'no'):
                        break
                    else:
                        continue
            else:
                continue

if __name__ == '__main__':
    elephant = Elephant()
    elephant.run()
