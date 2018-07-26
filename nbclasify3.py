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

    # Load the model's learned parameters
    def load(self):
        # literal_eval is used to convert string representation of Python's dictionary to the actual object
        # This is one use case of it.
        from ast import literal_eval
        saved = open(self.saved_model, "r")
        # Load all the saved values
        self.conditional_probabilities = literal_eval(saved.readline().strip())
        self.prior_probabilities = literal_eval(saved.readline().strip())
        self.unique_word_count = int(saved.readline().strip())
        self.variables = literal_eval(saved.readline().strip())
        saved.close()

    def get_conditional_probability(self, word, class_initial):
        if word in self.conditional_probabilities[class_initial]:
            return self.conditional_probabilities[class_initial][word]
        return math.log(1 / (self.unique_word_count + self.variables[class_initial]))

    # Classify individual review
    def classify_review(self, review):
        true_prob, fake_prob, pos_prob, neg_prob = self.prior_probabilities['t'], self.prior_probabilities['f']\
            , self.prior_probabilities['p'], self.prior_probabilities['n']

        # Remove punctuation and stop words from the review
        review = util3.remove_stop_words(util3.remove_punctuation(review))
        identifier, *review = review.split()

        # Note, here we add the conditional probabilities of every word belonging to each of the classes.
        # We are able to add here because we took log of the probabilities earlier during training.
        # If we had taken probabilities by themselves, we would have had to multiply them.
        # P(True | Review) = P(True) * P(Review | True)
        # P(Review | True) = P(W1 | True) * P(W2 | True) * P(W3 | True) * .... P(Wn | True)
        # So, for log probabilities, we can add instead of multiplication
        for word in review:
            true_prob += self.get_conditional_probability(word, 't')
            fake_prob += self.get_conditional_probability(word, 'f')
            pos_prob += self.get_conditional_probability(word, 'p')
            neg_prob += self.get_conditional_probability(word, 'n')

        
        return identifier, "True" if true_prob > fake_prob else "Fake", \
                "Pos" if pos_prob > neg_prob else "Neg"

    # Classify all the reviews in a given test file.
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
