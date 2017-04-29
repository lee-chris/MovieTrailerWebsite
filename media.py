class Movie(object):
    
    """Simple container of movie information.
    
    Attributes:
        title: title of the movie
        poster_image_url: absolute http url to an image of the movie's poster
        trailer_youtube_url: absolute http url to a trailer for the movie
    """
    
    
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        
        """Construct movie structure.
        
        Args:
            title: title of the movie
            poster_image_url: absolute http url to an image of the movie's poster
            trailer_youtube_url: absolute http url to a trailer for the movie
        """
        
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
