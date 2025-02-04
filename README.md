# Reddit Comment Scraper

This Python script scrapes comments from Reddit using the Pullpush.io API. It allows you to search for comments based on various criteria, including keywords, author, subreddit, and date range.  The scraped data is saved in JSON format. I likely will not keep adding to this project, since it was meant as a one-time thing for a research project I was asked to help on.

## Usage

```Bash
python reddit_scraper.py
```

The script will prompt you to enter commands to filter the data. Here's a list of the available commands:

- q: Text to search for.
- ids: ID of a specific comment to look for.
- size: Maximum number of comments to retrieve (if less than 100). If you want to retrieve more than 100 comments, simply don't use this command.
- sort: Sorting order (asc for ascending, desc for descending).
- sort_type: What to sort by (score, num_comments, created_utc).
- author: Name of the author to search for.
- subreddit: Name of the subreddit to search in.
- after: Date to start the search (Epoch time). Required.
- before: Date to end the search (Epoch time). Required.
- link_id: ID of a specific post to find comments from.
- output: Name of the output file (default is Scraped_comments.json). The file extension .json will be added automatically.
- start or s: Start the scraping process.
- help: Display this help message.

Example:
```
    Welcome to the Reddit Comment Data Tool!
    Please enter the command you want to run: q
    Please enter the term to search: python
    Please enter the command you want to run: subreddit
    Please enter the subreddit to scrape: learnpython
    Please enter the command you want to run: after
    Enter the date you want scraped after (In format Epoch Time): 1678886400  # Example: March 15, 2023
    Please enter the command you want to run: before
    Enter the date you want scraped before (Epoch time): 1703798400 # Example: December 29, 2023
    Please enter the command you want to run: start
    Transfer in progress...
    ... (scraping progress) ...
    Transfer Successful
```

## Output

The scraped comments will be saved in a JSON file. This file will contain every attribute for each comment that the pullshift API provides (e.g. body, author, created_utc, score, etc.)

## Rate Limiting

This script has a crude handling of rate limitings, only making the code wait 3 seconds for every request. If the code runs too slowly, lower or remove the `sleep(3)` command in line 20.

## Error handling

The script has error handling for API invalid input, timeouts, and API connection problems. For any error, a message will print to console

# Contributing

Contributions are welcome! Please open an issue or submit a pull request. This is my first time dealing with API calls and it isn't meant to be a program for wide use. I just saw that there was no automated way to get Reddit comments from the pushshift API, so I decided to release this despite being made for very limited personal use.

