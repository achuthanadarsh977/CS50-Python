
import csv

def main():
    print("Welcome to the highest grossing movies application")
    print("1.View Top N Highest Grossing Movies")
    print("2.Filter Movie By Main_Genre")
    print("3.Find Movie By Studio")
    print("0.Exit")

    while True:
        option = input("Choose an option:")
        if option == "1":
            n = int(input("How many top movies do you want to see?"))
            top_movies = top_grossing_movies(movies,n)
            for movie in top_movies:
                print(f"{movie['title']} - {movie['worldwide_gross']}")

        elif option == "2":
            genre = input("Enter a genre:")
            genre_movies = filter_by_genre(movies,genre)
            for movie in genre_movies:
                print(f"{movie['title']} - {movie['worldwide_gross']}")

        elif option == "3":
            studio = input("Enter studio name:")
            studio_movies = movie_by_studio(movies,studio)
            for movie in studio_movies:
                print(f"{movie['title']} - {movie['worldwide_gross']}")
        elif option == "0":
            break
        else:
            print("Invalid option.Try again!")







def load_movies_data(filename):

    movies = []
    with open('blockbuster.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append(row)
    return movies


movies = load_movies_data('blockbuster.csv')
print(f"Loaded {len(movies)} movies.")

def top_grossing_movies(movies,n):
    sorted_movies = sorted(movies,key=lambda x:float(x['worldwide_gross'].replace('$','').replace(',','')),reverse=True)
    return sorted_movies[:n]



def filter_by_genre(movies,genre):
    return [movie for movie in movies if genre.lower() in movie['Main_Genre'].lower()]


def movie_by_studio(movies,studio):
    return [movie for movie in movies if studio.lower() in movie['studio'].lower()]




if __name__ == "__main__":
    main()
