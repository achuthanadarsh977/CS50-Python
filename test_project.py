from project import load_movies_data,top_grossing_movies, filter_by_genre , movie_by_studio
import unittest


class TestMovieAnalysis(unittest.TestCase):

   def setUp(self):
       self.movies = load_movies_data('blockbuster.csv')


   def test_load_movies(self):
       self.assertGreater(len(self.movies),"Movie data should not be empty after loading CSV file")


   def test_top_highest_grossing_movies(self):
      top_movies = top_grossing_movies(self.movies,3)
      self.assertEqual(len(top_movies),3,"Should exactly return 3 top movies")


   def test_filter_by_genre(self):
       action_movies = filter_by_genre(self.movies,'Action')
       self.assertGreater(len(action_movies),0,"There should be action movies in the dataset")
       self.assertIn("Avengers Endgame",[movie['title'] for movie in action_movies],"Avengers Endgame should be in action genre")




if __name__ == "__main__":
    unittest.main()
