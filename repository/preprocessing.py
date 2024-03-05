import os
import pandas as pd
import re


class DataPreprocessing:
    @staticmethod
    def remove_emoticons_and_foreign_chars(text):
        emoticon_pattern = re.compile(u'['
                                      u'\U0001F600-\U0001F64F'
                                      u'\U0001F300-\U0001F5FF'
                                      u'\U0001F680-\U0001F6FF'
                                      u'\U0001F1E0-\U0001F1FF'
                                      ']+',
                                      flags=re.UNICODE)
        foreign_char_pattern = re.compile(r'[^\x00-\x7F]+')
        text = emoticon_pattern.sub('', text)
        clean_text = foreign_char_pattern.sub('', text)
        return clean_text

    @staticmethod
    def dataframe_to_text(df, column_name, output_file):
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write('This is a Google Store reviews for Spotify application:' + '\n')
                for index, row in df.iterrows():
                    review_text = row[column_name]
                    file.write(review_text + '\n')
            print(f"Data successfully saved to {output_file}")
        except Exception as e:
            print(f"Error occurred: {str(e)}")

    def clean_review_text(self, csv_file_dir):
        df = pd.read_csv(csv_file_dir, usecols=['review_text', 'review_rating', 'review_likes', 'review_timestamp'])
        df = df[df.review_likes >= 5]
        df = df.sort_values(by=['review_rating', 'review_likes', 'review_timestamp'], ascending=[False, False, False])
        df['review_text'] = df['review_text'].apply(self.remove_emoticons_and_foreign_chars)
        df['review_text'] = df['review_text'].replace(r'\s+', ' ', regex=True)
        df['review_text'] = df['review_text'].str.strip()
        self.dataframe_to_text(df, 'review_text', os.path.join('data/clean_data', 'spotify_reviews.txt'))
