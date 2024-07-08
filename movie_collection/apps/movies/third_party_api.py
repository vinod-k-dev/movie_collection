import requests
from django.conf import settings

def fetch_movies(page=1):
    url = f"http://demo.credy.in/api/v1/maya/movies/?page={page}"

    try:
        response = requests.get(url, auth=(settings.MOVIE_API_USERNAME, settings.MOVIE_API_PASSWORD))
        response.raise_for_status()  # Raise an error for bad status codes

        return response.json()
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
        # Return static data or None if desired
        # I passed static data because some time API call is failed we can pass as well real error
        return {
            "count": 45466,
            "next": "https://demo.onefin.in/api/v1/maya/movies/?page=2",
            "previous": None,
            "results": [
                {
                    "title": "Queerama",
                    "description": "50 years after decriminalisation of homosexuality in the UK, director Daisy Asquith mines the jewels of the BFI archive to take us into the relationships, desires, fears and expressions of gay men and women in the 20th century.",
                    "genres": "",
                    "uuid": "57baf4f4-c9ef-4197-9e4f-acf04eae5b4d"
                },
                {
                    "title": "Satana likuyushchiy",
                    "description": "In a small town live two brothers, one a minister and the other one a hunchback painter of the chapel who lives with his wife. One dreadful and stormy night, a stranger knocks at the door asking for shelter. The stranger talks about all the good things of the earthly life the minister is missing because of his puritanical faith. The minister comes to accept the stranger's viewpoint but it is others who will pay the consequences because the minister will discover the human pleasures thanks to, ehem, his sister- in -law… The tormented minister and his cuckolded brother will die in a strange accident in the chapel and later an infant will be born from the minister's adulterous relationship.",
                    "genres": "",
                    "uuid": "163ce013-03e2-47e9-8afd-e7de7688c151"
                },
                {
                    "title": "Betrayal",
                    "description": "When one of her hits goes wrong, a professional assassin ends up with a suitcase full of a million dollars belonging to a mob boss ...",
                    "genres": "Action,Drama,Thriller",
                    "uuid": "720e8796-5397-4e81-9bd7-763789463707"
                },
                {
                    "title": "Siglo ng Pagluluwal",
                    "description": "An artist struggles to finish his work while a storyline about a cult plays in his head.",
                    "genres": "Drama",
                    "uuid": "e9548ee7-6a95-4917-893e-1fa1d3a6de40"
                },
                {
                    "title": "رگ خواب",
                    "description": "Rising and falling between a man and woman.",
                    "genres": "Drama,Family",
                    "uuid": "9b0a4aa2-9ec7-4a3d-98ab-622275f44ea5"
                }
                # Add more static movie entries as needed
            ]
        }
