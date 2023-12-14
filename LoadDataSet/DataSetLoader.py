import pandas as pd

def return_dataframe_object():
    
    path = 'DataSet/IMDB-Dataset-65k-movie-review.csv'
    
    df = pd.read_csv(path)
    df['Label'] = df['Ratings'].apply(lambda x: '1' if x >= 7 else ('0' if x<=4 else '2'))
    df=df[df.Label<'2']
    return df
    