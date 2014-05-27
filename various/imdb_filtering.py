#!/usr/bin/env python2
#

# Analysing data from text files (in this case length of movies/tv-shows from imdb)
# data source: ftp://ftp.fu-berlin.de/pub/misc/movies/database/
# exercise source: http://jmduke.com/posts/no-movies-havent-gotten-much-longer/

from os.path import expanduser
import pandas

# File location
home = expanduser("~")
length_file = home+"/var/running-times.list"


def process_file():

    # Get data but exclude clutter (first 15 and last 2 lines)
    all_data = open(length_file).readlines()[15:-2]
    
    # Empty list to store processed data in
    parsed_data = []

    for line in all_data:

        # TV shows and videos shouldn't be included
        if "{" in line and "}" in line:
            continue
        if "(TV)" in line or "(V)" in line:
            continue
        if "\"" == line[0]:
            continue
            
        split_line = line.split('\t')

        try:
            # Get the first column.
            release_date = split_line[0]
            # First column looks like MOVIE_NAME (RELEASE_YEAR), so split at "(" and grab everything after.
            release_date = release_date.split("(")[1]
            # Years are four digits (and numerical), right?
            release_date = int(release_date[:4])
            # Some titles are from the future or the stone age, for whatever reason.
            # Skip those.
            if release_date > 2014 or release_date < 1895:
                continue

            # Get the last column if it's got what we want; otherwise grab the one before it, for cases like:
            # > Zubin and the I.P.O. (1983) (TV)            USA:59  (with commercials)
            run_time = split_line[-1] if "(" not in split_line[-1] else split_line[-2]
            # Some of the lines are in the form of COUNTRY:TIME, so split at the colon. 
            run_time = run_time.split(":")[-1]
            # Strip the newline character and convert to integer.
            run_time = int(run_time.strip())
            # Skip current title if it's too long or short
            if run_time < 45 or run_time > 360:
                continue

            # Finally, add it to our list of processed titles
            parsed_data.append([release_date, run_time])
        except:
            pass

    return filter(lambda x: x[1] % 30, parsed_data)

def create_stats():

    parsed_films = process_file()
    films = pandas.DataFrame(parsed_films)
    print films.describe()

if __name__ == "__main__":
    create_stats()
