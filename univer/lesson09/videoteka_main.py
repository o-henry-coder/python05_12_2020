import sqlite3
from sqlite3 import Error
import csv
import json


class Database:
    def __init__(self, database):
        self.database = database

    def create_connection():
        connection = None
        try :
            connection = sqlite3.connect('movie_database.sqlite')
            print("Connection to Movie Database successful")
        except Error as e :
            print(f"The error '{e}' occurred")

        return connection

    def csv_save():
        with sqlite3.connect('movie_database.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute("select * from films")
            with open("films_data.csv", "w") as csv_file :
                csv_writer = csv.writer(csv_file, delimiter="\t")
                csv_writer.writerow([i[0] for i in cursor.description])
                csv_writer.writerows(cursor)
            cursor.execute("select * from actors")
            with open("films_data.csv", "a") as csv_file :
                csv_writer = csv.writer(csv_file, delimiter="\t")
                csv_writer.writerow([i[0] for i in cursor.description])
                csv_writer.writerows(cursor)
            cursor.execute("select * from directors")
            with open("films_data.csv", "a") as csv_file :
                csv_writer = csv.writer(csv_file, delimiter="\t")
                csv_writer.writerow([i[0] for i in cursor.description])
                csv_writer.writerows(cursor)
        print("Data exported successfully")

    def json_save():
        csvfile = open('films_data.csv', 'r')
        jsonfile = open('films_data.json', 'w')

        fieldnames = ("film_id", "title", "director_id", "name", "country")
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader :
            json.dump(row, jsonfile)
            jsonfile.write('\n')



class Films:
    def __init__(self, title, date, country):
        self.country = country
        self.title = title
        self.date = date


    def __str__(self):
        return f"({self.title}, {self.date}, {self.country})"

    def __repr__(self):
        return  self.__str__()

class Actors:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def __str__(self):
        return f"({self.name}, {self.birthdate})"

    def __repr__(self):
        return  self.__str__()

class Requests:
    def show_actors(f_title:Actors):
        with sqlite3.connect('movie_database.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT actors.name, actors.birthdate from actors"
                           f" JOIN films ON actors.film_id = films.film_id "
                           f"WHERE films.title LIKE '%{f_title}%'")
            results = cursor.fetchall()
            if results is None:
                print('there is no such film')
            else:
                actors = []
                for entry in results :
                    actors.append(Actors(name=entry[0], birthdate=entry[1]))
                    print(entry, '\n')
                conn.commit()

    def show_all_films():
        with sqlite3.connect('movie_database.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT films.title, films.date, films.country from films')
            results = cursor.fetchall()
            films = []
            for entry in results :
                films.append(Films(title = entry[0], date = entry[1], country= entry[2]))
                print(entry, '\n')
            conn.commit()
        return films

    def show_films_with_date(date:Films):
        with sqlite3.connect('movie_database.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT films.title, films.date, films.country from films  WHERE films.date >'{date}'"
                            "ORDER by films.date DESC")
            results = cursor.fetchall()
            films = []
            for entry in results :
                films.append(Films(title = entry[0], date = entry[1], country= entry[2]))
                print(entry, '\n')
            conn.commit()

    def show_actors_directors():
        with sqlite3.connect('movie_database.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT actors.name, actors.birthdate from actors "
                           f"JOIN directors ON actors.name = directors.name")
            results = cursor.fetchall()
            actors_directors = []
            for entry in results :
                actors_directors.append(Actors(name=entry[0], birthdate=entry[1]))
                print(entry, '\n')
            conn.commit()

    def __repr__(self):
        return  self.__str__()


class ChangeInfo:
    def insert_actors(new_actor = []):
        a_id = int(input('enter new actor id '))
        name = input('enter new actor name ')
        birth = input('enter actor birthdate ')
        f_id = None
        new_actor = [a_id, name, birth, f_id]
        with sqlite3.connect('movie_database.sqlite') as conn :
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO actors VALUES (?,?,?,?)",new_actor)

            conn.commit()

    def update_actors():
        name = input('enter actor name to be changed ')
        new_name = input('enter new actor name ')
        a_id = int(input('enter new actor id '))
        birth = input('enter actor birthdate ')

        with sqlite3.connect('movie_database.sqlite') as conn :
            cursor = conn.cursor()
            cursor.execute(f"UPDATE actors SET name = '{new_name}', actor_id =  '{a_id}', "
                           f"birthdate = '{birth}', film_id = NULL WHERE actors.name = '{name}'")

            conn.commit()

    def delete_actors():
        name = input('enter actor name to be deleted ')
        with sqlite3.connect('movie_database.sqlite') as conn :
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM actors WHERE actors.name = '{name}'")

            conn.commit()

    def delete_films():
        date = input('enter year for the films after it to be deleted ')
        with sqlite3.connect('movie_database.sqlite') as conn :
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM films WHERE films.date > '{date}'")

            conn.commit()


if __name__ == '__main__':
    def main_menu():
        ans = True
        while ans :
            print("""
            1. Show all films in the movie database
            2. Show actors for the given film
            3. Show all films after the given date
            4. Show actors that were also directors
            5. Add a new actor
            6. Update info about the actor
            7. Delete the given actor from the database
            8. Delete films after the given year
            9. Save database to csv format
            10. Save database to json format
            
            11. Exit/Quit
            """)
            ans = input("What would you like to do? ")
            if ans == "1" :
                print('Films in the database:')
                print('=============================================')
                Requests.show_all_films()
            elif ans == "2" :
                f_title = input('Enter film ')
                print(f'Actors in {f_title} film: ')
                print('=============================')
                Requests.show_actors(f_title)
            elif ans == "3" :
                date = input('Enter date ')
                print(f'Films after {date} year: ')
                print('=============================================')
                Requests.show_films_with_date(date)
            elif ans == "4" :
                print('The actors that were also directors')
                print('*********************************************')
                Requests.show_actors_directors()
            elif ans == "5":
                ChangeInfo.insert_actors()
                print('The information has been successfully changed')
            elif ans == "6":
                ChangeInfo.update_actors()
                print('The information has been successfully changed')
            elif ans == "7":
                ChangeInfo.delete_actors()
                print('The actor has been deleted from the database')
            elif ans == "8":
                ChangeInfo.delete_films()
            elif ans == "9":
                Database.csv_save()
                print("Thank you. The file was saved as 'films_data.csv'")
            elif ans == "10":
                Database.csv_save()
                Database.json_save()
                print("Thank you. The file was saved as 'films_data.json'")
            elif ans == "11":
                print("\n Goodbye")
                ans = None
            else :
                print("\n Not Valid Choice Try again")


    main_menu()
