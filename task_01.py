#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#reading files
df=pd.read_csv(r'C:\Users\aarya\OneDrive\Desktop\DS\POPULATION DATA.csv')
print(df)
df.shape
df.info()
df.describe()
print(df.columns)
df.drop(columns=['Indicator Name'],inplace=True)
print(df.columns)
totalpopulation_df=df[df['Indicator Code']=='SP.POP.TOTL']
print(totalpopulation_df)
totalpopulation_sort = totalpopulation_df.sort_values(by='2022',ascending=False)
print(totalpopulation_sort['2022'])
top20_countries=totalpopulation_sort.head(20)
print(top20_countries)

# Sorting DataFrame by 2022 population for most populated countries
totalpopulation_sort_2022 = totalpopulation_df.sort_values(by='2022', ascending=False)
top20_countries_2022 = totalpopulation_sort_2022.head(20)

# Sorting DataFrame by 2020 population for most populated countries
totalpopulation_sort_2020 = totalpopulation_df.sort_values(by='2020', ascending=False)
top20_countries_2020 = totalpopulation_sort_2020.head(20)

# Sorting DataFrame by 2022 population for less populated countries
totalpopulation_sort_2022 = totalpopulation_df.sort_values(by='2022', ascending=True)
top20_lpcountries_2022 = totalpopulation_sort_2022.head(20)

# Sorting DataFrame by 2020 population for less populated countries
totalpopulation_sort_2020 = totalpopulation_df.sort_values(by='2020', ascending=True)
top20_lpcountries_2020 = totalpopulation_sort_2020.head(20)

# Defining colors with different shades of blue=2022 and green=2020
colors_2022 = plt.cm.Blues(np.linspace(0.3, 1, 20))
colors_2020 = plt.cm.Greens(np.linspace(0.3, 1, 20))

# Creating subplot to have a better comparison
fig, axs = plt.subplots(2, 2, figsize=(12,16))
# Plot 2022 data for top populated countries
axs[0,0].bar(top20_countries_2022['Country Name'], top20_countries_2022['2022'], color=colors_2022, edgecolor='darkblue')
axs[0,0].set_xlabel('Country')
axs[0,0].set_ylabel('Population')
axs[0,0].set_title('Top 20 Populated Countries in 2022')
axs[0,0].tick_params(axis='x', rotation=90)
axs[0,0].grid(True)
# Plot 2020 data for top populated countries
axs[0,1].bar(top20_countries_2020['Country Name'], top20_countries_2020['2020'], color=colors_2020, edgecolor='darkgreen')
axs[0,1].set_xlabel('Country')
axs[0,1].set_ylabel('Population')
axs[0,1].set_title('Top 20 Populated Countries in 2020')
axs[0,1].tick_params(axis='x', rotation=90)
axs[0,1].grid(True)
# Plot 2022 data for top less populated countries
axs[1,0].bar(top20_lpcountries_2022['Country Name'], top20_lpcountries_2022['2022'], color=colors_2022, edgecolor='darkblue')
axs[1,0].set_xlabel('Country')
axs[1,0].set_ylabel('Population')
axs[1,0].set_title('Top 20 Less Populated Countries in 2022')
axs[1,0].tick_params(axis='x', rotation=90)
axs[1,0].grid(True)
# Plot 2020 data for top less populated countries
axs[1,1].bar(top20_lpcountries_2020['Country Name'], top20_lpcountries_2020['2020'], color=colors_2020, edgecolor='darkgreen')
axs[1,1].set_xlabel('Country')
axs[1,1].set_ylabel('Population')
axs[1,1].set_title('Top 20 Less Populated Countries in 2020')
axs[1,1].tick_params(axis='x', rotation=90)
axs[1,1].grid(True)

plt.tight_layout()
plt.show()


#for 1960 & 1961
# Sorting DataFrame by 1960 & 1961 population for most populated
totalpopulation_sort_1960 = totalpopulation_df.sort_values(by='1960', ascending=False)
top20_countries_1960 = totalpopulation_sort_1960.head(20)
totalpopulation_sort_1961 = totalpopulation_df.sort_values(by='1961', ascending=False)
top20_countries_1961 = totalpopulation_sort_1961.head(20)

# Sorting DataFrame by 1960 & 1961 population for less populated
totalpopulation_sort_1960 = totalpopulation_df.sort_values(by='1960', ascending=True)
top20_lpcountries_1960 = totalpopulation_sort_1960.head(20)
totalpopulation_sort_1961 = totalpopulation_df.sort_values(by='1961', ascending=True)
top20_lpcountries_1961 = totalpopulation_sort_1961.head(20)

# Define colors with different shades of red=1960 and orange=1961
colors_1960 = plt.cm.Reds(np.linspace(0.3, 1, 20))
colors_1961 = plt.cm.Oranges(np.linspace(0.3, 1, 20))

# Creating subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 16))
# Plot 1960 data for top populated countries
axs[0,0].bar(top20_countries_1960['Country Name'], top20_countries_1960['1960'], color=colors_1960, edgecolor='darkred')
axs[0,0].set_xlabel('Country')
axs[0,0].set_ylabel('Population')
axs[0,0].set_title('Top 20 Populated Countries in 1960')
axs[0,0].tick_params(axis='x', rotation=90)
axs[0,0].grid(True)
# Plot 1961 data for top populated countries
axs[0,1].bar(top20_countries_1961['Country Name'], top20_countries_1961['1961'], color=colors_1961, edgecolor='darkorange')
axs[0,1].set_xlabel('Country')
axs[0,1].set_ylabel('Population')
axs[0,1].set_title('Top 20 Populated Countries in 1961')
axs[0,1].tick_params(axis='x', rotation=90)
axs[0,1].grid(True)
# Plot 1960 data for top less populated countries
axs[1,0].bar(top20_lpcountries_1960['Country Name'], top20_lpcountries_1960['1960'], color=colors_1960, edgecolor='darkred')
axs[1,0].set_xlabel('Country')
axs[1,0].set_ylabel('Population')
axs[1,0].set_title('Top 20 Less Populated Countries in 1960')
axs[1,0].tick_params(axis='x', rotation=90)
axs[1,0].grid(True)
# Plot 1961 data for top less populated countries
axs[1,1].bar(top20_lpcountries_1961['Country Name'], top20_lpcountries_1961['1961'], color=colors_1961, edgecolor='darkorange')
axs[1,1].set_xlabel('Country')
axs[1,1].set_ylabel('Population')
axs[1,1].set_title('Top 20 Less Populated Countries in 1961')
axs[1,1].tick_params(axis='x', rotation=90)
axs[1,1].grid(True)

plt.tight_layout()
plt.show()


# The DataFrame for India
india_population_df = totalpopulation_df[totalpopulation_df['Country Name'] == 'India']
# Taking population data of India from 2012 to 2022
population_years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
india_population = india_population_df[population_years].values.flatten()
# The DataFrame for Belgium
belgium_population_df = totalpopulation_df[totalpopulation_df['Country Name'] == 'Belgium']
# Taking population data of Belgium from 2012 to 2022
belgium_population = belgium_population_df[population_years].values.flatten()

# Creating subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 16))

# Plot India's population data from 2012 to 2022
axs[0].bar(population_years, india_population, color='lightgreen', edgecolor='darkgreen')
axs[0].set_title("Population Trend: India (2012-2022)")
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Population')
axs[0].grid(True)
axs[0].tick_params(axis='x', rotation=45)

# Plot Belgium's population data from 2012 to 2022
axs[1].bar(population_years, belgium_population, color='lightcoral', edgecolor='darkred')
axs[1].set_title("Population Trend: Belgium (2012-2022)")
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Population')
axs[1].grid(True)
axs[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()


# The DataFrame for the year 1972
population_1972 = totalpopulation_df[['Country Code', '1972']]
# The total population in 1972
total_population_1972 = population_1972['1972'].sum()
#The percentage of total population for each country code
population_1972['Percentage_of_Total'] = (population_1972['1972'] / total_population_1972) * 100

# Displaying the result
print(population_1972)

