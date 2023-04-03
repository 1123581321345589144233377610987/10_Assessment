class Movie():
    def __init__(self):
        self.title = ""
        self.release_year = ""
        self.story_year = ""
    def set_title(self, title):
        self.title = title
    def set_release_year(self, release_year):
        self.release_year = release_year
    def set_story_year(self, story_year):
        self.story_year = story_year
    def get_title(self):
        return self.title
    def get_release_year(self):
        return self.release_year
    def get_story_year(self):
        return self.story_year

FILE = open('MarvelMovies.csv', 'r')
file = FILE.readlines()
file.sort()
FILE.close()
movies = []
count = 0
for i in file:
    movies.append(Movie())
    i = i.strip("\n")
    i = i.split(",")
    movies[count].set_title(i[0])
    movies[count].set_release_year(i[1])
    movies[count].set_story_year(i[2])
    count += 1
title = "Title"
release = "Release"
story = "Storyline"
print(f"{title:^40}{release:11}{story:11}")
count = 0
for i in movies:
    print(f"{movies[count].get_title():40}{movies[count].get_release_year():11}{movies[count].get_story_year():11}")
    count += 1
