# Movie Recommendation System

This project is a **Movie Recommendation System** that suggests movies based on user preferences and movie similarities. It utilizes **content-based filtering** using metadata from the TMDB 5000 movies dataset.

## Features

- **Top Movie List**: Displays the top 15 movies based on a weighted rating score.
- **Movie Recommendations**: Provides recommendations for movies similar to a selected film.
- **Popularity Visualization**: A bar chart visualization of the top 6 most popular movies.
- **Interactive Console**: Users can choose actions through a simple text-based interface.

## Prerequisites

Ensure you have the following libraries installed:

- `pandas`
- `sklearn`
- `matplotlib`

You can install them using:
```bash
pip install pandas scikit-learn matplotlib
```

## Dataset

The project uses the following datasets:
- `tmdb_5000_credits.csv`
- `tmdb_5000_movies.csv`

These files should be placed in the same directory as the script.

## Usage

Run the program using:
```bash
python main.py
```

### Options
1. **View Top Movies**: Displays the top 15 movies based on weighted ratings.
2. **Get Movie Recommendations**: Asks for a movie title and provides a list of similar movies.
3. **Exit**: Terminates the program.

### Example
**Recommendations for 'The Dark Knight Rises':**
```
1. The Dark Knight
2. Batman Begins
3. Inception
4. Man of Steel
5. The Prestige
```

## Code Structure
- **main.py**: The main script containing the core logic.
- **Functions**:
  - `load_and_merge_data()`: Loads and merges movie and credit datasets.
  - `calculate_weighted_rating()`: Computes the top movies based on a weighted score.
  - `plot_popular_movies()`: Visualizes the most popular movies.
  - `get_recommendations()`: Returns similar movies for a given title using cosine similarity.

## Future Improvements
- Incorporate additional recommendation techniques (collaborative filtering).
- Add a web interface for user interaction.
- Use additional metadata (genres, keywords) for enhanced recommendations.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Enjoy discovering movies with this recommendation system!
