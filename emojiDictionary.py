import re;
dict = [];

wordFile = 'words.txt'
file = open(wordFile)

#Parses file and creates dictionary
for line in file:
    stuff = line.strip().split("=");
    #Sorts to descending by String length
    stuff.sort(key=lambda x : len(x),reverse=True);
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
            #\\b is a built in regex thing that is used to match word start/end
            #(?!:) next group is not :
            pattern = re.compile(r'(?!:)(\b)'+stuff+r'(?!:)(\b)');
            str = re.sub(pattern, tuple[1], str);
    global lastHadEmojiBool;
    lastHadEmojiBool = not str.__eq__(original);
    return str;

#Determines whether the last string evaluated contained an emoji
def lastHadEmoji():
    global lastHadEmojiBool;
    return lastHadEmojiBool;
