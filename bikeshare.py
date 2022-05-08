import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = input("\nPlease select a city to filter by via typing one out below: Chicago, New York City or Washington?\n")
        if city not in ('Chicago', 'New York City' or 'Washington'):
            print("Whoops! Typo alert! Try write out your city option again: Chicago, New York City or Washington?")
            city= input().lower()
            continue
        else:
            print("Great choice! :)")
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        month = input("\nPlease select a month to filter by via typing one out below: January, February, March, April, May, June or type 'all' if you want no filter applied.\n")
        if month not in ('January', 'February', 'March', 'April', 'May', 'June' or 'all'):
            print("Oopsies - did you mispell a month? Don't worry, I won't tell anyone! Try write out your option again: January, February, March, April, May, June or type 'all' if you want no filter applied.\n")
            month=input().lower()
            continue
        else:
            print("Fantastic :)")
            break

    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day = input("\nPlease select a day to filter by via typing one out below: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type 'all' if you want no filter applied.\n")
        if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' or 'all'):
            print("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type 'all' if you want no filter applied.\n")
            day=input().lower()
            continue
        else:
            print("Getting some data for you now...")
            break



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['Day'].mode()[0]
    print('Most common day of week:', popular_day)


    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Hour'].mode()[0]
    print('Most common start hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station:', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df.groupby['Start station', 'End Station'].idxmax()
    print('The most frequent combination of start station and end station:', common_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    total_travel_time_hrs = total_travel_time/3600
    print('Total travel time:', total_travel_time_hrs, 'hours')


    # TO DO: display mean travel time
    avg_travel_time=df['Trip Duration'].mean()
    avg_travel_time_mins=avg_travel_time/60
    print('Average travel time:', avg_travel_time_mins, 'minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:', user_types)


    # TO DO: Display counts of gender
    gender_count = df['Gender Count'].value_counts()
    print('Count of genders:', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Earliest Year'].min()
    print('Earliest Year:', earliest_year)
    
    most_recent_year = df['Most Recent Year'].max()
    print('Most Recent Year:', most_recent_year)
    
    common_year = df['Most Common Year'].value_counts().idxmax()
    print('Most Common Year:', common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of data from city spreadsheet"""
    
    while True:
        option=['yes','no']
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
        if view_data in option:
           option=='yes':
           start_loc = 0
           print(df.iloc[start_loc:5])
           break
        else:
            print("Try again!")
      
    while True:
        option=['yes','no']
        view_display = input("Do you wish to continue with 5 more rows? Type yes/no? ").lower() 
        if view_display in option:
           option=='yes':
           start_loc = 5
           print(df.iloc[start_loc:10])
           break
        else:
            print("Ok :)")

    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
