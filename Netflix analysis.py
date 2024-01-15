import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("netflix_titles.csv")

df.head(2)

df.shape

df.describe(include = 'object')

df.info()

df.isnull().sum()

df[df['duration'].isnull()]


df.loc[df['duration'].isnull(), 'duration'] = df.loc[df['duration'].isnull(), 'rating']


df['rating'].unique()



df['rating']



df['rating'].shape


df.shape

df['rating'].unique()


df.loc[(df['rating'] == '74 min') | (df['rating'] == '66 min') | (df['rating'] == '84 min'), 'rating'] = np.nan


df.shape


df['rating'].unique()

df.dtypes

df['release_year'].unique()

df['Date_N'] = pd.to_datetime(df['release_year'], format = '%Y')


df['Date_N'].dt.year.value_counts()


df['Date_N'].unique()


df['date_added'] = df['date_added'].str.strip() 


df['Date_Added'] = pd.to_datetime(df['date_added'], format = '%B %d, %Y')


df['Date_Added'].unique()


df['type'].count()

MovShows = df.groupby('Date_Added')['type'].value_counts().reset_index()
print(MovShows)


plt.figure(figsize = (8,5))
yr_added = df['Date_Added'].dt.year.value_counts()
ax = sns.barplot( x = yr_added.index, y = yr_added.values, hue = yr_added.values, legend = False)
for container in ax.containers:
    ax.bar_label(container, color = '#8f6083')
plt.xlabel('Year Added', color = '#8f6083', weight = 'bold', fontsize = 12)
plt.ylabel('Shows & Movies', color = '#8f6083', weight = 'bold', fontsize = 12)
plt.title('Number Of Titles Added Per Year', color = '#8f6083', weight = 'bold', fontsize = 15)
plt.xticks( ticks = range(14), labels = np.sort(np.array(yr_added.index, dtype = int)))
plt.grid(True, color = '#573c5f', alpha = 0.1)
plt.show()


plt.figure(figsize =(10,5))
yr = df['Date_Added'].dt.year.value_counts().reset_index()
ad = sns.barplot(x = yr['Date_Added'] , y = yr['count'], hue = yr['count'])
for container in ad.containers:
    ad.bar_label(container, color = '#8f6083')

plt.show()


ax = sns.countplot(x = df['type'], hue =  df['type'])
for container in ax.containers:
    ax.bar_label(container, label_type = 'center', color = 'white' , size = 14, weight = 'bold')
plt.ylabel('No. of Titles',color = '#3274a1', weight = 'bold', fontsize = 12 )
plt.xlabel('Type', color = '#3274a1', weight = 'bold', fontsize = 12)
plt.xticks(color = '#3274a1', weight = 'bold', fontsize = 10)

plt.show()

ax = sns.countplot(x = df['type'], hue = df['type'])
for container in ax.containers:
    ax.bar_label(container, label_type = 'center', color = 'white' , size = 14, weight = 'bold')
    
plt.figure(figsize= (12,4))
ay = sns.countplot(x = df['Date_Added'].dt.year, hue = df['type'], width = 0.9)
for container in ay.containers:
    ay.bar_label(container)
plt.xticks(ticks = range(14), labels = np.sort(np.array(yr_added.index, dtype = int)))

plt.show()


df['Date_Added'] = pd.to_datetime(df['Date_Added'])
df['Year'] = df['Date_Added'].dt.year

MovShows = df.groupby('Year')['type'].value_counts().reset_index(name='count')
MovShows.columns = ['Year','Type', 'Count']

    
plt.figure(figsize=(15,5))
ay = sns.barplot(x='Year', y='Count', hue='Type', data=MovShows)


# Design elements:
for container in ay.containers:
    ay.bar_label(container)
plt.xlabel('Year Added', color = '#3274a1', weight = 'bold', fontsize = 12)
plt.ylabel('Shows & Movies', color = '#3274a1', weight = 'bold', fontsize = 12)
plt.title('Number Of Titles Added Per Year', color = '#3274a1', weight = 'bold', fontsize = 15)
plt.xticks( ticks = range(14), labels = np.sort(np.array(MovShows['Year'].unique(), dtype = int)))
plt.grid(True, color='#3274a1', alpha = 0.1)


plt.show()



### Movies released in 2020

df['type'] = df['type'].str.lower()


Select = int(input('Enter the year that you want to see: '))
Type = input('Enter the type in lower case: ')
data = df[(df['release_year'] == Select) & (df['type'] == Type)]
data.head()


Top_directors = df['director'].value_counts().head(5).reset_index()
Top_directors.columns = ['Directors', 'Titles']
print(Top_directors)



### No. of titles done by a particular actor


df[df['cast'] == 'Emma Roberts']

top = df[df['cast'].str.contains('Robert Downey', case = False, na = False)].count()
print(top)

Actor = input('Enter the name of the Actor/Actress: ')
dd = df[df['cast'].str.contains(Actor, case = False, na = False)].groupby('type')
top = dd['cast'].count()
print(top)


Actor = input('Enter the name of the Actor/Actress: ')
Grouped = df[df['cast'].str.contains(Actor, case=False, na = False)].groupby('type')
Tops = Grouped['cast'].count()
print(Tops)


df['rating'].unique(), df['rating'].nunique()


#### Tv 14 rating in canada


df[(df['rating'] == 'TV-14') & (df['country'] == 'Canada')]

#### How many movies got the PG-13 rating after 2010

aa = df[(df['rating'] == 'PG-13') & (df['release_year'] > 2008) & (df['type'] == 'movie')]
aa.groupby('type')['title'].count()


df[['Minutes', 'Unit']] = df['duration'].str.split(" ", expand = True)


df ['Minutes'] = df['Minutes'].astype('int')


df['Minutes'].dtype


df.index.nlevels


df[df['type'] == 'movie'][['title','duration', 'Minutes']].sort_values(by = 'Minutes', ascending = False).head(5), df[df['type'] == 'movie'][['title','duration', 'Minutes']].sort_values(by = 'Minutes', ascending = True).head()


df[df['type'] == 'tv show'][['title','duration', 'Minutes']].sort_values(by = 'Minutes', ascending = False).head(), df[df['type'] == 'tv show'][['title','duration', 'Minutes']].sort_values(by = 'Minutes', ascending = True).head()


#### Which country has the highest no. of Tv Shows?

ad = df[df['type'] == 'tv show'].groupby('country')
print(ad['country'].count().sort_values(ascending = False).head(3))


#### Sort data by Year


sort = df.sort_values('Year', ascending = True, inplace = False)
sort.head(3)


df['Year'].isnull().sum()



df[df['Year'].isnull()]
df.loc[df['Year'].isnull(), 'Year'] = df.loc[df['Year'].isnull(), 'release_year']


df['Year'].isnull().sum()

