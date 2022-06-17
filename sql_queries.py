# DROP TABLES

songplay_table_drop = " DROP TABLE IF EXISTS songplays"
user_table_drop = " DROP TABLE IF EXISTS users"
song_table_drop = " DROP TABLE IF EXISTS songs"
artist_table_drop = " DROP TABLE IF EXISTS artists"
time_table_drop = " DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (songplay_id int PRIMARY KEY, start_time time, user_id int,\
level Varchar, song_id int, artist_id int, session_id int, location Varchar, user_agent text)
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users ( user_id int PRIMARY KEY, first_name Varchar,\
last_name Varchar, gender Varchar, level Varchar)
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR PRIMARY KEY, title text ,artist_id Varchar, year int, duration float)
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (artist_id Varchar PRIMARY KEY, name Varchar, location Varchar, latitude float, longitude float)
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY , hour float, day float, week float, month float, year float, weekday float)
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays (songplay_id , start_time , user_id ,level , song_id , artist_id , session_id , location , user_agent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert = (""" INSERT INTO users (user_id , first_name , last_name , gender , level ) VALUES (%s, %s, %s, %s, %s) CONFLICT (user_id) DO NOTHING
""")

song_table_insert = (""" INSERT INTO  songs (song_id , title , artist_id , year, duration ) VALUES (%s, %s, %s, %s, %s) CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = (""" INSERT INTO  artists (artist_id , name , location , latitude , longitude ) VALUES (%s, %s, %s, %s,%s) CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = (""" INSERT INTO time (start_time , hour , day , week , month , year , weekday ) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = (""" SELECT s.song_id, s.artist_id FROM songs s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]