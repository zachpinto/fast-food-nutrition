Fast Food caloric content 
==============================

Demo: https://notebooks.gesis.org/binder/jupyter/user/zachpinto-fast-food-nutrition-hc86o2h7/doc/tree/notebooks/02_report.ipynb

## Introduction
This repo presents a very simple data analysis of caloric information of several fast food restaurants located in the Unites States. I was curious to see how various chains compared in terms of caloric distribution of their main items. 

The entire process encompasses data scraping, data cleaning, augmentation using the OpenAI API, and exploratory data analysis to provide a simple box and whisker plot to show the caloric distribution of main items across these fast food restaurants.

## Data 
The data was scraped from **fastfoodnutrition.org**, a website that collects nutritional data from dozens of popular fast food restaurants in the US.
First, I used **BeautifulSoup4** to parse the HTML to extract the URLs of all individual restaurants on the main page.

Next, I used the URLs to scrape the nutritional information for each restaurant.
I extracted the name of the restaurant, the name of every item that restaurant currently offers along with its calorie count.
I then saved the data to a CSV file for further use later.

Before any further work, I decided to create a copy of the original dataset to avoid any potential data loss.

## Augmentation
I used the **OpenAI API** to classify the menu items into categories based on their names and calorie content.

**Model Used:** GPT-3.5-turbo-0125 and GPT-3.5-turbo
**Task:** Classifying menu items based on their names and calorie content, and appending the classification to the original dataset.
Output: Each item was labeled with one of the predetermined categories to facilitate further analysis.

Eventually, I realized that another model, GPT-3.5-turbo-0125, was much faster than the recently released GPT-3.5-turbo-0125. Therefore, I switched to the earlier model to classify the menu items, and resumed from the row where I left off

Finally, I merged the classifications csv output with the original dataset to create a new dataset with the classifications appended.


## Data Cleaning

The output dataset was cleaned to ensure consistent formatting and to remove any unnecessary characters.

### Cleaning Steps:

1. **Whitespace Trimming:** Removed leading and trailing spaces from all textual data.
2. **HTML Entity Conversion:** Translated HTML entities to their corresponding characters for readability.
3. **Calorie Data Normalization:** Standardized calorie values to integer format, eliminating unnecessary decimal points.
4. **Capitalization:** Uniformed restaurant names to uppercase for consistency.

See /notebooks/00_data_cleaning.ipynb for the full data cleaning process.

## EDA

The EDA focused on understanding the calorie distribution of main dishes across different restaurants.

I wanted to do this for each classification, just to get a general basic idea of the spread of calories for each type of food.

As a proof of concept, this was completed first using **seaborn** and **matplotlib** to visualize the data.

Then, finally, I used seaborn to make a more visually appealing boxplot.



### Key Visualization:

- **Boxplot:** A box and whisker plot displaying the calorie distribution for each classification at each restaurant, ordered by median calorie content. Outliers beyond 3 standard deviations were excluded to focus on the typical menu offerings.

see /notebooks/01_eda.ipynb for the full EDA process.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   │
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

--------

