import re
import string
import pandas as pd
import pickle


test = pd.read_parquet('data/task1_test_for_user.parquet')

tfidf = pickle.load(open('tfidf', 'rb'))
clf = pickle.load(open('clf_task1', 'rb'))

def replace_re(text, regexp, inplace): 
    return regexp.sub(inplace, text)

test['item_name'] = test['item_name'].apply(lambda x: x.replace("\xa0", ' '))
regex_punc = re.compile('[%s]'%re.escape('.,!?'))
test['item_name'] = test['item_name'].apply(lambda x: replace_re(x, regex_punc, ' '))
test['item_name'] = test['item_name'].apply(lambda x: x.strip())
regex_seq_spaces = re.compile(' {2,}')
test['item_name'] = test['item_name'].apply(lambda x: replace_re(x, regex_seq_spaces, ' '))
test['item_name'] = test['item_name'].apply(lambda x: x.lower())

X_test = tfidf.transform(test.item_name)

pred = clf.predict(X_test)

res = pd.DataFrame(pred, columns=['pred'])
res['id'] = test['id']

res[['id', 'pred']].to_csv('answers.csv', index=None)
