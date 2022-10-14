# Group_1_Final_Project

## **Overall Project Outline**

The purpose of our project is to use machine learning, specifically a linear regression model, in order to predict future housing prices by zip code and by date within major Texas Zip Codes. 

**1. Broad Questions**
    -
    - *Can we use machine learning to predict sales trends by date and by region/zip code?*
    - *When evaluating the linear regression model, there are statistically significant spikes in price that do not align with the trend line of the model. We would like to explore the spikes and see if there is correlation between the sales spikes and historically significant events (i.e. COVID, housing bubbles, recessions, etc.)*

**2. Technologies & Data Used** 
    -
    - Linear Regression: We will use a linear regression model to implement our predictive machine learning, specifically using zip code, state and date data points, with zip code data being our core data (that which we will want to analyze by). 
        - The model will plot every zip code as an individual regression model and store the results in a dictionary that will be used later in the project for our user interface. 
        - Libraries Used: MatPlotLib, SkLearn, NumPy, Pandas, Jupyter Notebook and DateTime

    - Zillow offers a large collection of data points, related to housing prices, by zip code, by state, and over time. We compiled and cleaned this data into a DataFrame. 

    - Database: PGAdmin and AWS

    - Dataframes Created Using Jupyter Notebook:

        - df (DataFrame directly read from original data CSV file: data_unclean.csv)
            - This data was sourced from Zillow
        - df1 (Dataframe that was transposed and cleaned from df)
            - This data was saved as clean_data.csv
        - clean_data (Dataframe read in clean_data.csv used for Linear Regression Model)
            - We created the slope_intercept.csv after running the clean_data Dataframe through the Linear Regression Model
        - data_tableau (Dataframe that was transposed for visualizations within Tableau) 
            - We created the tableau_clean.csv to upload into Tableau
            - We created the tableau_clean.csv so that we could transpose the columns and rows, for specifically mapping visualizations that were not easily read using the clean_data.csv file 

    - Visualization: 

        - Predictive Model: Users will be able to access a website, pick a zip code and future date. The website will output results upon clicking an analyze button. 
        - User Interactive Website: HTML, Flask Server, SQL_Alchemy, XMLHTTP, Python, Javascript, PGAdmin and AWS
        - Final Presentation: Tableau - utilizing the Story mode for our final presenation, however utilized sheets and dashboards to create charts and visualizations. Additionally, we used MatPlotLib for visualizations.
  

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
    In Week 2 of our project, we have finalized our linear regression model and saved the results (specifically the slope and intercepts by zip code) into a DataFrame and exported that to a CSV file, which we will use within our HTML code and website. Additionally, we have created our database using AWS and PGAdmin - we will use this database to connect to our website, where our slope_intercept.csv file is stored. This will be integrated into our HTML code in week 3. We also began work on our visualizations for our final presentation. We opted to use Tableau for our visualizations, however, when we imported our clean_data.csv data set into Tableau, we found that the format of the data did not align with our visualizations, as the clean data set was more geared towards a linear regression model, rather than mapped visualizations. To overcome this obstacle, we decided to create an additional dataframe and CSV, which transposed the columns and rows of our data - this allowed us to use the data more effectively with maps. Currently, we have about 95% of our visualizations complete and are working on incorporating them into a Tableau story form for our final presentation. We also began our framework for our HTML code that will build our website. We plan to work more extensively on this in week 3. 

    **AWS --> pgAdmin**
    Utilizing AWS’s relational database (the largest cloud provider in the market today), we set up and connected a Postgres database. 

    PostgreSQL, usually referred to as “Postgres,” is an object-relational database system that uses the SQL language.  

    •	Created a PostgreSQL Database in relational database (RDS) in AWS

    •	Created S3 bucket and stored data on AWS Simple Storage Service (Amazon S3)

    •	Connected an RDS to pgAdmin

		1.	Registered server using the endpoint connectivity link from AWS
		2.	Created table in pgAdmin 
![image_1](Resources/image_1.png).
		3.	Imported data into the table
		4.	Read table 
![image_2](Resources/image_2.png).
![image_3](Resources/image_3.png).

Segment #3
1. Roles: 
    - Nathan: Circle
    - Lucybel: Square
    - Ruslana: X
    - Megan: Triangle

       **Segment 3 Process & Progress**
       Requirements and Branch Merges: We are in the process of finalizing our HTML code and therefore still have open branches going into Segment 4. We will fully finalize and merge in our last submission. 
       Storyboard and Final Presentation: We are currently fine tuning our final presentation and will be using Tableau Story in lieu of Google Slides to present our final story. Currently, we have 90% of our story completed and placeholders where additional data is needed to complete. Within our story, we outline much of our analysis process, as well as justification for project direction, website and final visualizations. 
       The final link for our Tableau Story can be found here: https://public.tableau.com/app/profile/megan.henson/viz/Group_One_Final_Project/GroupOneFinalProject?publish=yes
       Testing: We are actively testing and finalizing code. In addition to testing code seperately, we have been allotting class time and additional project work time on Saturday's and Sunday's to run and test code. 

Segment #4
1. Roles: 
    - Nathan: Circle
    - Lucybel: Square
    - Ruslana: Triangle
    - Megan: X

       **Segment 4 Process & Progress**


## **Project Dashboard & Presentation Outline**

**Website Outline**
- Clean styling with banner and title
- Two entry fields - one for date and one for zip code
    - Zip Code entry field will be a drop down pick list
    - Date entry field will be a drop down calendar where a date will be selected
- "Show Results" button
    - When button is clicked, it will clear the entry fields
    - Results will show Zip Code and Date with future projected price
- Backend: 
    - Read in file slope/intercept file from AWS
    - Calculates future value using Y = MX + B (Linear Regression Model)

**Tableau Storyboard & Presentation**
1. Slide 1: Intro/Big Picture Questions
2. Slide 2:Cleaning the Data - Scraping, Review and Early Analysis
3. Slide 3:Machine Learning - Linear Regression Model
    - Slide 4: How we decided on our model
    - Slide 5: Process of building model and saving data
4. Slide 6: Building and Integrating the Database
5. Slide 7: Website - User Interface (link website)
6. Slide 8 thru 11: Analysis & Tableau Visualizations
7. Slide 12: Closing and Q&A



