current_movies = {
    'The Shawshank Redemption': '11:00am',
    'The Dark Knight': '01:00pm',
    "Schindler's List": '03:00pm',
    '12 Angry Men': '05:00pm',
    'Pulp Fiction': '07:00pm',
    'Fight Club': '09:00pm',
    'Forrest Gump': '11:00pm',
    'Inception': '01:00am',
    'Interstellar': '03:00am'
    }

print("We're showing the following movies:")
for key in current_movies:
    print(key)

del current_movies['Interstellar'] #Intentionally removed.

movie = input('What movie would you like the showtime for\n')

#current_movies[movie] throw excpetion when item does not exist but get(movie) return noun.
showtime = current_movies.get(movie)

if showtime:
    print(movie, 'is playing at', showtime)
else:
    print("Requested movie isn't playing")