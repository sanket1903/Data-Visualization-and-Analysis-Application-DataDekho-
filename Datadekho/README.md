##Datadekho (DATA VISUALIZATION APPLICATION):-

With the technology advancements, the organisation today has the pre-eminence of taking data driven decisions and strategize their planning, forecasts based on the same. A profusion of business users do not have time to analyze the data and then secure noteworthy insights. And there are gaps betwixt how the tool produces an output and how the business user can exploit it to interpret it. In accompaniment, it needs a admirable domain knowledge to build business insights from data. Not every user is a business expert. Given a snapshot of data, we would like to fabricate a system which can verbalise a story from the data. The story includes the automation in the sense of being driven by the data, context and personal preferences. In this case, it solves both the problems of the tool usage as well as guiding the user with the data driven intelligence to make business decision. The whole corollary is driven by outcome and effectiveness.

## Tool Description:-

Data Storyteller is an AI based tool that can take a data set, identify patterns in the data, can interpret the result, and can then produce an output story that is understandable to a business user based on the context. It is able to pro-actively analyse data on behalf of users and generate smart feeds using natural language generation techniques which can then be consumed easily by business users with very less efforts. The application has been built keeping in mind a rather elementary user and is hence, easily usable and understandable. This also uses a **multipage implementation** of Streamlit Library using Class based pages. 

## Features:- 

Given data/analytics output, the tool can:-

- turn the data into interactive data stories based on the given data 
- generate deep insights, infer pattern and help in business decisions.
- provide personalization profiles; these could be represented as meta data describing what would be of interest to a given user.
- generate reports understandable to a business user with interactive and intuitive interface.

## 📝 Module-Wise Description




_📌 **Data Upload**_ <br/>

This module deals with the data upload. It can take csv and excel files. As soon as the data is uploaded, it creates a copy of the data to ensure that we don't have to read the data multiple times. It also saves the columns and their data types along with displaying them for the user. This is used to upload and save the data and it's column types which will be further needed at a later stage. 

_📌 **Change Metadata**_ <br/>

Once the column types are saved in the metadata, we need to give the user the option to change the type. This is to ensure that the automatic column tagging can be overridden if the user wishes. For example a binary column with 0 and 1s can be tagged as numerical and the user might have to correct it. The three data types available are:

* Numerical 
* Categorical 
* Object

The correction happens immediately and is saved at that moment. 

_📌 **Machine Learning**_ <br/>

This section automates the process of machine learning by giving the user the option to select X and y variables and letting us do everything else. The user can specify which columns they need for machine learning and then select the type of process - regression and classficiation. The application selects multiple models and saves the best one as a binary `.sav` file to be used in the future for inferencing. The accuracy or R2 score is shown right then and there with the model running in the background.  

## Technology Stack 

1. Python 
2. Streamlit 
3. Pandas
4. Scikit-Learn
5. Seaborn

# How to Run 

- Clone the repository
- Setup Virtual environment
```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
- Run Streamlit
```
$ streamlit run app.py
```


