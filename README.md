# Netflix Analysis

```python

In this project, I am analyzing a dataset from Netflix using Python. The approach is straightforward – examining the data to understand patterns and trends.
The objective is to clean the data, comprehend changes in Netflix content, and identify viewer preferences. The analysis covers ratings, types of content, and durations. Additionally, an interactive feature is available for practical exploration.

# Let's embark on a journey through this Netflix dataset using Python and Pandas.

# Importing the essential libraries for our exploration.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Reading the dataset into a Pandas DataFrame.
df = pd.read_csv("netflix_titles.csv")

# Checking the initial rows to get a glimpse of the data.
df.head(2)

# Exploring the dimensions of our dataset (rows and columns).
df.shape

# Describing the categorical aspects of the data for insights.
df.describe(include='object')

# Gathering general information about the DataFrame.
df.info()

# Identifying missing values across the dataset.
df.isnull().sum()

# Addressing a specific issue: filling null 'duration' values with corresponding 'rating' values.
df[df['duration'].isnull()]
df.loc[df['duration'].isnull(), 'duration'] = df.loc[df['duration'].isnull(), 'rating']

# Checking unique values in the 'rating' column. Variety is the spice of Netflix.
df['rating'].unique()

# Exploring the 'rating' column further. What's the audience watching?
df['rating']

# Understanding the shape of the 'rating' column.
df['rating'].shape

# Filtering out specific values in the 'rating' column to clean up the variety.
df['rating'].unique()

# Tackling outliers: replacing certain 'rating' values with NaN.
df.loc[(df['rating'] == '74 min') | (df['rating'] == '66 min') | (df['rating'] == '84 min'), 'rating'] = np.nan

# Checking the impact of our cleanup on the overall dataset.
df.shape

# Ensuring we've successfully dealt with the outliers.
df['rating'].unique()

# Verifying data types, a crucial step in our exploration.
df.dtypes

# Exploring unique release years within our dataset.
df['release_year'].unique()

# Converting the 'release_year' column into a datetime object for analysis.
df['Date_N'] = pd.to_datetime(df['release_year'], format='%Y')

# Counting the titles added each year. Let's identify trends!
df['Date_N'].dt.year.value_counts()

# Examining the unique values in the 'Date_N' column.
df['Date_N'].unique()

# Cleaning up the 'date_added' column by removing any unwanted whitespaces.
df['date_added'] = df['date_added'].str.strip()

# Transforming 'date_added' into a consistent datetime format.
df['Date_Added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y')

# Verifying the uniqueness of the 'Date_Added' column. Every addition counts.
df['Date_Added'].unique()

# Counting the number of titles for each type – Movies or TV Shows.
df['type'].count()

# Grouping by 'Date_Added' and 'type' to observe the evolving Netflix content landscape.
MovShows = df.groupby('Date_Added')['type'].value_counts().reset_index()
print(MovShows)

# Plotting a bar chart to visualize the number of titles added per year.
plt.figure(figsize=(8, 5))
yr_added = df['Date_Added'].dt.year.value_counts()
ax = sns.barplot(x=yr_added.index, y=yr_added.values, hue=yr_added.values, legend=False)
for container in ax.containers:
    ax.bar_label(container, color='#8f6083')
plt.xlabel('Year Added', color='#8f6083', weight='bold', fontsize=12)
plt.ylabel('Shows & Movies', color='#8f6083', weight='bold', fontsize=12)
plt.title('Number Of Titles Added Per Year', color='#8f6083', weight='bold', fontsize=15)
plt.xticks(ticks=range(14), labels=np.sort(np.array(yr_added.index, dtype=int)))
plt.grid(True, color='#573c5f', alpha=0.1)
plt.show()

# Plotting a bar chart for the count of titles added per year.
plt.figure(figsize=(10, 5))
yr = df['Date_Added'].dt.year.value_counts().reset_index()
ad = sns.barplot(x=yr['Date_Added'], y=yr['count'], hue=yr['count'])
for container in ad.containers:
    ad.bar_label(container, color='#8f6083')
plt.show()

# Plotting a countplot for the distribution of 'type' (Movie/TV Show).
ax = sns.countplot(x=df['type'], hue=df['type'])
for container in ax.containers:
    ax.bar_label(container, label_type='center', color='white', size=14, weight='bold')
plt.ylabel('No. of Titles', color='#3274a1', weight='bold', fontsize=12)
plt.xlabel('Type', color='#3274a1', weight='bold', fontsize=12)
plt.xticks(color='#3274a1', weight='bold', fontsize=10)
plt.show()

# Plotting a countplot for the distribution of 'type' (Movie/TV Show) over the years.
ax = sns.countplot(x=df['type'], hue=df['type'])
for container in ax.containers:
    ax.bar_label(container, label_type='center', color='white', size=14, weight='bold')

plt.figure(figsize=(12, 4))
ay = sns.countplot(x=df['Date_Added'].dt.year, hue=df['type'], width=0.9)
for container in ay.containers:
    ay.bar_label(container)
plt.xticks(ticks=range(14), labels=np.sort(np.array(yr_added.index, dtype=int)))
plt.show()

# Converting 'Date_Added' to datetime and creating a new 'Year' column.
df['Date_Added'] = pd.to_datetime(df['Date_Added'])
df['Year'] = df['Date_Added'].dt.year

# Grouping by 'Year' and 'type' columns, counting occurrences, and creating a bar chart.
MovShows = df.groupby('Year')['type'].value_counts().reset_index(name='count')
MovShows.columns = ['Year', 'Type', 'Count']

plt.figure(figsize=(15, 5))
ay = sns.barplot(x='Year', y='Count', hue='Type', data=MovShows)

# Design elements for the bar chart.
for container in ay.containers:
    ay.bar_label(container)
plt.xlabel('Year Added', color='#3274a1', weight='bold', fontsize=12)
plt.ylabel('Shows & Movies', color='#3274a1', weight='bold', fontsize=12)
plt.title('Number Of Titles Added Per Year', color='#3274a1', weight='bold', fontsize=15)
plt.xticks(ticks=range(14), labels=np.sort(np.array(MovShows['Year'].unique(), dtype=int)))
plt.grid(True, color='#3274a1', alpha=0.1)
plt.show()

# Prompting user input to filter data by a specific year and type.
Select = int(input('Enter the year that you want to see: '))
Type = input('Enter the type in lower case: ')
data = df[(df['release_year'] == Select) & (df['type'] == Type)]
data.head()

# Finding the top 5 directors based on the number of titles.
Top_directors = df['director'].value_counts().head(5).reset_index()
Top_directors.columns = ['Directors', 'Titles']
print(Top_directors)

# Finding the number of titles associated with a specific actor (e.g., Emma Roberts).
df[df['cast'] == 'Emma Roberts']

# Finding the number of titles associated with a specific actor (e.g., Robert Downey).
top = df[df['cast'].str.contains('Robert Downey', case=False, na=False)].count()
print(top)

# Prompting user input for an actor/actress name and displaying the count of titles they are associated with.
Actor = input('Enter the name of the Actor/Actress: ')
dd = df[df['cast'].str.contains(Actor, case=False, na=False)].groupby('type')
top = dd['cast'].count()
print(top)

# Prompting user input for an actor/actress name and displaying the count of titles they are associated with.
Actor = input('Enter the name of the Actor/Actress: ')
Grouped = df[df['cast'].str.contains(Actor, case=False, na=False)].groupby('type')
Tops = Grouped['cast'].count()
print(Tops)

# Displaying titles with 'TV-14' rating in Canada.
df[(df['rating'] == 'TV-14') & (df['country'] == 'Canada')]

# Finding the number of movies with 'PG-13' rating released after 2010.
aa = df[(df['rating'] == 'PG-13') & (df['release_year'] > 2008) & (df['type'] == 'movie')]
aa.groupby('type')['title'].count()

# Splitting 'duration' into 'Minutes' and 'Unit', converting 'Minutes' to an integer.
df[['Minutes', 'Unit']] = df['duration'].str.split(" ", expand=True)
df['Minutes'] = df['Minutes'].astype('int')
df['Minutes'].dtype

# Displaying the top 5 longest and shortest movies.
df[df['type'] == 'movie'][['title', 'duration', 'Minutes']].sort_values(by='Minutes', ascending=False).head(5), df[df['type'] == 'movie'][['title', 'duration', 'Minutes']].sort_values(by='Minutes', ascending=True).head()

# Displaying the top TV show with the longest and shortest duration.
df[df['type'] == 'tv show'][['title', 'duration', 'Minutes']].sort_values(by='Minutes', ascending=False).head(), df[df['type'] == 'tv show'][['title', 'duration', 'Minutes']].sort_values(by='Minutes', ascending=True).head()

# Finding the country with the highest number of TV shows.
ad = df[df['type'] == 'tv show'].groupby('country')
print(ad['country'].count().sort_values(ascending=False).head(3))

# Sorting the DataFrame by the 'Year' column in ascending order.
sort = df.sort_values('Year', ascending=True, inplace=False)
sort.head(3)

# Displaying the number of null values in the 'Year' column.
df['Year'].isnull().sum()

# Displaying rows where the 'Year' column is null and filling them with corresponding values from 'release_year'.
df[df['Year'].isnull()]
df.loc[df['Year'].isnull(), 'Year'] = df.loc[df['Year'].isnull(), 'release_year']

# Displaying the number of null values in the 'Year' column after filling.
df['Year'].isnull().sum()

In this Netflix data analysis project, I navigated through Python to uncover the intricacies of the streaming giant. The mission was clear – ensure data cleanliness, decipher
content trends, and unveil viewer preferences. Scrutinizing ratings, content types, and durations provided a holistic view. Adding an interactive feature heightened practical
exploration. Beyond numbers, this journey illuminated the evolving landscape of Netflix, offering valuable insights into audience preferences. A concise exploration but one that
speaks volumes about the power of data in decoding entertainment dynamics.

```
![screencapture-localhost-8888-notebooks-Downloads-Da-Project-Netflix-Analysis-Netflix-analysis-ipynb-2024-01-08-16_14_22](https://github.com/Rizwans-github/Netflix-Analysis/assets/141806496/a07cd298-ec87-4858-8830-69accaec52a5)
