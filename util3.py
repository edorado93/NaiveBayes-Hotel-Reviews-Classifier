import string
stop_words = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours',
              'ourselves', 'you', "you're", "you've", "you'll",
              "you'd", 'your', 'yours', 'yourself', 'yourselves',
              'he', 'him', 'his', 'himself', 'she', "she's", 'her',
              'hers', 'herself', 'it', "it's", 'its', 'itself',
              'they', 'them', 'their', 'theirs', 'themselves', 'what',
              'which', 'who', 'whom', 'this', 'that', "that'll", 'these',
              'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
              'being', 'have', 'has', 'had', 'having', 'do', 'does',
              'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
              'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by',
              'for', 'with', 'about', 'against', 'between', 'into', 'through',
              'during', 'before', 'after', 'above', 'below', 'to', 'from',
              'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
              'again', 'further', 'then', 'once', 'here', 'there', 'when',
              'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
              'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
              'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
              'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now',
              'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn',
              "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't",
              'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',
              "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't",
              'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won',
              "won't", 'wouldn', "wouldn't"}

common_words = {"a","the","is","was","were","that","their","should","can","could","must","they","their","get","got","put",
"keep","it","on","for","in","about","upon","you","i","we","would","and","will","number","be","he","she","it","their"
"that","ok","k","one","two","three","four","five","six","seven","eight","nine","up","down","us","but","all","where"
,"been","of","do","dont","later","make","made","ans","at","our","him","his","her","else","did","does","done","had"
"has","have","to","than","with","by","or","makes","likes","liked","made","kmow","my","from","went","told","only","this"
,"much","me","mine","im","say","said","spoke","men","women","since","back","before","okay","an","what","where","who","whom"
,"also","if","other","yet","go","such","throughout","through","though","as","when","oh","so","here","after","them","then",
"what","man","woman","there","let","now","bed","come","came","its","ill","ive","were""there","hyatt","regency","chicago","husband","summer","vacation",
"couldnt","had","some","seems","north","michigan","avenue","are","drake","westin","concierge","august","fiancee","city",
"even","while","see",""}

translator = str.maketrans('', '', string.punctuation)

def remove_punctuation(review):
    return review.translate(translator)

def remove_stop_words(review):
    new_review = []
    for word in review.split():
        if word not in stop_words and word not in common_words:
            new_review.append(word)

    return " ".join(new_review)