import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
valid_months = ['january', 'february', 'march', 
              'april', 'may', 'june',
              'july', 'august', 'september',
              'october', 'november', 'december', 'all']  
          
valid_weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def isAMonth(s):
    """
    Checks if the value s is a valid month

    Returns:
        (int) month - the month or (boolean) False if the value is invalid
    """

    try:     
        if s in valid_months:
           return int(valid_months.index(s)) +1
        elif 1 <= int(s) <= 12:
           return int(s)
        else:
           return False
    except ValueError:
        return False
        
def isAWeekday(s):
    """
    Checks if the value s is a valid weekday

    Returns:
        (int) weekday - the weekday or (boolean) False if the value is invalid
    """

    try:     
        if s in valid_weekdays:
           return int(valid_weekdays.index(s)) +1
        elif 1 <= int(s) <= 7:
           return int(s)
        else:
           return False
    except ValueError:
        return False

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    valid_cities = { 'c': 'chicago', 'chicago': 'chicago',
              'n': 'new york city', 'ny': 'new york city', 'nyc': 'new york city', 
              'new york': 'new york city', 'new york city': 'new york city',
              'w': 'washington', 'washington': 'washington' }
    

    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("")
    print("1 - Let's choose first a city")
    city = None
    while city is None or valid_cities.get(city) is None :
       try:
          print("\nValid values are (capital letters don't matter):")
          print("- c or chicago for Chicago")
          print("- n, ny, nyc, new york and new york city for New York City")
          print("- w or washington for Washington")
          print()
          city = input("Which city do you want to choose ? : ").lower()
          if valid_cities.get(city) is None:
             print()
             print("You have entered a wrong value. Could you please try again?") 
          else:
             print()
             print("You have choosen: ", valid_cities.get(city).title())
       except (ValueError, KeyboardInterrupt):
          print()
          print("It seems there is an issue with the value that you entered. Could you please try again?") 

    # TO DO: get user input for month (all, january, february, ... , june)
    print("")
    print("2 - Let's choose a month now")
    month = None
    while month is None or not isAMonth(month) :
       try:
          print("\nValid values are (capital letters don't matter):")
          print("- all for every month")
          print("- january, february, march... Months written in English")
          print("- 1, 2, 3... Months written as a number, beginning with January as 1")
          print()
          month = input("Which month(s) do you want to choose ? : ").lower()
          resultMonth = isAMonth(month)
          if not resultMonth or month == '0' :
             print()
             print("You have entered a wrong value. Could you please try again?") 
          else:
            print()
            print("You have entered (month):", month)
            #print("{} is saved for the following calculation.".format(resultMonth.title()))
       except (ValueError):
          if not resultMonth:
            print()
            print("It seems there is an issue with the value that you entered. Could you please try again?") 
       except (KeyboardInterrupt):
          print()
          print("It seems there is an issue with the value that you entered. Could you please try again?") 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("")
    print("3 - And let's choose a weekday to finish")
    weekday = None
    while weekday is None or not isAWeekday:
       try:
          print("\nValid values are (capital letters don't matter):")
          print("- all for all weekdays")
          print("- monday, tuesday, wednesday... Days written in English")
          print("- 1, 2, 3... Weekdays written as a number, with Monday as 1 and Sunday as 7")
          print()
          weekday = input("Which weekday(s) do you want to choose ? : ").lower()
          resultWeekday = isAWeekday(weekday)
          if not resultWeekday or weekday == '0':
             print()
             print("You have entered a wrong value. Could you please try again?") 
             weekday = None
          else:
            print()
            print("You have entered (weekday):", weekday)
       except (ValueError):
          if not resultWeekday:
            print()
            print("It seems there is an issue with the value that you entered. Could you please try again?")
       except (KeyboardInterrupt):
          print()
          print("It seems there is an issue with the value that you entered. Could you please try again?")


    print('-'*40)
    return valid_cities.get(city), resultMonth, resultWeekday


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - index of the month, beginning at one. 13 means all months
        (str) day - index of the day of week, beginning at one. 8 means "all"
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv('data/' + CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 13:
        df = df.loc[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 8:
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day -1]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_weekday = df['day_of_week'].mode()[0]
 
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Frequent:\n- Month: {}\n- Weekday: {}\n- Start Hour: {}'.format(
        valid_months[popular_month].title(), valid_weekdays[popular_weekday].title(), popular_hour)) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Stations '] = df['Start Station'] + ' - ' + df['End Station']
    popular_combination_stations = df['Start End Stations '].mode()[0]
    
    print('Most Frequent:\n- Start Station: {}\n- End Station: {}\n- Combination of Start and End station: {}'.format(
        popular_start_station.title(), popular_end_station.title(), popular_combination_stations))     

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('- Total travel time:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('- Mean travel time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def see_raw_data(df):
    """
    Displays 5 rows of raw data until the user confirms 
    he doesn't want to see the raw data.
    """
    
    answer = None
    interact = 1

    while answer is None or answer.lower() != 'no':
    
       if interact == 1:
          print("")
          print("Do you want to see the 5 first rows of raw data ?")
          answer = input("Please choose between yes and no (capital letters don't matter):").lower()
          if answer.lower() == 'yes':
            print("")
            print(df.head())
            interact += 1
    
       if (answer.lower() == 'yes' or answer.lower() == 'y') and interact > 1:
          print("")
          print("Do you want to see the following 5 rows of raw data ?")
          answer = input("Please choose between yes and no (capital letters don't matter):").lower()
       
       if answer.lower() == 'yes' or answer.lower() == 'y':
          print("")
          print(df[(interact-1)*5:interact*5])
          interact += 1       
       
       if answer.lower() == 'no' or answer.lower() == 'n':
          break
          
       if answer.lower() != 'yes' and answer.lower() != 'y':
          print("")
          print("You have entered an invalid value, please enter yes or no (capital letters don't matter)")
          answer = 'yes'

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('- Count of user types:')
    try:
        user_types = dict(df['User Type'].value_counts())
        for x in user_types:
            print('{}: {}'.format(x, user_types[x]))
    except (KeyError):
        print('There is no data concerning user types in our database. Try another month and/or city.')

    # TO DO: Display counts of gender
    print('\n- Count of genders:')
    try:
        gender = dict(df['Gender'].value_counts())
        for x in gender:
            print('{}: {}'.format(x, gender[x]))
    except (KeyError):
        print('There is no data concerning the gender in our database. Try another month and/or city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\n- Information concerning the year of birth:')
    try:
        print('Earliest year of birth:', int(df['Birth Year'].min()))
        print('Most recent year of birth:', int(df['Birth Year'].max()))
        print('Most common year of birth:', int(df['Birth Year'].mean()))
    except (KeyError):
        print('There is no data concerning the birth year in our database. Try another month and/or city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    """Main function launched automatically"""
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        see_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
