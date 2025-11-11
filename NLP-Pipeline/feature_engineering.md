The Feature Engineering step is the third step in the NLP pipeline,
following Data Acquisition and Text Preparation.
After preparing the text data, the goal of feature engineering is
to transform this text into a format that can be effectively used by
machine learning and deep learning algorithms.

Feature Engineering

feature engineering essentially involves converting text into numbers.
This conversion is necessary because most machine learning and deep
learning models primarily work with numerical data.
In some contexts,
this process is also referred to as text vectorization because you
are converting text into vectors of numbers

key aspects of feature engineering as explained in the source:

Purpose: The fundamental purpose is to get the data into the correct format (numerical)
for machine learning and deep learning algorithms.

Process: This step involves extracting input columns (features) from the text data.

Example: The sentiment analysis for movie reviews.
If you have reviews with corresponding sentiment labels (positive or negative),
you can perform basic feature engineering by creating new columns such as:

Number of positive words in the review

Number of negative words in the review◦
Number of neutral words in the review The original
text review is then replaced by these numerical features, along with the sentiment label

---

Advanced Techniques: The advanced feature engineering techniques that will be discussed:

- Bag of Words
- TF-IDF (Term Frequency-Inverse Document Frequency)
- Word2Vec

Dependence on the Problem: The specific feature engineering techniques you apply
heavily depend on the nature of the NLP problem you are trying to solve.
For instance, the feature engineering for sentiment analysis might differ from that used in text summarization.
You need to be open to different possibilities and not assume that
one technique (like Bag of Words)
will work for every problem

---

Feature engineering in ML VS DL

Machine Learning vs. Deep Learning:
There's a key difference in how feature engineering is approached in traditional
machine learning pipelines compared to deep learning pipelines:

1. Machine Learning: In machine learning, you typically need to manually engineer
   features based on your domain knowledge and understanding of the problem.
   You preprocess the data and then explicitly create features before feeding them
   into the machine learning algorithm. While this allows for interpretability of the model's results
   because you understand the features driving the prediction, it requires more effort and domain expertise.
   There's also a risk that the engineered features might not all be helpful and could even negatively impact the model.

2. Deep Learning: In deep learning, after preprocessing the data,
   you often feed the raw text (or sequences of tokens) directly
   into the deep learning model. The deep learning model itself
   automatically learns the relevant features during the training process,
   a concept often referred to as embeddings. This reduces the need for manual
   feature engineering but can make the model less interpretable,
   as it's harder to understand which specific features the model has
   learned and is using for its predictions.

3. Integration of Heuristic Approaches: heuristic (rule-based or "jugaad") approaches used
   when data is limited can be integrated into the feature engineering step of a machine learning pipeline.
   For example, a rule to identify spam emails based on a specific sender ID can be used as an additional binary feature in your machine learning model

---
