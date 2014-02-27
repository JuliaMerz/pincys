# _Project_
_Description: Meet Pincy's, Pintrest + Macy's. This Chrome extension places an unobtrusive button on the Pintrest UI that when clicked, searches the pin on Macy's and returns the best matching results.

## _Technologies Used_
1. Flask 
..* A Flask server to generate the content for the extension
2. SQLAlchemy
..* Database of the product suggestions returned by Macy's, with information on their user rating, views, clickthrough rate, and Mechanical Turk rating.
3. Amazon Mechanical Turk
..* Leverages the power of MTurk to provide ratings for how closely suggestions match pins.
..* Popular pins can be submitted in batches to MTurk for human pairing with products from Macy's.