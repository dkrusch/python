-- Query all of the entries in the Genre table
SELECT * FROM Genre;

-- Using the INSERT statement, add one of your favorite artists to the Artist table.
INSERT INTO Artist (ArtistId, ArtistName, YearEstablished)
VALUES (null, "Death Grips", 2011);
SELECT * FROM Album;
DELETE FROM Artist WHERE ArtistId=29;
SELECT * FROM Song;
-- Using the INSERT statement, add one, or more, albums by your artist to the Album table.
INSERT INTO Album (AlbumId, Title, ReleaseDate, AlbumLength, Label, ArtistId, GenreId)
VALUES (null, "Exmilitary", "05/28/2011", 2654, "Epic", 28, 13);
-- Using the INSERT statement, add some songs that are on that album to the Song table.
INSERT INTO Song (SongId, Title, SongLength, ReleaseDate, GenreId, ArtistId, AlbumId)
VALUES (null, "Beware", 230, "2/5/2011", 13, 28, 23),
(null, "Guillotine", 193, "2/5/2011", 13, 28, 23),
(null, "Takyon", 212, "10/23/2010", 13, 28, 23);
SELECT * FROM Song;
-- Write a SELECT query that provides the song titles, album title, and artist name for all of the data you just entered in. Use the LEFT JOIN keyword sequence to connect the tables, and the WHERE keyword to filter the results to the album and artist you added.
SELECT s.Title, s.ReleaseDate, a.Title FROM Song s left JOIN Album a ON a.AlbumId = s.AlbumID;


-- Reminder: Direction of join matters. Try the following statements and see the difference in results.

-- SELECT a.Title, s.Title FROM Album a LEFT JOIN Song s ON s.AlbumId = a.AlbumId;
-- SELECT a.Title, s.Title FROM Song s LEFT JOIN Album a ON s.AlbumId = a.AlbumId;
-- Write a SELECT statement to display how many songs exist for each album. You'll need to use the COUNT() function and the GROUP BY keyword sequence.
SELECT a.Title, COUNT(s.AlbumId) FROM Album a left JOIN Song s ON a.AlbumId = s.AlbumID
GROUP BY a.AlbumId;

-- Write a SELECT statement to display how many songs exist for each artist. You'll need to use the COUNT() function and the GROUP BY keyword sequence.
SELECT a.ArtistName, COUNT(s.Title) FROM Artist a left JOIN Song s ON a.ArtistId = s.ArtistID
GROUP BY a.ArtistId;
-- Write a SELECT statement to display how many songs exist for each genre. You'll need to use the COUNT() function and the GROUP BY keyword sequence.
SELECT g.Label, COUNT(s.Title) FROM Genre g left JOIN Song s ON g.GenreId = s.GenreID
GROUP BY g.GenreId;

-- Using MAX() function, write a select statement to find the album with the longest duration. The result should display the album title and the duration.
SELECT Title, MAX(AlbumLength) From Album;

-- Using MAX() function, write a select statement to find the song with the longest duration. The result should display the song title and the duration.
SELECT Title, MAX(SongLength) From Song;

-- Modify the previous query to also display the title of the album.
SELECT s.Title, a.Title, MAX(s.SongLength) From Song s LEFT JOIN Album a ON a.AlbumId = s.AlbumId;