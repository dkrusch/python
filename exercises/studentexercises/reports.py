import sqlite3

class Song():

    def __init__(self, title, releasedate, genreid, artistid, albumid):
        self.title = title
        self.releasedate = releasedate
        self.genreid = genreid
        self.artistid = artistid
        self.albumid = albumid

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Daniel/workspace/python/exercises/music-history/musichistory.db"

    def all_songs(self):

        """Retrieve all songs with the album name"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            # db_cursor.execute("""
            # select s.SongId,
            #     s.Title,
            #     s.ReleaseDate,
            #     a.Title
            # from Song s
            # join Album a on s.AlbumId = a.AlbumId
            # order by s.AlbumId
            # """)

            db_cursor.execute("""
            select s.SongId,
                s.Title,
                s.ReleaseDate,
                a.Title
            from Song s
            join Album a on s.AlbumId = a.AlbumId
            order by s.AlbumId
            """)

            all_students = db_cursor.fetchall()

            # song = Song("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE", "releasedate", 3, 15, 20)
            # print(f'{song.title} is in {song.releasedate}')

            # for student in all_students:
            #     print(f'{student[1]}, released on {student[2]}, is in the album {student[3]}')

    def all_albums(self):

        """Retrieve all songs with the album name"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            # db_cursor.execute("""
            # select s.SongId,
            #     s.Title,
            #     s.ReleaseDate,
            #     a.Title
            # from Song s
            # join Album a on s.AlbumId = a.AlbumId
            # order by s.AlbumId
            # """)

            db_cursor.execute("""
            select a.AlbumId,
                a.Title,
                a.ReleaseDate
            from Album a
            """)

            all_students = db_cursor.fetchall()

            # song = Song("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE", "releasedate", 3, 15, 20)
            # print(f'{song.title} is in {song.releasedate}')

            # for student in all_students:
            #     print(f'{student[1]}, released on {student[2]}')

    def album_artist(self):

        """Retrieve all songs with the album name"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.AlbumId,
                s.Title,
                a.ArtistId,
                a.ArtistName
            from Album s
            join Artist a on s.ArtistId = a.ArtistId
            order by a.ArtistName
            """)

            # db_cursor.execute("""
            # select a.AlbumId,
            #     a.Title,
            #     a.ReleaseDate
            #     ar.ArtistName
            # from Album a
            # join Artist ar on a.ArtistId = ar.ArtistId
            # order by a.ArtistId
            # """)

            alb_art = db_cursor.fetchall()



            # for student in alb_art:
            #     print(f'{student[1]}, by {student[3]}')

            artists = {}

            for song in alb_art:
                album_id = song[0]
                album_name = song[1]
                artist_id = song[2]
                artist_name = song[3]

                if artist_name not in artists:
                    artists[artist_name] = [album_name]
                else:
                    artists[artist_name].append(album_name)

            print(artists)

    def all_ongs(self):

        """Show what albums each artist is working on """

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select ar.ArtistId,
                ar.ArtistName,
                a.Title
            from Artist ar
            join Album a on ar.ArtistId = a.ArtistId
            order by a.ArtistId
            """)

            all_artists = db_cursor.fetchall()

            artist_works = {}

            for artist in all_artists:
                song_id = artist[0]
                artist_name = artist[1]
                title = artist[2]

                if artist_name not in artist_works:
                    artist_works[artist_name] = [title]
                else:
                    artist_works[artist_name].append(title)

            for artist, albums in artist_works.items():
                print(f"{artist} is working on:")
                for album in albums:
                    print(f"\t* {album}")

    def song_by_album(self):

        """Show what albums each artist is working on """

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.SongId,
                s.Title,
                a.Title
            from Song s
            join Album a on s.AlbumId = a.AlbumId
            order by s.ArtistId
            """)

            all_artists = db_cursor.fetchall()

            album_song = {}

            for artist in all_artists:
                song_id = artist[0]
                song_title = artist[1]
                album_title = artist[2]

                if album_title not in album_song:
                    album_song[album_title] = [song_title]
                else:
                    album_song[album_title].append(song_title)

            # for artist, albums in album_song.items():
            #     print(f"{artist} has the songs:")
            #     for album in albums:
            #         print(f"\t* {album}")




            {
                print(f"{album} has the songs:") for album, songs in album_song.items()
            }

            # {
            #     print(f"\t* {song}"):
            #     {
            #        print(f"{album} has the songs:")
            #     }
            #     for album, songs in album_song.items() for song in songs
            # }




reports = StudentExerciseReports()
# reports.all_songs()
# reports.all_ongs()
# reports.all_albums()
# reports.album_artist()
reports.song_by_album()