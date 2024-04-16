# PRODIGY_DS_01
This is my first task with Prodigy Infotech where I was supposed to create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population. 
DATA SET USED: https://www.canva.com/link?target=https%3A%2F%2Fdata.worldbank.org%2Findicator%2FSP.POP.TOTL&design=DAFpRxy47kU&accessRole=viewer&linkSource=document
### BASIC LAYOUT
The initial part of this project was to import necesssary libraries,check if the data is getting printed in the console with the necessary functions.Once it was executed, my next step was to select a continuous variable to sort the data.Since age and genders were not specified in data,I decided to take years as continuous variable.Once decided with it,my next step was to sort the data for most populated countries and least populated countries. In the beginning I did it separately and it worked as well but to create a better accessibility for the viewers to visualize the data for most & less populated countries in 2022 & 2020, I tried the subplot function to create a better layout.
### CHECKING THE DATA PRINTED IN CONSOLE.
![image](https://github.com/aarya-09/PRODIGY_DS_01/assets/126316004/228c5c8e-35f2-4b6b-9b2e-ce3d5fe8582c)
![image](https://github.com/aarya-09/PRODIGY_DS_01/assets/126316004/03df2916-1058-4c9b-a1e9-9dc4cf9a3dd5)

### CODE FOR IMPORTING LIBRARIES,DATA CHECKING,SORTING AND SUBPLOTS.
![print1](https://github.com/aarya-09/PRODIGY_DS_01/assets/126316004/b5980874-9c0e-4f04-9866-e664197a7a8a)
![print2](https://github.com/aarya-09/PRODIGY_DS_01/assets/126316004/2c29867e-db51-4451-80a7-675bce763479)

As seen in the code we defined colors to make a difference for visuality. Blue was chosen for 2022 whereas green for 2020. To improvise it further we used the following functions to create the different intensity of colors to indicate the different level of population:
1) plt.cm.Blues(np.linspace(0.3, 1, 20))
2) plt.cm.Greens(np.linspace(0.3, 1, 20))

Explaination of the function:plt.cm.Greens is a function provided by Matplotlib that generates a colormap representing shades of green. The np.linspace(0.3, 1, 20) part creates an array of 20 equally spaced values ranging from 0.3 to 1. These values represent the intensity of the color in the colormap. Here 0.3 to 1 is used to control intensity of color, where 0.3 is darker and 1 is the brightest.

The layout of text was also getting overlapped and was not looking pleasant on eyes as well.It was difficult to read what was written on x-axis due to over lapping. So we used this "axs[0,0].tick_params(axis='x', rotation=90)" to rotate the text and make it more visually applealing.

In the similarly way, we tried this code for 1960 and 1961 data but this time with different colors. Red was for 1960 and Orange for 1961.

### CODE FOR 1960 & 1961
![print3](https://github.com/aarya-09/PRODIGY_DS_01/assets/126316004/a4d72bd7-8dc2-49b4-bc1a-d53d4df7222f)

### THE RESULT FOR 2022 AND 2020 DATA.
![most and least populated](https://github.com/aarya-09/PRODIGY_DS_01/assets/126316004/318a9dbc-fbd1-4c7b-870d-275dfff1911a)

### THE RESULT FOR 1960 AND 1961 DATA.
![1960 1961 population](https://github.com/aarya-09/PRODIGY_DS_01/assets/126316004/737b8c24-828b-4a9e-8ab6-0f1651867eb9)

In the following code for the first half, we have used India's and Belgium's data for comparing the population differnce over a decade. For this, the decade chosen was 2012-2022.Here first we created the DataFrame for both the countries and defined population_years.The other process was same as before for defining colors.
### RESULT OF INDIA AND BELGIUM POPULATION TREND
![india Vs belgium](https://github.com/aarya-09/PRODIGY_DS_01/assets/126316004/5e8bea90-2612-4322-b4dc-c7c824f4ae7d)

For the second half, we just printed out the statement in console to get percentage of total population in each country by using country code.
### 1972 TOTAL POPULATION PERCENTAGE WISE
![image](https://github.com/aarya-09/PRODIGY_DS_01/assets/126316004/cbd352d4-2bf7-4c1d-b211-259cc123fb49)

### SOME ERRORS TO AVOID
While the code was comparatively easy there are some minor errors that made our data look visually chaotic.
1. OVERLAPPING OF X-AXIS AND THE TITLE OF SECOND GRAPH:
   To avoid that happening, we used function such as "plt.tight_layout()" which adjust the layout and make it look cleaner and more appealing to the eyes.
2. COLOUR OR COLOR:
   The most silliest yet the most common mistake to happen. In python we use 'color' and not 'colour'.
   Make sure to use the colors that are supported by python/matplotlib.There are many colors that don't exist such as pink, light green.
4. DEFINING ARRAYS:
   Make sure to use correct index to create your data. With wrong inputs there would definitely be an error.
### HELP TAKEN FROM
To overcome certain errors we used AI,Google and certain coding related websites.
### EDITORS USED
The software that I used was Spyder as I was more comfortable to work with it. However, you can use V.S.Code or Jupyter notebook as well. 


