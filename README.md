# Multinational Retail Data Centralisation

## _Milestone 2: Extract and clean the data from the data sources_

### Task 1: Set up a new database to store the data

- Objective: Initialize a new local database called sales_data using pgAdmin4.
- Skills Learned: Database initialization, use of pgAdmin4, basic SQL commands for creating databases.

### Task 2: Initialise the three project classes
- Objective: Create scripts and classes for data extraction and cleaning. 
The classes will be structured to handle data from different sources. 
- Skills Learned: Object-oriented programming in Python, designing software for modularity and reusability.

### Task 3: Extract and clean the user data
- Objective: Develop methods to extract and clean user data from an AWS database.
- Skills Learned: Working with cloud databases(AWS), data extraction techniques, data cleaning and peprocessing


### Task 4: Extracting users and cleaning card details

- Objective: Extract users' card details from a PDF in an AWS S3 bucket and clean the data.
- Skills Learned: Interacting with AWS S3, working with PDF data, data privacy considerations.


### Task 5: Extract and clean the details of each store

- Objective: Retrieve store data using an API and clean the data.
- Skills Learned: API usage, GET requests, data cleaning from JSN or XML

### Task 6: Extract and clean the product details

- Objective: Extract product details stored in a CSV format in an S3 bucket and clean the data.
- Skills Learned: CSV file handling, AWS S3 interactions, data preprocessing.

### Task 7: Retrieve and clean the orders table

- Objective: Extract and clean data from the orders table stored in an AWS RDS database.
- Skills Learned: Advanced database operations, working with AWS RDS, SQL queries for data cleaning.

### Task 8: Retrieve and clean the data events data
- Objective: Extract and clean data from a JSON file containing sales event details and upload it to the 'sales_data' database under the table 'dim_date_times'.

- Skills Learned: JSON data handling, data transformation, ETL (Extract, Transform, Load) processes.

###  Aim of the Project

The aim of this project is to develop a robust system for extracting, cleaning and storing data from various sources. This system will enable efficient data analysis and reporting, aiding in better decision-making processes.

###  What I learned

- Comprehensive Data Handling: How to manage and process data from diverse sources like databases, APIs, CSV, PDFs, and JSON files

- Cloud Services Interaction: Skills in using AWS services, including database managment and file storage.

- Porgramming and Database Skills: Advanced Python programming, SQL and database management.

- ETL Processes: Understanding and iimplementing ETL processes for data integration.

- Data Cleaning and Preprocessing: Techniques for cleaning and preparing data for analysis.

- Problem-Solving: Developing solutions for complex data handling tasks

## Milestone 3: Create the database schema

### Task 1: Cast the columns of the orders_table to the correct data types
### Task 2: Cast the columns of the dim_users_table to the correct data types
### Task 3: Update the dim_store table
### Task 4: Make changes to the dim_products table for the delivery team
### Task 5: Update the dim_products table with the required data types
###  Task 6: Update the dim_date_times table
### Task 7: Updating the dim_card_details table
### Task 8: Create the primary keys in the dimension tables

## Milestone 4: Querying the data

### Task 1: How many stores does the business have and in which conuntries?
### Task 2: Which locations currently have the most stores?
### Task 3: Which months produced the largest amount of sales?
### Task 4: How many sales are coming from online?
### Task 5: What percentage of sales come through each type of store?
### Task 6: Which hmonth in each year produced the highest cost of sales?
### Task 7: What is our staff headcount?
### Task 8: Which German store type is selling the most?
### Task 9: How quickly is the company making sales?

## License
This project is licensed under the MIT License
[MIT](https://choosealicense.com/licenses/mit/)
