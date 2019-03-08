import gensim
from gensim.models import Word2Vec
from scipy import spatial
model = Word2Vec.load('data/ko.bin')
import numpy as np

def sim_word(sample_word,topn):
    print("**************** top " , topn, 'similar_word with' ,sample_word, '*****************\n')
    print(model.most_similar(positive=[sample_word], topn=5))


sim_word('아이유',5)
sim_word('컴퓨터',5)
sim_word('사랑',5)




def sim(sample_word,most_similar_word):
    per=model.wv.rank(sample_word, most_similar_word)

    print(sample_word, "  " , most_similar_word, '=' ,per)

# print(model.most_similar(positive=['이승기'], topn=5))

# s1 = '배고프다'
# s2 = '감사합니다 최고에요'

# questions=["안녕하세요","저렴한 식당으로 안내해줘 ","저렴한 가격으로 여섯명이 갈 수있는 파리에 있는 식당 예약하고 싶어", "안녕하세요 어떻게 도와드릴까요", "예약을 진행해드리도록 하겠습니다", "고마워 너가 최고야", "적당한 가격으로 바꿔줘", "다른 리스트를 보여드릴게요", '아니 별로야']#512?

# q_vec=[]
# index2word_set = set(model.wv.index2word)
# len(index2word_set)
# def avg_feature_vector(sentence, model, num_features, index2word_set):
#     words = sentence.split()
#     feature_vec = np.zeros((num_features, ), dtype='float32')
#     n_words = 0
#     for word in words:
#         if word in index2word_set:
#             n_words += 1
#             feature_vec = np.add(feature_vec, model[word])
#     if (n_words > 0):
#         feature_vec = np.divide(feature_vec, n_words)
#     return feature_vec

# s1_afv = avg_feature_vector(s1, model=model, num_features=100, index2word_set=index2word_set)
# s2_afv = avg_feature_vector(s2, model=model, num_features=100, index2word_set=index2word_set)

# for i in questions:
#     s1_afv = avg_feature_vector(i, model=model, num_features=100, index2word_set=index2word_set)
#     q_vec.append(s1_afv)

# sim_list=[]
# for i in q_vec:
#     sim = 1 - spatial.distance.cosine(i, s2_afv)
#     sim_list.append(sim)
# print(sim_list)
# print('top %d questions similar to "%s"' % (2, (s2)))
# print(questions[sim_list.index(max(sim_list))])




# score = np.sum(q_vec * s2_afv, axis=1)
# topk_idx = np.argsort(score)[::-1][:2]
# print('top %d questions similar to "%s"' % (2, (s2)))
# for idx in topk_idx:
#     print('> %s\t%s' % (('%.1f' % score[idx]), (questions[idx])))

# print(sim)
# print(len(index2word_set))