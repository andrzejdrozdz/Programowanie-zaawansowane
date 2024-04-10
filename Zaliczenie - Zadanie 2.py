class Movie:

    def __init__(self, title, year, rating) :
        self.title = title if isinstance(title, str) else ""
        self.year = year if isinstance(year, int) else 0
        self.rating = rating if isinstance(rating, float) else 0.0
    

    def __repr__(self):
        return f"{self.title} {self.year} {self.rating}"
        

    def __lt__(self, other):
        # 1. sortowanie po tytule rosnąco
        # return (self.title) < (other.title)
        # 2. sortowanie po tytule malejąco
        # return (other.title) < (self.title)
        # 3. sortowanie po tytule i roku rosnąco
        # return (self.title, self.year) < (other.title, other.year)
        # 4. sortowanie po roku  i ocenie filmu malejąco
        # return (other.year, other.rating) < (self.year, self.rating)
        # 5. sortowanie po tytule, roku  i ocenie rosnąco
        return (self.title, self.year, self.rating) < (other.title, other.year, other.rating)
    
    


movies = [
    Movie("Skazani na Shawshank", 1994, 9.3),
    Movie("Ojciec chrzestny", 1972, 9.2),
    Movie("Mroczny Rycerz", 2008, 9.0),
    Movie("Ojciec chrzestny II", 1974, 9.0),
    Movie("Dwunastu gniewnych ludzi", 1957, 9.0),
    Movie("Lista Schindlera", 1993, 9.0),
    Movie("Władca Pierścieni: Powrót króla", 2003, 9.0),
    Movie("Pulp Fiction", 1994, 8.9),
    Movie("Władca Pierścieni: Drużyna Pierścienia", 2001, 8.9),
    Movie("Dobry, zły i brzydki", 1966, 8.3)
]

print(movies)

movies.sort()

print(movies)
