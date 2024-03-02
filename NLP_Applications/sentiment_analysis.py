'''This script is used to implement a sentiment and similarity analysis model
of Amazon Product Reviews using spaCy and TextBlob libraries.'''
# Import the libraries
import pandas as pd
from textblob import TextBlob
import spacy
nlp = spacy.load('en_core_web_sm')

# Import the dataset of the product reviews from the csv file and get a sample size
dataframe = pd.read_csv('amazon_product_reviews.csv', encoding='utf-8', dtype=str).sample(10)

# Drop the null values and duplicates in the reviews.text column if any
reviews_data = dataframe['reviews.text'].dropna().drop_duplicates()

# Initialise an empty list of processed product reviews
processed_reviews = []

# For each of the product reviews in the reviews.text column
for review in reviews_data:
    # Remove the leading and trailing white spaces and make the review lower case
    preprocessed_review = review.strip().lower()

    # Tokenise the review
    doc = nlp(preprocessed_review)

    # Lemmatise the review tokens and remove the white spaces, punctuations, stop words
    preprocessed_review = [token.lemma_ for token in doc \
        if not token.is_space | token.is_punct | token.is_stop]

    # Concatenate the processed tokens to form a new string if their list is not empty
    if preprocessed_review != []:
        # Append the new string to the list of processed product reviews
        processed_reviews.append(' '.join(preprocessed_review))

def predict_sentiment(product_review):
    '''This function predicts the sentiment of the input product review.'''

    # Create a TextBlob object of the text data
    blob = TextBlob(product_review)
    print(blob)
    print(blob.sentiment)

    # Get the polarity value of the text data
    polarity = blob.sentiment.polarity

    # Return the sentiment of the text data based on the range of polarity value
    if polarity > 0 and polarity <= 0.5:
        return 'Weak Positive'
    if polarity > 0.5 and polarity <= 1:
        return 'Strong Positive'
    if polarity < 0 and polarity >= -0.5:
        return 'Weak Negative'
    if polarity < -0.5 and polarity >= -1:
        return 'Strong Negative'
    return 'Neutral'

# Display the sentiment output title
print('Sentiment Analysis of Amazon Product Reviews')
print()

# Predict the sentiment for each of the product reviews
for index, review in enumerate(processed_reviews, start=1):
    print(f'#{index}', end=' ')
    print(predict_sentiment(review))
    print()

# Display the similarity output title
print('Similarity Comparison of Amazon Product Reviews')
print()

# Compare the similarity of the product reviews
for index, review in enumerate(processed_reviews, start=1):
    # Tokenise the first review
    review = nlp(review)

    for index_, review_ in enumerate(processed_reviews, start=1):
        # Tokenise the second review
        review_ = nlp(review_)

        # Display the two product reviews
        print(f'#{index} {review}')
        print(f'#{index_} {review_}')

        # Compare the similarity of the two product reviews
        similarity = review.similarity(review_)
        if similarity > 0.5 and similarity <= 1:
            print('Highly Similar', end=' ')
        elif similarity < 0.5 and similarity >= 0:
            print('Weakly Similar', end=' ')

        # Display the similarity value of the two product reviews
        print(similarity)
        print()
