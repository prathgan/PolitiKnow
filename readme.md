# PolitiKnow
PolitiKnow is a web application developed by Pratham Gandhi for voters and politicians in the United States.
Similar to the popular dating app Tinder, PolitiKnow uses a like-dislike system to learn what types of
politicians a voter likes and dislikes, and trains a machine learning model on that information, which it
later uses to predict if a user might be interested in learning more about a given candidate. Depending on this
prediction, PolitiKnow gathers a constantly updating list of politicians' profiles to show to voters, allowing
voters to learn more about candidates they might be interested in voting for in various election scenarios,
including local, state, and national elections, and thus make the most informed decision when deciding who to
vote for. Additionally, this platform allows politicians to distribute information about their political stance
and campaign more effectively. If a voter so chooses, they can use the "discover" page of PolitiKnow to learn not
only about candidates which PolitiKnow thinks they might be interested in, but all other candidates as well. Users
can tailor their "discover" functionality to include various types of candidates, including those who directly oppose
their views, all candidates, those of a certain party, and many more categories.
## Running PolitiKnow Locally
**Please note**: there currently exists no production build of PolitiKnow which is hosted anywhere. Thus, it can only be run
locally and all data and machine learning is stored and executed locally. A production build is in the works and will be
hosted online soon with cloud data storage and ML. Stay tuned.


To run your own local instance of PolitiKnow, download the `.zip` of this repository from its GitHub page. Then,
`cd` to the root of the PolitiKnow directory and execute the following terminal commands:
- `mkdir data`
- `cd data`
- `mkdir models`
- `cd ../../`
- `pip install -r requirements.txt`

While those dependency installs are running, create a `.csv` file in the `data` subdirectory, and fill it using the spreadsheet application or text
editor of your choice in the following manner:

|    | 1                 |
|----|-------------------|
| 0  | Filler            |
| 1  | filler@filler.com |
| 2  | filler            |
| 3  | 1                 |
| 4  | 1                 |
| 5  | 1                 |
| 6  | 1                 |
| 7  | 1                 |
| 8  | 1                 |
| 9  | 1                 |
| 10 | 1                 |
| 11 | 1                 |
| 12 | 1                 |
| 13 | 1                 |
| 14 | 1                 |
| 15 | 1                 |
| 16 | 1                 |
| 17 | 1                 |
| 18 | 1                 |
| 19 | 1                 |

Then, after the `.csv` file has been created and all dependencies are installed, `cd` to the root of the PolitiKnow directory again, and run `export FLASK_APP`. Finally, run `flask run` from the root of the directory and you're all set!
Navigate to the url displayed in your terminal window after you ran the last command and you can start using PolitiKnow!
