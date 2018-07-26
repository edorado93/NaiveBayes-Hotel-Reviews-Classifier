# NaiveBayes-Hotel-Reviews-Classifier

In this assignment we will write a naive Bayes classifier to identify hotel reviews as either true or fake, and either positive or negative. You will be using the word tokens as features for classification. 

## Data
A set of training and development data will is available with the following files:

* One file train-labeled.txt containing labeled training data with a single training instance (hotel review) per line (total 960 lines). The first 3 tokens in each line are:
a unique 7-character alphanumeric identifier
  * a label True or Fake
  * a label Pos or Neg
These are followed by the text of the review.
* One file dev-text.txt with unlabeled development data, containing just the unique identifier followed by the text of the review (total 320 lines).
* One file dev-key.txt with the corresponding labels for the development data, to serve as an answer key.

## Programs
There are two programs implemented: `nblearn.py` will learn a naive Bayes model from the training data, and `nbclassify.py` will use the model to classify new data. The learning program will be invoked in the following way:

```
> python nblearn.py /path/to/input
```

The argument is a single file containing the training data; the program will learn a naive Bayes model, and write the model parameters to a file called `nbmodel.txt`. 
The classification program will be invoked in the following way:

```
> python nbclassify.py /path/to/input
```

The argument is a single file containing the test data file; the program will read the parameters of a naive Bayes model from the file `nbmodel.txt`, 
classify each entry in the test data, and write the results to a text file called `nboutput.txt`.

##Notes

* **Problem formulation**. You may treat the problem as two binary classification problems (true/fake and positive/negative), or as a 4-class single classification problem. Choose whichever works better.
* **Smoothing and unknown tokens**. You should implement some method of smoothing for the training data and a way to handle unknown vocabulary in the test data, otherwise your programs won’t work. The reference solution will use add-one smoothing on the training data, and will simply ignore unknown tokens in the test data. You may use more sophisticated methods which you implement yourselves.
* **Tokenization**. You’d need to develop some reasonable method of identifying tokens in the text (since these are the features for the naive Bayes classifier). Some common options are removing certain punctuation, or lowercasing all the letters. You may also find it useful to ignore certain high-frequency or low-frequency tokens. You may use any tokenization method which you implement yourselves. Experiment, and choose whichever works best.

