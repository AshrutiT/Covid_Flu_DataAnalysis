tree = ("Would you like to use the cached file for the Flu data if it exists? 1 (Yes) or 0 (no): \n",
        
        "Would you like to use the cached file for the Covid-19 data if it exists? 1 (Yes) or 0 (no): \n",
        
        'The following app allows the visualization of several aspects of Flu and Covid-19\
prevalence in the United States.\n\nWould you like to see the type of analysis to expect?  1 (Yes) or 0 (no): \n',
        
        "Would you like to continue with the analysis? 1 (Yes) or 0 (no): \n",
        
        "Have a great day. App is Exiting!", 
        
       ("\n\n\033[1m Overview of the visualizations that are included in the app:" 
      "\n\n>Number of flu cases per year\n\n"
        ">Relationship between the number of tested individuals for flu and positive flu cases\n\n"
        ">Distribution of the percentage of positive flu cases\n\n"
        ">View Flu Data\n\n"
        ">Total number of covid cases per year\n\n"
        ">Change of new cases over time\n\n"
        ">Distribution of confirmed covid cases\n\n"
        ">Overview of Covid Data\n\n"
        ">Examine correlation between Covid-19 attributes\n\n"
        ">Total Number of cases per state\n\n"
     ))

try:
    overwrite1 = int(input(tree[0]))

    overwrite2 = int(input(tree[1]))

    select = int(input(tree[2]))

    if select == 0:
        run_flag = int(input(tree[3]))
        
    elif select == 1:
        print(tree[5])
        run_flag = int(input(tree[3]))
    elif select == 1:
        run_flag = int(input(tree[3]))
        
    else:
        print(tree[4])
        quit()

    def collect_data(source, overwrite = False):
        try:
            # Import libraries
            import requests
            from bs4 import BeautifulSoup
            import pandas as pd
            from urllib.request import urlopen
            source = source
            if overwrite == 1:
                #check if the file exists
                import os.path
                from os import path

                if path.exists(source+'.csv') == True:
                    #delete the collected data if the user allows overwriting
                    import os
                    print('Chose to overwrite if the data exists')
                    os.remove(source+'.csv')
                    overwrite = 1
                    if source == 'covid':
                        df = pd.read_csv('https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD')
                        #scrap flu data if the selected source if flu
                    if source == 'flu':
                        #provide web page to scrap
                        url = "https://www.cdc.gov/flu/weekly/weeklyarchives2021-2022/data/whoAllregt_cl13.html"
                        # Create object page
                        page = requests.get(url)
                        # parser-lxml = Change html to Python friendly format
                        # Obtain page's information
                        soup = BeautifulSoup(page.text, 'lxml')
                        #soup
                        # Obtain information from tag <table>
                        table1 = soup.find('table')
                        # Obtain every title of columns with tag <th>
                        headers = []
                        for i in table1.find_all('th'):
                            title = i.text
                            headers.append(title)
                        FluData = pd.DataFrame(columns = headers)
                        # Create a for loop to fill FluData
                        for j in table1.find_all('tr')[1:]:
                            row_data = j.find_all('td')
                            row = [i.text for i in row_data]
                            length = len(FluData)
                            FluData.loc[length] = row
                        df = FluData
                        '''Create an exception to check for the length of the flu data We noted in vscode, 
                        flu data is not scraped. This will use the pandas read html to scrape the data if the data is not scraped'''
                        if len(df) <= 0:
                            import pandas as pd
                            df = pd.read_html("https://www.cdc.gov/flu/weekly/weeklyarchives2021-2022/data/whoAllregt_cl13.html")
                            df = df[0]
                            df.to_csv(source+'.csv', index = False)
                        else:
                            df = FluData
                    else:
                        print('Check your source or internet connection')
                    #cache the collected file
                    df.to_csv(source+'.csv', index = False)
                else:
                    overwrite = 0
                    if source == 'covid':
                        df = pd.read_csv('https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD')
                        #scrap flu data if the selected source if flu
                    elif source == 'flu':
                        #provide web page to scrap
                        url = "https://www.cdc.gov/flu/weekly/weeklyarchives2021-2022/data/whoAllregt_cl13.html"
                        # Create object page
                        page = requests.get(url)
                        # parser-lxml = Change html to Python friendly format
                        # Obtain page's information
                        soup = BeautifulSoup(page.text, 'lxml')
                        #soup
                        # Obtain information from tag <table>
                        table1 = soup.find('table')
                        # Obtain every title of columns with tag <th>
                        headers = []
                        for i in table1.find_all('th'):
                            title = i.text
                            headers.append(title)
                        FluData = pd.DataFrame(columns = headers)
                        # Create a for loop to fill FluData
                        for j in table1.find_all('tr')[1:]:
                            row_data = j.find_all('td')
                            row = [i.text for i in row_data]
                            length = len(FluData)
                            FluData.loc[length] = row
                        df = FluData
                    else:
                        print('Check your source or internet connection')
                    #cache the collected file
                    df.to_csv(source+'.csv', index = False)
            elif overwrite == 0:
                try:
                    #check if the data was cached
                    df = pd.read_csv(source+'.csv')
                except:
                    if source == 'covid':
                        df = pd.read_csv('https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD')
                        #scrap flu data if the selected source if flu
                    elif source == 'flu':
                        #provide web page to scrap
                        url = "https://www.cdc.gov/flu/weekly/weeklyarchives2021-2022/data/whoAllregt_cl13.html"
                        #Create object page
                        page = requests.get(url)
                        #parser-lxml = Change html to Python friendly format
                        #Obtain page's information
                        soup = BeautifulSoup(page.text, 'lxml')
                        #soup
                        #Obtain information from tag <table>
                        table1 = soup.find('table')
                        #Obtain every title of columns with tag <th>
                        headers = []
                        for i in table1.find_all('th'):
                            title = i.text
                            headers.append(title)
                        FluData = pd.DataFrame(columns = headers)
                        #Create a for loop to fill FluData
                        for j in table1.find_all('tr')[1:]:
                            row_data = j.find_all('td')
                            row = [i.text for i in row_data]
                            length = len(FluData)
                            FluData.loc[length] = row
                        df = FluData
                    else:
                        '''Create an exception to check for the length of the flu data We noted in vscode, 
                        flu data is not scraped. This will use the pandas read html to scrape the data if the data is not scraped'''
                        import pandas as pd
                        df = pd.read_html("https://www.cdc.gov/flu/weekly/weeklyarchives2021-2022/data/whoAllregt_cl13.html")
                        df = df[0]
                        df.to_csv(source+'.csv', index = False)                              
                    #cache
                    df.to_csv(source+'.csv', index = False)
            return df
        except:
            print('There is an error with one of your input/internet, kindly run the program and provide correct input')
    
    from flask import Flask, render_template,request
    import plotly
    import plotly.express as px
    import plotly.graph_objs as go
    import pandas as pd
    import numpy as np
    import json


    app = Flask(__name__)
    #Collect data
    import pandas as pd
    #Collect flu data
    if overwrite1 == 1:
        df = collect_data('flu', overwrite = True)
    elif overwrite1 == 0:

        try:
            '''Collect the flu data, if it is available in the path, otherwise scrap the data'''
            df = pd.read_csv('flu.csv') 
        except:
            df = collect_data('flu', overwrite = True)
    else:
        print("Wrong choice")
        
  
        
    @app.route('/')
    def index():
        feature = 'Bar'
        bar = create_plot(feature)
        return render_template('index.html', plot=bar)

    def my_form_post():
        text = request.form['text']
        processed_text = text.upper()
        return processed_text

      #Covid-19 data
    import pandas as pd
    #Collect data
    if overwrite2 == 1:
        df_covid = collect_data('covid', overwrite = True)
    elif overwrite2 == 0:
        try:
            '''Collect the covid data, if it is available in the path, otherwise scrap the data'''
            df_covid = pd.read_csv('covid.csv')
                #select the required variables 
            df_covid = df_covid[['submission_date', 'state', 'tot_cases', 'conf_cases','prob_cases',
        'new_case', 'new_death', 'tot_death']]
        except:
            df_covid = collect_data('covid', overwrite = True)
                #select the required variables 
            df_covid = df_covid[['submission_date', 'state', 'tot_cases', 'conf_cases','prob_cases',
        'new_case', 'new_death', 'tot_death']]
    else:
        print("Wrong choice")

        
    #select the required variables 
    df_covid = df_covid[['submission_date', 'state', 'tot_cases', 'conf_cases','prob_cases',
        'new_case', 'new_death', 'tot_death']]
    #convert submission date to date variable
    df_covid['Date'] = pd.to_datetime(df_covid['submission_date'])
    df_covid = df_covid.sort_values('Date', ascending = 0)

    def create_plot(feature):
        if feature == 'Bar1':
            #Get year
            Week_str = [str(item) for item in df.Week]
            Year = [item[0:4] for item in Week_str]
            df['Year'] = Year
            data = [
                go.Bar(
                    x=df['Year'].values, # assign x as the dataframe column 'x'
                    y=df['% Positive'].values, text = "Number of positive cases"
                )
            ]
            #print(data)

        elif feature == 'Scatter1':

            # Create a trace
            data = [go.Scatter(
                x = df['Total # Tested'].values,
                y = df['% Positive'].values,
                mode = 'markers')]
        elif feature == 'Count1':

            x = df['Percent Positive B '].values
            data = [go.Histogram(x=x,
                    marker=dict(color='rgb(0, 0, 100)'))]
        elif feature == 'Data1':
            data = [go.Table(header=dict(values=['Total # Tested', '% Positive', 'Week']),
                    cells=dict(values=[df['Total # Tested'], df['% Positive'], df['Week']]))]

        elif feature == 'Correlation1':
            correl = round(pd.DataFrame(df.corr()), 2)
            data = [go.Table(header=dict(values=['Attribute','Week', 'Total A', 'Total B', 'Percent Positive A',
        'Percent Positive B', 'Total # Tested', '% Positive']),
                    cells=dict(values=[['Week', 'Total A', 'Total B', 'Percent Positive A',
        'Percent Positive B ', 'Total # Tested', '% Positive'],correl['Week'],correl[ 'Total A'],correl[ 'Total B'],
                                        correl[ 'Percent Positive A'],correl[
        'Percent Positive B '],correl[ 'Total # Tested'],correl[ '% Positive']]))]
        elif feature == 'line':
            #get the total number of cases per day
            new_cases_time = pd.DataFrame(df_covid.groupby('submission_date')['new_case'].sum()).reset_index()
            new_cases_time['submission_date'] = pd.to_datetime(new_cases_time['submission_date'])
            new_cases_time = new_cases_time.sort_values('submission_date')
            x =  new_cases_time['submission_date'].values
            y =  new_cases_time['new_case'].values
            data = [go.Scatter(x=x, y=y)]
            
            #covid data visualization
        if feature == 'Bar':
            #Get year
            day_str = [str(item) for item in df_covid.submission_date]
            Year = [item[6:10] for item in day_str]

            df_covid['Year'] = Year
            df_covid1 = pd.DataFrame(df_covid.groupby('Year')['tot_cases'].mean()).reset_index()
            data = [
                go.Bar(
                    x=df_covid1['Year'].values, # assign x as the dataframe column 'x'
                    y=df_covid1['tot_cases'].values, text = "Number of total cases"
                )
            ]
            #print(data)
        elif feature == 'Count':

            x = df_covid['conf_cases'].values
            data = [go.Histogram(x=x,
                    marker=dict(color='rgb(0, 0, 100)'))]        
        elif feature == 'Data':
            data = [go.Table(header=dict(values=['submission_date', 'state', 'tot_cases', 'conf_cases','prob_cases',
        'new_case', 'new_death', 'tot_death']),
                    cells=dict(values=[df_covid['submission_date'],df_covid['state'],df_covid['tot_cases'],
                                        df_covid['conf_cases'],df_covid['prob_cases'],df_covid[
                    'new_case'],df_covid['new_death'],df_covid['tot_death']]))]        
        elif feature == 'Correlation':
            correl = round(pd.DataFrame(df_covid.corr()), 2)
            data = [go.Table(header=dict(values=['Variables','tot_cases', 'conf_cases', 'prob_cases', 'new_case', 'new_death',
        'tot_death']),
                    cells=dict(values=[['tot_cases', 'conf_cases', 'prob_cases', 'new_case', 'new_death',
        'tot_death'],correl['tot_cases'],correl[ 'conf_cases'],correl[ 'prob_cases'],correl[ 'new_case'],
                                        correl[ 'new_death'],correl[
        'tot_death']]))]
            
        elif feature == 'state':
            cases_per_state = round(pd.DataFrame(df_covid.groupby('state')['tot_cases'].max()).reset_index())
            cases_per_state = cases_per_state.sort_values('tot_cases', ascending = False)
            data = [go.Table(header=dict(values=['State', 'Total cases']),
                    cells=dict(values=[cases_per_state['state'], cases_per_state['tot_cases']]))]  

        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON

    @app.route('/bar', methods=['GET', 'POST'])
    def change_features():
        feature = request.args['selected']
        graphJSON= create_plot(feature)
        return graphJSON
    #change data
    def change_data():
        feature = request.args['datax']
        overwrite = request.args['overwrite']
        dataa = collect_data(overwrite = False)
        return dataa
    if run_flag == 0:
        print(tree[4])
        quit()
    else:
        if __name__ == '__main__':
            app.run()
except:
    print("There was an error processing your input. Try again.")


