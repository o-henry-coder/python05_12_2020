import sqlite3 as sq

ACTORS = [('1', 'John Malkovich', '1956', '3'), ('2', 'Johny Depp', '1963', '1'),
          ('3', 'Christina Richi', '1980', '1'), ('4', 'Vivien Lie', '1913', '2'),
          ('5', 'Clark Gable', '1901', '2'), ('6', 'Hattie McDaniel', '1903', '2'),
          ('7', 'Orson Welles', '1890', '13'), ('8', 'Quentine Tarantino', '1988', '8'),
          ('9', 'Kolin Firth', '1977', '15'), ('10', 'Daniel Redcliff', '1990', '4'),
          ('11', 'Al Paccino', '1956', '6'), ('12', 'Emma Watson', '1991', '4'),
          ('13', 'Archil Gomiashvilio', '1965', '14'), ('14', 'Helena Bonham Carter', '1979', '15'),
          ('15', 'Jennifer Ehle', '1980', '15'), ('16', 'Lee Sun-kyun', '1988', '10'),
          ('17', 'Tim Robbins', '1938', '7'), ('18', 'Marlon Brando', '1948', '6'),
          ('19', 'Sergey Filippov', '1958', '14'), ('20', 'Lew Ayres', '1974', '5'),
          ('21', 'Cho Yeo-jeong', '1988', '10'), ('22', 'John Travolta', '1963', '8'),
          ('23', 'Michael Fisher', '1969', '11'), ('24', 'Morgan Freeman', '1974', '7'),
          ('25', 'Louis Wolheim', '1968', '5'), ('26', 'Uma Thurman', '1981', '8'),
          ('27', 'Noriko Hidaka', '1985', '9'), ('28', 'Rumi Hiiragi', '1978', '12'),
          ('29', 'Joseph Cotten', '1979', '13'), ('30', 'Alan Rickman', '1968', '4'),
          ('31', 'Ray Collins', '1984', '13'), ('32', 'Mari Natsuki', '1980', '12')]

FILMS = [('1', 'Sleepy Hollow', '1', '1999', 'USA'),
         ('2', 'Gone with the Wind', '2', '1939', 'USA'),
         ('3', 'The ABC Murders', '14', '2018', 'Great Britain'),
         ('4', 'Harry Potter and the Sorcerer Stone', '5', '2001', 'USA'),
         ('5', 'All Quiet on the Western Front', '12', '1930', 'Germany'),
         ('6', 'The Godfather', '6', '1972', 'USA'),
         ('7', 'The Shawshank Redemption', '11', '1994', 'USA'),
         ('8', 'Pulp Fiction', '4', '1994', 'USA'),
         ('9', 'My Neigbor Totoro', '8', '1988', 'Japan'),
         ('10', 'Parasite', '15', '2018', 'Southern Korea'),
         ('11', 'Howl Moving Castle', '9', '2012', 'Japan'),
         ('12', 'Spirited Away', '10', '2001', 'Japan'),
         ('13', 'Citizen Kane', '3', '1941', 'USA'),
         ('14', 'The Twelve Chairs', '7', '1971', 'Russia'),
         ('15', 'The King Speech', '13', '2011', 'Great Britain')]

DIRECTORS = [('1', 'Tim Burton', '1958', '1'), ('2', ' Victor Fleming', '1889', '2'),
             ('3', 'Orson Welles', '1890', '13'), ('4', 'Quentine Tarantino', '1988', '8'),
             ('5', 'Chris Columbus', '1935', '4'), ('6', 'Francis Ford Coppola', '1947', '6'),
             ('7', 'Leonid Gaidai', '1932', '14'), ('8', 'Hayao Miyazaki ', '1889', '9'),
             ('9', 'Isao Takahata', '1979', '11'), ('10', 'Keiko Niwa', '1981', '12'),
             ('11', 'Tom Hooper', '1958', '15'), ('12', 'Frank Darabont', '1868', '7'),
             ('13', 'Lewis Milestone', '1889', '5'),('14', 'Alex Gabassi', '1959', '3'),
             ('15', 'Bong Joon-ho', '1948', '10')]

with sq.connect("movie_database.sqlite") as con :
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS films (
            film_id INTEGER PRIMARY KEY,
            title TEXT, 
            director_id INTEGER,
            date INTEGER,
            country TEXT,
            FOREIGN KEY (director_id) REFERENCES directors (id)
            );""")
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS actors (
            actor_id INTEGER PRIMARY KEY,
            name TEXT,
            birthdate INTEGER,
            film_id INTEGER,
            FOREIGN KEY (film_id) REFERENCES films (film_id)
            );""")
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS directors (
            director_id INTEGER PRIMARY KEY,
            name TEXT,
            birthdate INTEGER,
            film_id INTEGER,
            FOREIGN KEY (film_id) REFERENCES films (film_id)
            );""")
    con.commit()

    cur.executemany("""INSERT OR REPLACE INTO actors VALUES(?,?,?,?);""", ACTORS)
    cur.executemany("""INSERT OR REPLACE INTO directors VALUES(?,?,?,?);""", DIRECTORS)
    cur.executemany("""INSERT OR REPLACE INTO films VALUES(?,?,?,?,?);""", FILMS)
    con.commit()



#director_id INTEGER NOT NULL,
            # FOREIGN KEY (director_id) REFERENCES directors (id),

#            FOREIGN KEY (actor_id) REFERENCES actors (id),