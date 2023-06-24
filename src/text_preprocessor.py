import pandas as pd
import re
import spacy
from nltk.corpus import stopwords

def preprocess_text_data(df: pd.DataFrame, text_column: str) -> pd.DataFrame:
    """
    Preprocesses textual data in a DataFrame by removing links, non-alphabetic characters,
    performing lemmatization, removing stopwords, and generating word tokenization.
    
    Args:
        df (pd.DataFrame): DataFrame containing the text data.
        text_column (str): Name of the column in the DataFrame containing the text data.
        
    Returns:
        pd.DataFrame: DataFrame with the preprocessed text and word tokenization columns.
    """
    # Creating a copy of the comments column 
    df['comment_preprocessed'] = df[text_column]
    
    # Remove links
    df['comment_preprocessed'] = df['comment_preprocessed'].apply(lambda text: re.sub(r'http\S+|https\S+|www.\S+', '', text))
    
    # Removing all non-alpha characters
    df['comment_preprocessed'] = df['comment_preprocessed'].apply(lambda text: re.sub("[^A-Z]", " ", text, 0, re.IGNORECASE))
    
    # Initialize spaCy's English language model
    nlp = spacy.load('en_core_web_sm')
    
    # Lemmatization
    df['comment_preprocessed'] = df['comment_preprocessed'].apply(lambda text: ' '.join([token.lemma_ for token in nlp(text)]))

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    df['comment_preprocessed'] = df['comment_preprocessed'].apply(lambda text: ' '.join([word for word in text.split() if word not in stop_words]))

    # Word tokenizer column
    df['comment_tokens'] = df['comment_preprocessed'].apply(lambda text: [token.text for token in nlp(text)])

    return df
