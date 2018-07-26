import math
import sys
import util3
class NaiveBayesClassifier:
    def __init__(self, input_file):
        self.file = input_file
        self.model_file = "nbmodel.txt"

        """ Dictionaries required for the model. """
        self.negative_word_count = {}
        self.positive_word_count = {}
        self.true_word_count = {}
        self.fake_word_count = {}
        self.dictionaries = {"t" : self.true_word_count, "f" : self.fake_word_count,
                             "p" : self.positive_word_count, "n" : self.negative_word_count}

        """ Variables required for the model """
        self.variables = {"t" : 0, "f" : 0,
                          "p" : 0, "n" : 0}


        self.prior_probabilities = {"t" : 0, "f" : 0,
                                     "p" : 0, "n" : 0}
        self.unique_words = set()

    def update_priors(self, review):
        self.variables[review[0].lower()] += 1

    def update_word_count(self, word, review):
        self.dictionaries[review[0].lower()][word] = self.dictionaries[review[0].lower()].get(word, 0) + 1

    """ Laplace smoothing included for unknown combinations. """
    def conditional_probabilities(self, type, word, div):
        if word not in self.dictionaries[type]:
            self.dictionaries[type][word] = 1 / div
        else:
            self.dictionaries[type][word] = (self.dictionaries[type][word] + 1) / div

        self.dictionaries[type][word] = math.log(self.dictionaries[type][word])

    def train(self):
        with open(self.file) as f:
            for line in f:
                line = util3.remove_stop_words(util3.remove_punctuation(line))
                identifier, true_or_fake, pos_or_neg, *review = line.strip().split()
                self.update_priors(true_or_fake)
                self.update_priors(pos_or_neg)

                for word in review:
                    self.update_word_count(word, true_or_fake)
                    self.update_word_count(word, pos_or_neg)
                    self.unique_words.add(word)


        self.prior_probabilities["f"] = math.log(self.variables["f"] / (self.variables["f"] + self.variables["t"]))
        self.prior_probabilities["t"] = math.log(self.variables["t"] / (self.variables["f"] + self.variables["t"]))
        self.prior_probabilities["n"] = math.log(self.variables["n"] / (self.variables["n"] + self.variables["p"]))
        self.prior_probabilities["p"] = math.log(self.variables["p"] / (self.variables["n"] + self.variables["p"]))

        divs = sum(self.dictionaries['p'].values()), sum(self.dictionaries['n'].values()),\
        sum(self.dictionaries['f'].values()), sum(self.dictionaries['t'].values())
        for word in self.unique_words:
            self.conditional_probabilities('t', word, divs[3] + len(self.unique_words))
            self.conditional_probabilities('f', word, divs[2] + len(self.unique_words))
            self.conditional_probabilities('p', word, divs[0] + len(self.unique_words))
            self.conditional_probabilities('n', word, divs[1] + len(self.unique_words))

        self.variables['t'] = divs[3]
        self.variables['f'] = divs[2]
        self.variables['p'] = divs[0]
        self.variables['n'] = divs[1]

    def save_model(self):
        with open(self.model_file, "w") as f:
            f.write(str(self.dictionaries))
            f.write("\n")
            f.write(str(self.prior_probabilities))
            f.write("\n")
            f.write(str(len(self.unique_words)))
            f.write("\n")
            f.write(str(self.variables))

if __name__ == "__main__":
    nb = NaiveBayesClassifier(sys.argv[1])
    nb.train()
    nb.save_model()
