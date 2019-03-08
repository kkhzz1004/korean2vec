from konlpy.tag import Twitter
from collections import Counter
from tqdm import tqdm
import regex

def get_tags(open_text_file):
    nlp = Twitter()
    nouns_list = []
    toekn_list =[]
    i=0
    for line in open_text_file:
    # for line in tqdm(open_text_file):
        print(line)
        text = line
        text=regex.sub(u"[\n]", " ", text)
        n = nlp.nouns(text)
        token =nlp.morphs(text)
        for value in n:
            nouns_list.append(value)
        for j in token:
            toekn_list.append(j)
        # if i == 400:
        #     break
        # else:
        #     i+=1
    return nouns_list,toekn_list
 
def main():
    text_file_name = "data/ko.txt"
    noun_count = 100
    token_file_name = "token.txt"
    output_file_name = "noun_count.txt"
    output2_file_name = "token_count.txt"
    noun_file_name = "noun.txt"
    
    open_text_file = open(text_file_name, 'r', encoding='utf-8')
    open_output_file = open(output_file_name, 'w', encoding='utf-8')
    token_output_file = open(token_file_name, 'w', encoding='utf-8')
    noun_output_file = open(noun_file_name, 'w', encoding='utf-8')
    open_output2_file = open(output2_file_name, 'w', encoding='utf-8')
    
    

    nouns_list ,toekn_list = get_tags(open_text_file)
    
    token_output_file.write(str(toekn_list))
    noun_output_file.write(str(nouns_list))

    count = len(nouns_list)
    tokens =  len(toekn_list)
    print('number of nouns: ',count)
    print('number of token: ',tokens)

    count = Counter(nouns_list)
    tokens =  Counter(toekn_list)


    tags2 = []
    tags3 = []
    for n, c in tqdm(count.most_common(noun_count)):
        temp = {'tag': n, 'count': c}
        tags2.append(temp)
    
    for tag in tqdm(tags2):
        noun = tag['tag']
        count = tag['count']
        open_output_file.write('{} {}\n'.format(noun, count))

    for n, c in tqdm(tokens.most_common(noun_count)):
        if c != '\n':
            temp = {'tag': n, 'tokens': c}
            tags3.append(temp)
    
    for tag in tqdm(tags3):
        noun = tag['tag']
        tokens = tag['tokens']
        open_output2_file.write('{} {}\n'.format(noun, tokens))
    
    open_output_file.close()
    open_text_file.close()
 
 
if __name__ == '__main__':
    main()

