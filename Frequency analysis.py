import re

def get_key(diction, value):
    for k, v in diction.items():
        if v == value:
            return k

file_in = open("text.txt", "r", encoding = 'utf-8')
file_out = open("text_out.txt", "w", encoding = 'utf-8')

text_raw = file_in.read()

wordDict = {}
text = [i.title() for i in re.split(r'[\W]', text_raw)]
words = len(text)


def main():    
    result = ''
    result = 'The approximate number of words in the text: ' + str(words) + '\n'
    for i in text:
    	if(i not in wordDict.keys()):
    		wordDict[i] = text.count(i)
    for i in sorted(wordDict.values(), reverse=True):
        result += get_key(wordDict, i) + ' - ' + str(i) + '\n'
        wordDict.pop(get_key(wordDict, i))

main()        
file_out.write(result)

file_in.close()
file_out.close()
