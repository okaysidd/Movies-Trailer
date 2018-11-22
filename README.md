# Movies-Trailer

## Introduction
This project was part of Udacity Python foundation course.
It involves building a simple backend for a movies trailer website.

## Note
The Udacity project required, at the minimum, to save movies data once and create web page out of them.
<i>I took some time to add the option for the user to add new movies. Also the current movies data and any new added is now not stored in the python file, but is inside a separate JSON file.</i>

## How to use
This project has been developed on **Python 3.6.7 version**.
Also **python module - The Movie Database (tmdb)*** is required for the <i>entertainment_udacity.py</i>.
To download- run ```pip3 install tmdbsimple```.


To get the project running, add the following files in a folder-
- <i>entertainment_api.py</i> (uses API provided by tmdb to fetch new movies)
- <i>fresh_tomatoes.py</i> (updated with story line display)
- <i>movies.py</i>
- <i>movies_details.json</i>

Run the <i>entertainment_api.py</i> file.

The class is defined in the <i>movies.py</i> file. The <i>entertainment_api.py</i> runs and gives user option to add new movies. The loaded movies can be saved permanently to be used later on in the  <i>movies_details.json</i> file. The <i>fresh_tomatoes.py</i> file contains the front end of the trailer website, also written inside python.

<i>The story line data is now available through the **Story line** button below each movie poster, and opens a modal with the movie story</i>


The <i>fresh_tomatoes.html</i> file in the repository is the sample result that was created using the Python files, as per the process mentioned above.

In case the tmdb module is not available, <i>entertainment_udacity.py</i> and <i>entertainment_json.py</i> are also available in the repository, which are simpler versions of the project, with similar visual outputs.

** *more details about 'the movie database' [here](https://www.themoviedb.org/documentation/api). **
