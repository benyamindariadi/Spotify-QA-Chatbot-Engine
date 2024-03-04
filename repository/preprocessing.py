import os
import pandas as pd

class DataPreprocessing:
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
        self.dataframe_to_text(df, 'review_text', os.path.join('data/clean_data', 'spotify_reviews.txt'))

