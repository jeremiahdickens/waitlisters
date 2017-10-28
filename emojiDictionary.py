dict = [];

wordFile = 'words.txt'
file = open(wordFile)

for line in file:
    stuff = line.strip().split("=");
    line = next(file)
    thing = line.strip();
    dict.append((stuff,':%s:'%thing));

def toEmojiString(str):
    for tuple in dict:
        for stuff in tuple[0]:
            str = str.replace(stuff, tuple[1]);
    return str;

print(dict);