-- lists all shows without a genre linked
-- displays: tv_shows.title - tv_show_genres.genre_id
-- genre_id will be NULL for these shows
-- results sorted by tv_shows.title ASC, tv_show_genres.genre_id ASC
-- uses only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
