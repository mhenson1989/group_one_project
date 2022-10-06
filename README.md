# Group_1_Final_Project

## **Project Outline**

**1. Broad Questions**
    - *Can we use machine learning to predict sales trends by date and by region/zip code?*
    - *When evaluating the linear regression model, there are statistically significant spikes in price that do not align with the trend line of the model. We would like to explore the spikes and see if there is correlation between the sales spikes and historically significant events (i.e. COVID, housing bubbles, recessions, etc.)*

**2. Technologies & Data Used** 
    - Linear Regression: We will use a linear regression model to implement our predictive machine learning, specifically using zip code, state and date data points, with zip code data being our core data (that which we will want to analyze by). 
        - The model will plot every zip code as an individual regression model and store the results in a dictionary that will be used later in the project for our user interface. 
    - Zillow offers a large collection of data points, related to housing prices, by zip code, by state, and over time. We plan to compile and clean this data into a DataFrame. 
    - Database: PGAdmin and AWS
    - Visualization: 
        - Predictive Model: Users will be able to access a website, pick a zip code and future date. The website will output results upon clicking an analyze button. 
        - User Interactive Website: HTML and Javascript
        - Final Presentation: Tableau - utilizing the Story mode
  

## **Project Phases & Timeline**
Segment #1
1. **Roles:** 
    - Nathan - Circle
    - Lucybel - X 
    - Ruslana - Triangle
    - Megan - Square

    **Segment 1 Process & Progress**
    Within the first phase of our project, we have compiled and scrubbed data from Zillow, specifically assessing sales prices by date and by zip code within Texas. This data was then input into a linear regression model to predict sales trends and future sles prices. When creating our linear regression model, one obstacle was determining how to account for multiple zip codes, each with its own regression model. We opted to create a for loop and run each zip code through the model, then storing it into a dictionary that we will then convert into a dataframe for future phases of our project. Additionally, this week, we have created an outline for our user interface feature, which will allow the user to input a specific zip code in Texas and a future date - the program would then output a predicted sales price for that zip code and date. 


Segment #2
1. **Roles:**
    - Nathan: X
    - Lucybel: Square
    - Ruslana: Triangle
    - Megan: Circle 

    **Segment 2 Process & Progress**
    In Week 2 of our project, we have finalized our linear regression model and saved the results (specifically the slope and intercepts by zip code) into a DataFrame and exported that to a CSV file, which we will use within our HTML code and website. Additionally, we have created our database using AWS and PGAdmin - we will use this database to connect to our website, where our slope_intercept.csv file is stored. We also began work on our visualizations for our final presentation. We opted to use Tableau for our visualizations, however, when we imported our clean_data.csv data set into Tableau, we found that the format of the data did not align with our visualizations, as the clean data set was more geared towards a linear regression model, rather than mapped visualizations. To overcome this obstacle, we decided to create an additional dataframe and CSV, which transposed the columns and rows of our data - this allowed us to use the data more effectively with maps. Currently, we have about 95% of our visualizations complete and are working on incorporating them into a Tableau story form for our final presentation. We also began our framework for our HTML code that will build our website. We plan to work more extensively on this in week 3. 

Segment #3
1. Roles: 
    - Nathan: Circle
    - Lucybel: Square
    - Ruslana: X
    - Megan: Triangle

       **Segment 3 Process & Progress**

Segment #4
1. Roles: 


## **Project Dashboard & Presentation Outline**

**Website**


**Tableau Storyboard & Presentation**


