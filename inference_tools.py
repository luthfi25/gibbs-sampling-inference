import sys
import ast
import re
import random
from numpy.random import choice
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from collections import Counter

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer() 

def clean_text(text):
    # lower case
    text = text.lower()

    # remove fullstop punctuation mark, and remove 's
    text = re.sub(r'[?!,.()\'\"\\\/]', ' ', text)

    # replace numbers
    text = re.sub(r'\d', ' ', text)

    # strip empty space
    text = re.sub(r'\s\s+', ' ', text)

    #remove stopword
    word_token = word_tokenize(text)
    filtered = [lemmatizer.lemmatize(unicode(w, 'ascii', 'ignore')) for w in word_token if (not w in stop_words) and (len(w) >= 3)]
    space = " "
    text = space.join(filtered)

    return text

def inference(new_document, corpus_wide, num_topics, iteration, alpha, beta):
    document_topic_distribution = [0 for i in range(0, num_topics)]
    doc_list = new_document.split(' ')
    word_topic_map = dict()
    
    corpus_wide_by_topic = dict()
    for w,t in corpus_wide.iteritems():
        for i in range(0, len(t)):
            try:
                corpus_wide_by_topic[i] += t[i]
            except KeyError as e:
                corpus_wide_by_topic[i] = t[i]

    #Initalization, assign random topic
    for ind in range(0, len(doc_list)):
        word = doc_list[ind]

        chosen_topic = random.randint(0, num_topics-1)
        try:
            corpus_wide[word][chosen_topic] += 1
        except KeyError as e:
            corpus_wide[word] = [1 if i == chosen_topic else 0 for i in range(0,num_topics)]

        document_topic_distribution[chosen_topic] += 1
        corpus_wide_by_topic[chosen_topic] += 1
        word_topic_map[word + '_' + str(ind)] = chosen_topic

    while iteration > 0:
        for ind in range(0, len(doc_list)):
            word = doc_list[ind]
            chosen_topic = word_topic_map[word + '_' + str(ind)]
            
            #subtraction
            document_topic_distribution[chosen_topic] -= 1
            corpus_wide[word][chosen_topic] -= 1
            corpus_wide_by_topic[chosen_topic] -= 1

            #Document probabilty
            document_topic_probabilty = dict()
            sum_doc_topic = sum(document_topic_distribution)
            for i in range(0,len(document_topic_distribution)):
                document_topic_probabilty[i] = (float(document_topic_distribution[i]) + alpha) / (sum_doc_topic + (num_topics * alpha))

            #Corpus probabilty
            word_topic_probability = dict()
            num_vocab = len(corpus_wide.keys())
            for i in range(0,len(corpus_wide[word])):
                word_topic_probability[i] = (float(corpus_wide[word][i]) + beta) / (corpus_wide_by_topic[i] + (num_vocab * beta))

            topic_prob = [0 for i in range(0, num_topics)]
            max_prob = (0, 0)
            #Highest Probabilty
            for i in range(0, num_topics):
                doc_prob = document_topic_probabilty[i]
                word_prob = word_topic_probability[i]
                topic_prob[i] = doc_prob * word_prob
            
            sum_topic_prob = sum(topic_prob)
            norm_topic_prob = [p / sum_topic_prob for p in topic_prob]
            new_topic_prob = choice(norm_topic_prob, p=norm_topic_prob)
            max_prob = (norm_topic_prob.index(new_topic_prob), new_topic_prob)

            #Addition
            word_topic_map[word + '_' + str(ind)] = max_prob[0]
            document_topic_distribution[max_prob[0]] += 1
            corpus_wide[word][max_prob[0]] += 1
            corpus_wide_by_topic[max_prob[0]] += 1

            #FOR DEBUGGING PURPOSE
            # if max_prob[0] != chosen_topic:
                # print("Topic change!! " + word + " from " + str(chosen_topic) + " to " + str(max_prob[0]))

            iteration -= 1

    return word_topic_map, document_topic_distribution

            
#Input: Gibbs Sampling Result
file_name = sys.argv[1] if len(sys.argv) >= 2 else "none"
file_data = open(file_name, "r")
gibbs_result_str = file_data.readlines()
gibbs_result = ast.literal_eval(gibbs_result_str[0])

file_name = sys.argv[2] if len(sys.argv) >= 3 else "none"
file_data = open(file_name, "r")
vocabulary = [s.split(' ') for s in file_data.readlines()]

corpus_wide = dict()

for v in vocabulary:
    corpus_wide[v[0]] = gibbs_result[vocabulary.index(v)]

#New Document
file_name = sys.argv[3] if len(sys.argv) >= 4 else "none"
file_data = open(file_name, "r")
document_raw = file_data.readlines()
document = clean_text(document_raw[0])

num_topics = sys.argv[4] if len(sys.argv) >= 8 else "none"
iteration = sys.argv[5] if len(sys.argv) >= 8 else "none"
alpha = sys.argv[6] if len(sys.argv) >= 8 else "none"
beta = sys.argv[7] if len(sys.argv) >= 8 else "none"

random.seed(1) #temp
#Run Inference on new document
word_topic_map, document_topic_distribution = inference(document, corpus_wide, int(num_topics), int(iteration), float(alpha), float(beta))

#Document probabilty FINAL
document_topic_probabilty = dict()
sum_doc_topic = sum(document_topic_distribution)
for i in range(0,len(document_topic_distribution)):
    document_topic_probabilty[i] = float(document_topic_distribution[i]) / sum_doc_topic

print(word_topic_map)
print(document_topic_probabilty)