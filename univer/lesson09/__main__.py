import sqlite3

class Artist:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"({self.id}, {self.name})"

    def __repr__(self):
        return  self.__str__()

if __name__ == '__main__':
    pass
    conn = sqlite3.connect('Chinook_Sqlite.sqlite')
    print('conn ok')
    cursor = conn.cursor() #точка, через которую потом работать
    cursor.execute('SELECT * FROM Artist')
    results = cursor.fetchall()
    artists = []
    for entry in results:
        artists.append(Artist(id = entry[0], name = entry[1]))
    print(artists)
    conn.close()