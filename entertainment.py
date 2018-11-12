import fresh_tomatoes as ft

import movies

casino_royale = movies.Movies('Casino Royale',
                              'New 007 must is appointed, but is he right for the job?',
                              'https://img.reelgood.com/content/movie/6befffd8-1f0c-405e-91c8-d84d0d080329/poster-780.webp',
                              'https://www.youtube.com/watch?v=36mnx8dBbGE')
#print(casino_royale.movie_story)
#casino_royale.show_trailer()

quantum_of_solace = movies.Movies('Quantum Of Solace',
                                  'An investigation leads Bond on the trail of Dominic Greene, a world-renowned developer of green technology. When Dominic assists a coup in Bolivia to fulfil his own intentions, Bond must save the day.',
                                  'https://hcmoviereviews.files.wordpress.com/2015/10/quantum-of-solace-james-bond-9614441-1280-1024.jpg',
                                  'https://www.youtube.com/watch?v=BBqYaFEWBxI')

skyfall = movies.Movies('Skyfall',
                        'An ex-MI6 agent steals a hard drive with top secret information to carry out a vendetta on Bond\'s overseer, M. Bond must face his past in a bid to try and save M.',
                        'https://m.media-amazon.com/images/M/MV5BNDVhZmJiYWMtNmIzMC00ZWNiLTkzZDYtNGNlZmViMGM4OGExXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg',
                        'https://www.youtube.com/watch?v=6kw1UVovByw')

spectre = movies.Movies('Spectre',
                        'James Bond receives an obscure message from M about a sinister organisation, \'SPECTRE\'. With the help of Madeleine, he uncovers the conspiracy, only to face an ugly truth.',
                        'https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Fscottmendelson%2Ffiles%2F2015%2F11%2Fspectre-banner-3-1200x600.jpg',
                        'https://www.youtube.com/watch?v=6kw1UVovByw')

movies_list = [casino_royale, quantum_of_solace, skyfall, spectre]
ft.open_movies_page(movies_list)
