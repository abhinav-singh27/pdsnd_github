import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        city = input('Would you like to see data for chicago, new york city, washington?').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Please enter correct city names')
        else:
            break
       
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month? all, january, february, march, april, may, june?').lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('Please enter correct month')
        else:
            break

            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day? all, monday, tuesday, wednesday, thursday, friday, saturday, sunday?').lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesdy', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Please enter correct day')
        else:
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    
    common_month = df['month'].mode()[0]
    
    print('\nMost common month:', common_month)


    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    
    common_day = df['day'].mode()[0]
    
    print('\nMost common day:', common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    common_hour = df['hour'].mode()[0]
    
    print('\nMost common start hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station = df['Start Station'].mode()[0]

    
    print('\nMost common start station:', common_station)


    # TO DO: display most commonly used end station
    
    common_end_station = df['End Station'].mode()[0]
    
    print('\nMost common end station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    concat_start_end_station = (df['Start Station']+" and "+df['End Station']).value_counts().idxmax()
    
    print("\nMost frequent Combination of station is between:", concat_start_end_station.split('and')[0],                                 concat_start_end_station.split('and')[1])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_total_seconds= df['Trip Duration'].sum()
        
    total_travel_time = sum_total_seconds / 60 / 60 / 24 / 365.25
     
    print('\nTotal travel time for the city:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print('\nMean travel time in seconds:', mean_travel_time)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    
    print('\nCount of user types:', count_user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        
        print('\nCount of gender:', count_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        
        earliest_birth_year = df['Birth Year'].min()
        
        most_recent_birth_year = df['Birth Year'].max()
        
        common_birth_year = df['Birth Year'].mode()[0]
        
        print("\nEarliest year of birth: " + str(earliest_birth_year))
        
        print("\nMost recent year of birth: " + str(most_recent_birth_year))
        
        print("\nMost common year of birth: " + str(common_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_data(df):
    """
    Displays five lines of raw data if the user types 'yes'.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say 'no'.
    
    """
    # TO DO: handle raw data and display them
    user_input = input('Do you want to see raw data? Enter yes or no.\n')
    count = 0

    while True :
        if user_input.lower() == 'yes':
            print(df.iloc[count : count + 5])
            count += 5
            user_input = input('\nDo you want to see 5 more lines of raw data? Enter yes or no.\n')
        else:
            break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
