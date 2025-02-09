# Covid_and_Flu_Data-
CDC data on COVID &amp; Flu cases, vaccinations and mortality - Analysis

#### Preparation of the execution environment

The data scraping and visualization app can be run following the steps specified below.

**** Only if needed ****
- Create a virtual environment in a folder of your choosing using: sudo python3 -m pip install virtualenv, or follow the link: https://phoenixnap.com/kb/install-flask

- Navigate to your folder and activate your virtual environment

::Activate the virtual environment using the following command or take help from this link: https://phoenixnap.com/kb/install-flask
cd flask
cd <folder name>
activate

- Copy the app.py file and the templates and static folders to the working directory

**** Install the required packages ****

- Install the required packages in the scripts directory

pip install flask

pip install pandas

pip install plotly

pip install lxml

- Open a terminal in VSCode and execute the following command

flask run

- Supply the required input

#### Interaction

> The interaction component involves making decisions regarding (a) To use cached or collect new files for both flu and covid-19, (b) whether to view the type of visualizations to expect before hand, (c) whether to continue or quit the analysis

When executing the program, you will be prompted to supply some input including a choice of using the cached files
or generating new files. Using cached files will prompt the app to use previously downloaded files but overwriting
will generate new files that are updated if the period between the last and current execution exceeds 24 hours

You will also be prompted as to whether you would like to see the kind of visualizations to expect. Depending on your answer,
you will be prompted as to whether to continue with the analysis after which you will see a link to the app. 


#### Disclaimer
- The files are cached from the website into your local directory (you can remove the previous covid.csv files or flu.csv files if you want to run the code afresh).

- When opting to overwrite, the app scraps the data afresh deleting any existing data. 
- Overwrite option is given incase a user decides not to use the cached file.
