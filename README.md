Group_1_Final_Project

Project Outline
1. Broad Questions - Can we use machine learning to predict sales trends by date and by region/zip code? - When evaluating the linear regression model, there are statistically significant spikes in price that do not align with the trend line of the model. We would like to explore the spikes and see if there is correlation between the sales spikes and historically significant events (i.e. COVID, housing bubbles, recessions, etc.)

2. Technologies & Data Used - Linear Regression: We will use a linear regression model to implement our predictive machine learning, specifically using zip code, state and date data points, with zip code data being our core data (that which we will want to analyze by). - The model will plot every zip code as an individual regression model and store the results in a dictionary that will be used later in the project for our user interface. - Zillow offers a large collection of data points, related to housing prices, by zip code, by state, and over time. We plan to compile and clean this data into a DataFrame. - Visualization: - Predictive Model: Users will be able to access a website, pick a zip code and future date. The website will output results upon clicking an analyze button. - Final Presentation: Tableau

Project Phases & Timeline
Segment #1

Roles:

Nathan - Circle
Lucybel - X
Ruslana - Triangle
Megan - Square
Segment 1 Process Within the first phase of our project, we have compiled and scrubbed data from Zillow, specifically assessing sales prices by date and by zip code within Texas. This data was then input into a linear regression model to predict sales trends and future sles prices. When creating our linear regression model, one obstacle was determining how to account for multiple zip codes, each with its own regression model. We opted to create a for loop and run each zip code through the model, then storing it into a dictionary that we will then convert into a dataframe for future phases of our project. Additionally, this week, we have created an outline for our user interface feature, which will allow the user to input a specific zip code in Texas and a future date - the program would then output a predicted sales price for that zip code and date.

Segment #2

Roles:
Nathan: X
Lucybel: Square
Ruslana: Triangle
Megan: Circle
Segment #3

Roles:
Segment #4

Roles:
