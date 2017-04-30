import fresh_tomatoes
import media


def show_movies():
    """Show the movies website"""
    
    # Build movies array
    movies = []
    
    movies.append(media.Movie(
        "Fight Club", 
        "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
        "https://www.youtube.com/watch?v=BdJKm16Co6M&t=2s"))
    
    movies.append(media.Movie(
        "Donnie Darko",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BZWQyN2ZkODktMTBkNS00OTBjLWJhOGYtNGU4YWVkNTY0ZDZkXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,683,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=rPeGaos7DB4"))
    
    movies.append(media.Movie(
        "Adapation",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxNjMwNDQwNF5BMl5BanBnXkFtZTYwNDIzNTc2._V1_.jpg",
        "https://www.youtube.com/watch?v=0HtZ2M4e_AM"))
    
    # Open website in web browser
    fresh_tomatoes.open_movies_page(movies)


# Use show_movies as the main function
if __name__ == "__main__":
    show_movies()
