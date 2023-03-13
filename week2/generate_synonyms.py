import fasttext

title_model = fasttext.load_model('/workspace/datasets/fasttext/title_model_100.bin')
top_words = open("/workspace/datasets/fasttext/top_words.txt", 'r')
synonyms = open("/workspace/datasets/fasttext/synonyms.csv", 'w')


for word in top_words.readlines():
    
