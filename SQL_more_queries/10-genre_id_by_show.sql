-- list all show contained in hbtn_0d_tvshows 
-- FOREIGN KEY (`show_id`) REFERENCES `tv_shows` (`id`)
-- FOREIGN KEY (`genre_id`) REFERENCES `tv_genres` (`id`)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres 
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;