import nltk
import os
import codecs
import argparse
import numpy as np


import gensim
import pickle
from gensim.models import Word2Vec
from konlpy.tag import Twitter
from sklearn.manifold import TSNE
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import pandas as pd

model = Word2Vec.load('data/ko.bin')

path = 'c:/windows/fonts/malgun.ttf'

font_name = fm.FontProperties(fname=path, size=50).get_name()
plt.rc('font', family=font_name)


vocab = list(model.wv.vocab)
X = model[vocab]

tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)

df = pd.DataFrame(X_tsne, index=vocab, columns=['x', 'y'])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(df['x'], df['y'],s=0.5)

i=1
for word, pos in df.iterrows():
    if i%1000==0: 
        ax.annotate(word, pos)
    i+=1
print(i)

plt.show()