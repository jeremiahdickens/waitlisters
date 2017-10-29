import re;
dict = [];

wordFile = 'dictionary.txt'
file = open(wordFile)

#Parses file and creates dictionary
for line in file:
    stuff = line.strip().split("=");
    #Sorts to descending by String length
    stuff.sort(key=lambda x : len(x),reverse=True);
    line = next(file).strip();
    thing = line.strip();
    dict.append((stuff,':%s:'%thing));

lastHadEmojiBool = False;
#Takes string to check for emojis as parameter
#Returns tuple String: modifiedString
def toEmojiString(str):
    original = str;
    for tuple in dict:
        for stuff in tuple[0]:
            #REGEX THING DO NOT CHANGE
            #MY LIFE WAS PUT INTO THIS
            temp = str;
            escapedStuff = re.sub(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\<\>\|\:\-])', r'\\\1', stuff);
            pattern = re.compile('( |^|$|\'|\"|\.|,|\\|/|\?|\;|\]|\[)'+escapedStuff+'( |^|$|\'|\"|\.|,|\\|/|\?|\;|\]|\[)', flags=re.I);
            str = pattern.sub(r'\1'+tuple[1]+r'\2', str);
    global lastHadEmojiBool;
    lastHadEmojiBool = not str.__eq__(original);
    return str;

#Determines whether the last string evaluated contained an emoji
def lastHadEmoji():
    global lastHadEmojiBool;
    return lastHadEmojiBool;
