import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import matplotlib.pyplot as plt


def load_and_merge_data():
    df1 = pd.read_csv('tmdb_5000_credits.csv')
    df2 = pd.read_csv('tmdb_5000_movies.csv')

    df1.columns = ['id', 'tittle', 'cast', 'crew']
    df2 = df2.merge(df1, on='id')
    return df2


def calculate_weighted_rating(df):
    C = df['vote_average'].mean()
    m = df['vote_count'].quantile(0.9)

    q_movies = df.copy().loc[df['vote_count'] >= m]

    def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        return (v / (v + m) * R) + (m / (m + v) * C)

    q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
    q_movies = q_movies.sort_values('score', ascending=False)
    return q_movies[['title', 'vote_count', 'vote_average', 'score']].head(15)


def plot_popular_movies(df):
    pop = df.sort_values('popularity', ascending=False)
    plt.figure(figsize=(12, 4))
    plt.barh(pop['title'].head(6), pop['popularity'].head(6), align='center', color='skyblue')
    plt.gca().invert_yaxis()
    plt.xlabel("Popularity")
    plt.title("Popular Movies")
    plt.show()


def build_tfidf_matrix(df):
    tfidf = TfidfVectorizer(stop_words='english')
    df['overview'] = df['overview'].fillna('')
    tfidf_matrix = tfidf.fit_transform(df['overview'])
    return tfidf_matrix


def compute_cosine_similarity(tfidf_matrix):
    return linear_kernel(tfidf_matrix, tfidf_matrix)


def create_indices(df):
    return pd.Series(df.index, index=df['title']).drop_duplicates()


def get_recommendations(title, cosine_sim, df, indices):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]


def main():
    df2 = load_and_merge_data()
    tfidf_matrix = build_tfidf_matrix(df2)
    cosine_sim = compute_cosine_similarity(tfidf_matrix)
    indices = create_indices(df2)

    while True:
        choice = input(
            "\nChoose an option:\n1. View top movies by score\n2. Get movie recommendations\n3. Exit\nEnter your choice (1/2/3): ")

        if choice == '1':
            print("\nTop 15 movies based on score:")
            top_movies = calculate_weighted_rating(df2)
            print(top_movies)
        elif choice == '2':
            title = input("Enter a movie title for recommendations: ")
            if title in indices:
                recommendations = get_recommendations(title, cosine_sim, df2, indices)
                print(f"\nMovies similar to '{title}':")
                print(recommendations)
            else:
                print("\nMovie not found. Please try again.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
