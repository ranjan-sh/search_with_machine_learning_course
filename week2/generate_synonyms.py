import fasttext

title_model = fasttext.load_model('/workspace/datasets/fasttext/title_model_100.bin')
top_words = open("/workspace/datasets/fasttext/top_words.txt", 'r')
synonyms = open("/workspace/datasets/fasttext/synonyms.csv", 'w')
syn_threshold = 0.75


for word in top_words.readlines():
    syn_list = title_model.get_nearest_neighbors(word)
    syn_list_filtered = [syn_word[1] for syn_word in syn_list if syn_word[0] >= syn_threshold]

    # syn_list always contains the original word
    if len(syn_list_filtered) > 1:
        syn_list_outout = ','.join(syn_list_filtered)
        print(syn_list_outout)
        syn_list_outout = syn_list_outout + '\n'
        synonyms.write(syn_list_outout)
    