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
    delim = ' \'\".,\\/?;][{}()';
    i = -1;
    while i < len(str):
        if(i==-1 or str[i] in list(delim)):
            for tuple in dict:
                for stuff in tuple[0]:
                    if(i+1+len(stuff) <= len(str) and (i+1+len(stuff)==len(str) or str[i+1+len(stuff)] in list(delim))):
                        a = str[i+1:].lower() if i+1+len(stuff) == len(str) else str[i+1:i+1+len(stuff)].lower();
                        b = stuff.lower();
                        if(a==b):
                            str = str[0:i+1]+tuple[1]+(str[i+1+len(stuff):] if i+1+len(stuff)<len(str) else '');
        i+=1;
    #------OLD CODE------
    #for tuple in dict:
    #    for stuff in tuple[0]:
    #        #REGEX THING DO NOT CHANGE
    #        #MY LIFE WAS PUT INTO THIS
    #        temp = str;
    #        escapedStuff = re.sub(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\!\<\>\|\:\-])', r'\\\1', stuff);
    #        pattern = re.compile('( |^|$|\'|\"|\.|,|\\|/|\?|\;|\]|\[)'+escapedStuff+'( |^|$|\'|\"|\.|,|\\|/|\?|\;|\]|\[)', flags=re.I);
    #        str = pattern.sub(r'\1'+tuple[1]+r'\2', str);
    global lastHadEmojiBool;
    lastHadEmojiBool = not str.__eq__(original);
    return str;

#Determines whether the last string evaluated contained an emoji
def lastHadEmoji():
    global lastHadEmojiBool;
    return lastHadEmojiBool;
