CREATE TABLE netflix_disney AS
SELECT *
FROM (
    SELECT title, type, director, actors, country, date_added, release_year, rating, duration, listed_in, description
    FROM netflix
    UNION ALL
    SELECT title, type, director, actors, country, date_Added, release_Year, rating, duration, listed_In, description
    FROM disney
) t;


CREATE OR REPLACE FUNCTION top_five_longest_movies(year_val INTEGER)
RETURNS TABLE (
    movie_title VARCHAR,
    movie_duration INTEGER
) AS $$
BEGIN
    RETURN QUERY
        SELECT title, CAST(duration AS INTEGER)
        FROM netflix_disney
        WHERE release_year = year_val AND duration ~ '^[0-9]+$'
        ORDER BY CAST(duration AS INTEGER) DESC
        LIMIT 5;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM top_five_longest_movies(2020);