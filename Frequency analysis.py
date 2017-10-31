import re

def get_key(diction, value):
    for k, v in diction.items():
        if v == value:
            return k


def write_by_count(file_in='text.txt', file_out='text_out.txt', reversed=False):
    if not file_in.endswith('.txt'):
        file_in += '.txt'
    if not file_out.endswith('.txt'):
        file_out += '.txt'

    with open(file_in, "r", encoding='utf-8') as file:
        text_raw = file.read()
    wordDict = {}
    text = [i.title() for i in re.split(r'[\W]', text_raw)]
    result = 'The approximate number of words in the text: ' + str(len(text)) + '\n'
    for word in text:
        if(word not in wordDict.keys()):
            wordDict[word] = text.count(word)

    for i in sorted(wordDict.values(), reverse=not reversed):
        result += get_key(wordDict, i) + ' - ' + str(i) + '\n'
        wordDict.pop(get_key(wordDict, i))

    with open(file_out, "w", encoding='utf-8') as file:
        file.write(result)


def write_alphabet_order(file_in='text.txt', file_out='text_out.txt', reversed=False):
    if not file_in.endswith('.txt'):
        file_in += '.txt'
    if not file_out.endswith('.txt'):
        file_out += '.txt'

    with open(file_in, "r", encoding='utf-8') as file:
        text_raw = file.read()
    text = [word.title() for word in re.split(r'[\W]', text_raw)]
    result = 'The approximate number of words in the text: ' + str(len(text)) + '\n'

    for word in sorted(set(text), reverse=reversed):
        result += word + ' - ' + str(text.count(word)) + '\n'

    with open(file_out, "w", encoding='utf-8') as file:
        file.write(result)


if __name__ == '__main__':
    write_by_count(reversed=False)   
    write_alphabet_order(reversed=False, file_out='text2')     

