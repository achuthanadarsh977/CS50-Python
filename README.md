#  Highest Grossing Films
    #### Video Demo: https://youtu.be/UkwUG1Kg8jE
    #### Description:

This project is a command-line application designed to interact with a dataset of blockbuster movies
stored in a CSV file (blockbuster.csv).Its primary purpose is to provide users with easy access to information
about the highest_grossing movies ,as well as options to filter movies by genre or studio.Below is an overview
of the key components and functionalities of the application.

Key Features:

  User Interface:The application greets users with a welcome message and presents a menu of four options which are
  view the top n highest-grossing movies, filter movies by their main genre , find movies produced by the specific
  studio and exit the application

  Data Loading: The movie data is loaded from the CSV file using the load_movies_data function which employs csv.DictReader
  to read each row into a dictionary format.This makes accessing movie attributes easier.

  Top grossing movies:When a user selects the option to view the top movies,the top_grossing_movies function is called.
   This function sorts the list of movies based on their worldwide gross earnings,which are parsed from the string format
   (eg:'$1,000,000').The users can specify how many movies they want to see.

  Filtering By Genre:The application allows users to filter movies based on their main genre.The filter_by_genre function
  iterates through the movie list and returns those that match the user_specified genre, making it case_sensitive for
  better usability.

  Finding movies by studio: Similar to genre filtering, users can search for movies produced by a particular studio
  through the movie_by_studio function.This funciton filters the movies based on the studio provided by the user.

  Input Validation:The application includes basic input validation to ensure that the user select valid options.If an
  invalid choice is made, the application prompts the user to try again.

  This project uses Python built_in csv file module for reading and parsing movie data.This ensures that the application
  can handle various formats and special characters present in movie titles and genres.
  The use of list comprehensions and sorting with lambda functions provides an efficient way to manage and retrieve data
  from the movie list.The command-line interface is designed to be straightforward,guiding users through their options and
  providing clear instructions for input.

  While the application serves its purpose, there are several areas for potential improvement:

  Implementing more robust error handling would improve user experience particularly for inputs that may not
  convert cleanly.

  Checking for the presence of specified genres or studios in the dataset could prevent confusion and enhance
  the applications reliability.

  Transitioning from a command-line interface to a graphical user interface could make the application more accessible
  to a broader audience.


In summary, this project exemplifies a simple yet effective way to interact with dataset of movies ,offering
valuable insights into popular films through a user-friendly command-line appilcation.
