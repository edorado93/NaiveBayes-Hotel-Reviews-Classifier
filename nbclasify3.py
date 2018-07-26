import sys
import math
import util3
class Classify:
    def __init__(self, test_file):
        self.test_file = test_file
        self.saved_model = "nbmodel.txt"
        self.output_file = "nboutput.txt"
        self.conditional_probabilities = {}
        self.prior_probabilities = {}
        self.unique_word_count = 0
        self.variables = {}

    def load(self):
        from ast import literal_eval
        saved = open(self.saved_model, "r")
        self.conditional_probabilities = literal_eval(saved.readline().strip())
        self.prior_probabilities = literal_eval(saved.readline().strip())
        self.unique_word_count = int(saved.readline().strip())
        self.variables = literal_eval(saved.readline().strip())
        saved.close()

    def get_conditional_probability(self, word, class_initial):
        if word in self.conditional_probabilities[class_initial]:
            return self.conditional_probabilities[class_initial][word]
        return math.log(1 / (self.unique_word_count + self.variables[class_initial]))

    def classify_review(self, review):
        true_prob, fake_prob, pos_prob, neg_prob = self.prior_probabilities['t'], self.prior_probabilities['f']\
            , self.prior_probabilities['p'], self.prior_probabilities['n']
        review = util3.remove_stop_words(util3.remove_punctuation(review))
        identifier, *review = review.split()

        for word in review:
            true_prob += self.get_conditional_probability(word, 't')
            fake_prob += self.get_conditional_probability(word, 'f')
            pos_prob += self.get_conditional_probability(word, 'p')
            neg_prob += self.get_conditional_probability(word, 'n')

        return identifier, "True" if true_prob > fake_prob else "Fake", \
                "Pos" if pos_prob > neg_prob else "Neg"

    def classify_test_file(self):
        output_file = open(self.output_file, "w")
        with open(self.test_file) as f:
            for review in f:
                identifier, class1, class2 = self.classify_review(review.strip())
                output_file.write(identifier + " " + class1 + " " + class2)
                output_file.write("\n")
        output_file.close()

if __name__ == "__main__":
    classifier = Classify(sys.argv[1])
    classifier.load()
    classifier.classify_test_file()
