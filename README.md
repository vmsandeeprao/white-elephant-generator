# White Elephant Gift Exchange Name Generator
About the game: https://en.wikipedia.org/wiki/White_elephant_gift_exchange

This is a simple script that generates names of friends in random order to pick a gift for White Elephant (aka Yankee Swap). I'm creating this since I did not see any White Elephant Name Generators out there. There are only Secret Santa generators. 


## Instructions on how to run the game

1. To use this program, simply create a text file with all the names of friends you want to play White Elephant with. Enter one name per line. If you create the file in your Downloads folder with name "elephant.py", then you won't need to enter the filepath. 

2. Simply run the script "elephant.py" in the command line terminal ('python elephant.py') and pass in the path to the file. You can then use command 'n' to have the script tell who should play the next game. 


## How the game looks

/Downloads/$ python elephant.py 
Welcome to White Elephant! 

Enter path for file with names [Press enter for default location (~/Downloads/elephant.txt)] > 
Reading names from ~/Downloads/elephant.txt
Here are the participants today: 
john
david
ive
steve
ellen


Beginning game. You can use the following commands:
 n - generate next name 
 b - play from beginning (reshuffle names again) 
 q - quit game (this will lose the order if you quit mid game)

command > n
Next Name: STEVE
command > n
Next Name: ELLEN
command > n
Next Name: JOHN
command > n
Next Name: IVE
command > n
Next Name: DAVID

All names are drawn! Hope you had fun!!