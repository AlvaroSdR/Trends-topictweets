# Twitter Topic Search
This Python script is designed to search for tweets on a topic specified by the user and save them to an Excel file. The script uses the searchtweets package to collect tweets and the openpyxl package to create and save the Excel file.

## Prerequisites
To run this script, you will need to have the following:

Python 3.x installed
A Twitter Developer Account with access to the Twitter API v2
Credentials for the Twitter API v2 stored in a YAML file named twitter_keys.yaml in the same directory as the script

## Usage
1. Clone or download the repository to your local machine.
2. Open a terminal window and navigate to the directory containing the script.
3. Install the required packages by running the command: pip install -r requirements.txt.
4. Run the script using the command: python search_tweets.py.
5. Enter a topic to search for when prompted.
6. The script will collect up to 100 tweets on the topic and save them to an Excel file named [search_topic]_tweets.xlsx in the same directory as the script.
7. The first sheet of the Excel file will contain all the collected tweets, while the second sheet will contain only tweets that start with one of the following words: "Who", "Why", "What", "When", "Where", or "How".


## Disclaimer
This script is provided as is and without any warranty. Use it at your own risk.

## Contributing
If you would like to contribute to this project, please contact in advance. Any contributions are welcome!

## License
This project is licensed under the My License. In case of use, please contact in advance.

## Contact
If you have any questions or suggestions, feel free to contact me at asanchezdrio@gmail.com.

Thanks for using the voice to text trasncriber!
