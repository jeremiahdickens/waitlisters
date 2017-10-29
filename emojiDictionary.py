dict = [];

wordFile = 'words.txt'
file = open(wordFile)

#Parses file and creates dictionary
for line in file:
    stuff = line.strip().split("=");
    line = next(file)
    thing = line.strip();
    dict.append((stuff,':%s:'%thing));

lastHadEmojiBool = False;

#Takes string to check for emojis as parameter
#Returns tuple String: modifiedString
def toEmojiString(str):
    original = str;
    for tuple in dict:
        for stuff in tuple[0]:
            str = str.replace(stuff, tuple[1]);
    global lastHadEmojiBool;
    lastHadEmojiBool = not str.__eq__(original);
    return str;

#Determines whether the last string evaluated contained an emoji
def lastHadEmoji():
    global lastHadEmojiBool;
    return lastHadEmojiBool;
