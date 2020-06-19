# Bikeshare Project 

## Description
Bikeshare Project from Udacity for [Programming for Data Science with Python](https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104)
Python code to import US bike share data from Motivate for popular cities Washington, New York, and Chicago.
The code answers questions about the data by computing descriptive statistics. Takes in raw input to create an interactive experience in the terminal to present these statistics.

### Available Filters
You will asked if you want to filter the data depending on:
**City**: This filters the data by city
**Month**: This filters the data by month
**Weekday**: This filters the data by weekday

### Results
You will be asked if you want to see the raw data of the filtered data.
The following statistics are shown depending on you choices:
**The most frequent times of travel**: Most common month, weekday and start hour
**the most popular stations and trip**: Most commonly used start station, end station and combination of start station and end station trip
**Total and average trip duration**: Total travel time and mean travel time
**Statistics on bikeshare users**: Counts of user types, counts of gender, earliest, most recent, and most common year of birth

## Files used
* main.py
* data/chicago.csv
* data/new_york_city.csv
* data/washington.csv

## Technology and dependency
The code is created with python. You will need following packages:
* [time](https://docs.python.org/fr/3/library/time.html)
* [pandas](https://pypi.org/project/pandas/)

## Setup
If you haven't installed pandas yet, you can install it with the **pip** command:
```
$ pip install pandas
```

You will need to unzip data.zip to create the .csv files in a subfolder data. You can do it manually or use the following command:
```
$ unzip data.zip
```

## Use
To run this project, go to the folder of the project and run the following code in your console:

```
$ cd pdsnd_github
$ python main.py
```

## Source
This project is inspired from [Udacity](https://www.udacity.com). 

## License
This code is licensed under the [MIT](https://opensource.org/licenses/mit-license.php) license
Copyright © 2020, Xavier Vare