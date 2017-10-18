# importing modules named "package" and "fresh_tomatoes"s
import package
import fresh_tomatoes
# creating instance for toy story
toy_story = package.Movie("Toy Story",
                          "A story of a boy and his toys ",
                          "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",    # NOQA
                          "https://www.youtube.com/watch?v=NTdKQzVFeis")                    # NOQA

# creating instance fo avatar movie
avatar = package.Movie("Avatar", "A maraine on an alien planet",
                       "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",    # NOQA
                       "https://www.youtube.com/watch?v=5PSNL1qE6VY")   # NOQA

# creating instance for bahubali movie
bahubali = package.Movie("Bahubali",
                         "Story of two brothers ",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BYmE4YjFmNWQtYTk5ZC00OGU3LWFlOTQtNThmYjBhZjhlNzU5XkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_SY1000_CR0,0,666,1000_AL_.jpg",   # NOQA
                         "https://www.youtube.com/watch?v=sOEg_YZQsTI")      # NOQA

# creating instance for three idiots movie
three_idiots = package.Movie("3 Idiots",
                             "Two friends looking for a lost buddY",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMyOTg0ODQ1OF5BMl5BanBnXkFtZTcwNjc0NTMwNQ@@._V1_SY1000_CR0,0,705,1000_AL_.jpg",   # NOQA
                             "https://www.youtube.com/watch?v=K0eDlFX9GMc")   # NOQA

# creating instance for DDLJ movie
dilwalle = package.Movie("Dilwalle Dulhaniye Le Jayenge",
                         "How Raj and Simran fall in love.",
                         "https://images-na.ssl-images-amazon.com/images/I/51gXOqCUijL.jpg",   # NOQA
                         "https://www.youtube.com/watch?v=c25GKl5VNeY")   # NOQA

# creating a list with all movies
movies = [toy_story, avatar, bahubali, three_idiots, dilwalle]

# opens the movie page in web browser
fresh_tomatoes.open_movies_page(movies)
