from math import log # IDF 계산을 위해

def split(docs):
  return list(set(w for doc in docs for w in doc.split()))

def tf(t, d):
    return d.count(t)

def idf(t,docs):
    N = len(docs)
    df = 0
    for doc in docs:
        df += t in doc
    return log(N/(df + 1))

def tfidf(t, d,docs):
  return tf(t,d)* idf(t,docs)

  
