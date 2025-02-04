import json
import requests
import time
import datetime

def get_comments(q, ids, size, sort, sort_type, author, subreddit, after, before, link_id, output_file):
    raw_data = requests.get(f'https://api.pullpush.io/reddit/search/comment/?q={q}&ids={ids}&size={size}&sort={sort}&sort_type={sort_type}&author={author}&subreddit={subreddit}&after={after}&before={before}')
    data = json.loads(raw_data.text)

    all_data = []

    newtime = int(data['data'][-1].get('created_utc'))
    start_time = newtime
    start_date = datetime.datetime.fromtimestamp(newtime).strftime('%c')
    print('I am currently looking at: ' + start_date)

    while newtime < int(before):
        print('Transfer in progress...')
        print()
        time.sleep(3)

        new_raw_data = requests.get(f'https://api.pullpush.io/reddit/search/comment/?q={q}&ids={ids}&size={size}&sort={sort}&sort_type={sort_type}&author={author}&subreddit={subreddit}&after={newtime}&before={before}')
        new_data = json.loads(new_raw_data.text)
        if new_data and ('data' in new_data) and new_data['data']:
            all_data.extend(new_data['data'])
            testtime = int(new_data['data'][-1].get('created_utc'))
            if (int(newtime) != int(testtime)):
                time_left_percentage = (100 * round(((newtime - start_time) / (int(before) - start_time)), 2))
                current_date = datetime.datetime.fromtimestamp(newtime).strftime('%c')
                newtime = testtime
        else:
            with open(output_file, "w") as destination:
                json.dump(all_data, destination, indent=4)
                print('The newest comment retreived was at: ' + datetime.datetime.fromtimestamp(newtime).strftime('%c'))
                return

        print('I am currently looking at: ' + current_date)
        print(f'I am {time_left_percentage}% done!')



def main():
    q=''
    ids=''
    size=''
    sort=''
    sort_type=''
    author=''
    subreddit=''
    after= ''
    before=''
    link_id=''
    output_file = 'Scraped_comments.json'
    running = False
    while running == False:
        print('Type HELP for a list of commands.')
        user_input = input('Welcome to the Reddit Comment Data Tool!\n Please enter the command you want to run: ')
        if (user_input.lower() == 'q'):
            q = input('Please enter the term to search: ')
        elif(user_input.lower() == 'ids'):
            ids = input('Please enter the comment ID: ')
        elif(user_input.lower() == 'size'):
            size = input('Please enter the desired amount of results if less than 100: ')
        elif(user_input.lower() == 'sort'):
            sort = input('Please enter the desired sort type (asc, desc): ')
        elif(user_input.lower() == 'sort_type'):
            sort_type = input('Please enter the sort type (score, num_comments, created_utc): ')
        elif(user_input.lower() == 'author'):
            author = input('Please enter the name of the author you want to scrape: ')
        elif(user_input.lower() == 'subreddit'):
            subreddit = input('Please enter the subreddit to scrape: ')
        elif(user_input.lower() == 'after'):
            after_temp = input('Enter the date you want scraped after (In format Epoch Time): ' )
            if (before != '') and (int(after_temp) >= int(before)):
                print('\'after\' cannot be bigger than \'before\'')
            else:
                after = after_temp
        elif(user_input.lower() == 'before'):
            before_temp = input('Enter the date you want scraped before (Epoch time): ')
            if (after != '') and (int(before_temp) <= int(after)):
                print('\'before\' cannot be smaller than \'after\'')
            else:
                before = before_temp
        elif(user_input.lower() == 'link_id'):
            link_id = input('Please enter the post ID: ')

        elif(user_input.lower() == 'output'):
            output_file = input('Please enter the output file name: ')
            output_file += '.json'

        elif(user_input.lower() == 'start') or (user_input.lower() == 's'):
            if (after == '') and (before == ''):
                print('Please enter an upper and lower boundary.(\'after\' and \'before\' command\')')
            elif (after == ''):
                print('Please enter a lower date boundary (\'after\' command\')')
            elif (before == ''):
                print('Please enter an upper date boundary (\'before\' command)')
            else:
                print()
                running = True

        elif(user_input.lower() == 'help'):
            print('List of commands: \n Q: text to search for \n Ids: ID of comment to look for \n Size: If you want less than 100 comments returned, this is the command for you! \n Sort: Style to sort. 2 inputs accepted: Ascending and Descending order \n Sort_type: What to sort *for*, accepts score (amount of upvotes), num_comments (How many comments does the comment have?, created_utc (sort by time))) \n Author: Lets you find comments from specific author \n Subreddit: What subreddit do you want to look for? \n After: Date to start search (Epoch time) \n Before: Date to end search (Epoch time) \n Link_ID: ID of specific comment to find \n Output: Name of output file \n Start: Start the search')
            print()
    try:
        get_comments(q, ids, size, sort, sort_type, author, subreddit, after, before, link_id, output_file)
        print('Transfer Successful')
    except TypeError as e:
        print('\n')
        print(e)
        print('\n \n')
        print('TypeError, likely from an invalid input. Please only use numbers for \'before\' and \'after\'')
    except KeyError as e:
        print('\n')
        print(e)
        print('\n \n')
        print('oops, KeyError. Connection probably timed out. Please try running the program again, and try doing smaller "chunks" of dates')
    except ValueError as e:
        print('\n')
        print(e)
        print('\n \n')
        print('Value Error. Please only use numbers for \'before\' and \'after\'')
    except Exception as e:
        print()
        print(e)
        print('\n \n')
        print('Program failed due to unknown reasons, please try running again.')


if __name__ == '__main__':
    main()


