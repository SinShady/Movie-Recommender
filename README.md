# Movie-Recommender

## Understanding the Problem
Flatflix is an hypothetical Netflix competitor that is all about connecting people to the movies they love. To help customers find those movies, they want to develop a world-class movie recommendation system to encourage users to stay on the platform. The movie recommender well recommend movie to users using a collaborative apporach. Users will be shown movies that similar users have liked in the past, we will also address the "Cold Start" problem of users with no history on the platform.

## Understanding The Data
We will be using the MovieLens dataset from the GroupLens research lab at the University of Minnesota. Becuase we are not planning on running our analysis on a powerful enough cloud platform, we will use the "small" dataset containing 100,000 user ratings.

The MovieLens dataset is a "classic" recommendation system dataset, that is used in numerous academic papers and machine learning proofs-of-concept. You will need to create the specific details about how the user will provide their ratings of other movies, in addition to formulating a more specific business problem within the general context of "recommending movies".

### The Data
The dataset was a clean dataset containing four CSV files:
1. `links.csv` (9742, 3)
Is a csv file containing 3 columns, `movieId`, `imdbId`, `tmdbId` with 9742 rows. Each row represents a unique movie.
2. `movies.csv` (9742, 3)
Is a csv file containing 3 columns, `movieId`, `title`, and `genre` with 9742 rows. Each row represents a unique movie
3. `ratings.csv` (100836, 4)
Is a csv file containg 4 `columns`, `userId`,	`movieId`, `rating`, `timestamp` with 100836 rows. Each row represents a `rating` from a `userID` assigned to a `movieID`
4. `tags.csv` (3683, 4)
Is a csv file containing 4 columns, `userId`,	`movieId`,	`tag`,	`timestamp` with 2683 rows. Each row represents a `timestamp` a `userID` gave assigned a `movieID` a `tag`.

## Preparing the Data
The steps we took to build the model/cold start
1. train test split
2. we ran a param grid, ended with best model .86
3. als model

## The Model
Jeff has got something
what does als do, it uses matrix multiplication with user ratings, since thers a lot of ratings that are blanks (not every user has rated every movies) als predicts ratings for those blank spaces, and then recommends the blank spaced movies. What it has predicted to be highly rated, it returns the top 5.

### Model Evaluation
why rsme and what our rsme means?

## Business Deployment
We optimized our model to recommend five movies for our users, based on their past rating history.
The infographic bellow shows some examples of movies our recommender suggests given a `liked` rating for the movie.

Since resources for emergency well repair may be limited, the following list shows where our model is most certain about about the wells it flags as non functional. In these regions, teams deployed to fix wells will make the fewest wasted trips.

## Summary
In summary we were able to build a model that produces 

We addressed the problem of broken wells and communities without access to clean water in Tanzania by creating a predictive model to identify wells that will cease to provide this important resource. We studied the problem and the data available, iterated through several model prototypes, and developed a model successfully predicts almost 80% of failing wells. Since our model was not uniformly accurate in all regions of the country, we identified those regions where our model could most efficiently be used to provide emergency maintenance to wells serving local populations.

We hope our predictive model will assist governmental and aid organizations in targeting failed wells for maintenance. Clean and functional wells save lives.
