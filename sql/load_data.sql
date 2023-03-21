\copy netflix FROM '../data/processed/processed_netflix.csv' DELIMITER ';' CSV HEADER;
\copy disney FROM '../data/processed/processed_disney.csv' DELIMITER ',' CSV HEADER;
