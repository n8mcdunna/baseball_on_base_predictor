from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd

from app import app

loan_purposes = ['Business',
                 'Car financing',
                 'Credit card refinancing',
                 'Debt consolidation',
                 'Green loan',
                 'Home buying',
                 'Home improvement',
                 'Major purchase',
                 'Medical expenses',
                 'Moving and relocation',
                 'Other',
                 'Vacation']
batters = ['Manny Machado', 'Paul Goldschmidt', 'Nick Markakis',
       'Charlie Blackmon', 'Brian Dozier', 'Anthony Rizzo', 'Mookie Betts',
       'Carlos Santana', 'Joey Votto', 'Nolan Arenado', 'Andrew McCutchen',
       'Eric Hosmer', 'Jose Altuve', 'Kyle Seager', 'Xander Bogaerts',
       'Jose Abreu', 'Brett Gardner', 'Edwin Encarnacion', 'Kole Calhoun',
       'Nelson Cruz', 'Francisco Lindor', 'Christian Yelich', 'Freddy Galvis',
       'Evan Longoria', 'Matt Carpenter', 'Ian Kinsler', 'Ender Inciarte',
       'DJ LeMahieu', 'Justin Upton', 'Adam Jones', 'Jean Segura',
       'Mike Trout', 'Kris Bryant', 'Alcides Escobar', 'Bryce Harper',
       'George Springer', 'Albert Pujols', 'Marcell Ozuna', 'Freddie Freeman',
       'Robinson Cano', 'Chris Davis', 'Todd Frazier', 'Nicholas Castellanos',
       'Joe Mauer', 'Kevin Pillar', 'Odubel Herrera', 'Cesar Hernandez',
       'Khris Davis', 'Kendrys Morales', 'Brandon Crawford', 'Elvis Andrus',
       'Lorenzo Cain', 'J.D. Martinez', 'Marcus Semien', 'Andrelton Simmons',
       'Jose Ramirez', 'Starlin Castro', 'Ian Desmond', 'Didi Gregorius',
       'Jason Kipnis', 'Rougned Odor', 'Matt Kemp', 'Carlos Gonzalez',
       'Dee Gordon', 'Jose Bautista', 'Eugenio Suarez', 'Melky Cabrera',
       'Asdrubal Cabrera', 'Curtis Granderson', 'Buster Posey', 'Jay Bruce',
       'Anthony Rendon', 'Mark Trumbo', 'Gregory Polanco', 'Giancarlo Stanton',
       'Ben Zobrist', 'Jason Heyward', 'Shin-Soo Choo', 'Yadier Molina',
       'Salvador Perez', 'Jonathan Schoop', 'Brandon Belt', 'J.T. Realmuto',
       'Adrian Beltre', 'Josh Donaldson', 'Starling Marte', 'Billy Hamilton',
       'Scooter Gennett', 'Dexter Fowler', 'Maikel Franco', 'Daniel Murphy',
       'Mitch Moreland', 'Josh Reddick', 'Alex Gordon', 'Logan Forsythe',
       'Carlos Correa', 'Victor Martinez', 'Yangervis Solarte',
       'Yonder Alonso', 'Justin Turner']
pitchers = ['Justin Verlander', 'Chris Archer', 'Kyle Gibson', 'Rick Porcello',
       'Jose Quintana', 'Corey Kluber', 'Cole Hamels', 'Max Scherzer',
       'Zack Greinke', 'Mike Leake', 'James Shields', 'Mike Fiers',
       'Dallas Keuchel', 'Jake Odorizzi', 'Chris Sale', 'Gerrit Cole',
       'Marco Estrada', 'Gio Gonzalez', 'Masahiro Tanaka', 'Julio Teheran',
       'Tanner Roark', 'Trevor Bauer', 'Carlos Carrasco', 'David Price',
       'Jacob deGrom', 'Carlos Martinez', 'CC Sabathia', 'J.A. Happ',
       'Kevin Gausman', 'Andrew Cashner', 'Ian Kennedy', 'Bartolo Colon',
       'Jon Lester', 'Sonny Gray', 'Felix Hernandez', 'Jason Hammel',
       'Wade Miley', 'Jake Arrieta', 'Kyle Hendricks', 'Jeff Samardzija',
       'Danny Duffy', 'Ervin Santana', 'Hector Santiago', 'Martin Perez',
       'Ivan Nova', 'Patrick Corbin', 'Anibal Sanchez', 'Clayton Kershaw',
       'Johnny Cueto', 'Jeremy Hellickson', 'Yovani Gallardo',
       'Chase Anderson', 'Jordan Zimmermann', 'Stephen Strasburg',
       'Eduardo Rodriguez', 'Robbie Ray', 'Michael Wacha', 'Mike Foltynewicz',
       'Francisco Liriano', 'John Lackey', 'R.A. Dickey', 'Collin McHugh',
       'Carlos Rodon', 'Jimmy Nelson', 'Marcus Stroman', 'Luis Severino',
       'Madison Bumgarner', 'Noah Syndergaard', 'Lance McCullers',
       'Derek Holland', 'Kendall Graveman', 'Drew Pomeranz', 'Doug Fister',
       'Lance Lynn', 'Chris Tillman', 'Taijuan Walker', 'Alex Wood',
       'Matt Harvey', 'Matt Moore', 'Mike Pelfrey', 'Jhoulys Chacin',
       'Jaime Garcia', 'Miguel Gonzalez', 'Aaron Nola', 'Sean Manaea',
       'Josh Tomlin', 'Ubaldo Jimenez', 'James Paxton', 'Michael Pineda',
       'Edinson Volquez', 'Ricky Nolasco', 'Matthew Boyd', 'Charlie Morton',
       'Aaron Sanchez', 'Danny Salazar', 'Jesse Chavez', 'Dan Straily',
       'Erasmo Ramirez', 'Michael Fulmer', 'Clayton Richard']

wind_directions = ['R to L', 'L to R', 'None', 'Out to CF', 'Out to RF', 'Out to LF',
       'In from RF', 'In from LF', 'In from CF', 'Varies', 'Calm']

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ## Create an at bat scenario!
    """), 
    html.Div([
        dcc.Markdown('###### Inning'), 
        dcc.Slider(
            id='inning', 
            min=1, 
            max=19, 
            step=1, 
            value=5, 
            marks={n: str(n) for n in range(0,20,2)}
        ),  
    ], style=style),

    html.Div([
        dcc.Markdown('###### Wind Speed'), 
        dcc.Slider(
            id='wind_speed', 
            min=0,
            max=30,
            step=5,
            value=10, 
            marks={n: str(n) for n in range(0,31,5)} 
        ), 
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Batter'), 
        dcc.Dropdown(
            id='batter', 
            options=[{'label': batter, 'value': batter} for batter in batters], 
            value=batters[0]
        ), 
    ], style=style),
    
    html.Div([
        dcc.Markdown('###### Pitcher'), 
        dcc.Dropdown(
            id='pitcher', 
            options=[{'label': pitcher, 'value': pitcher} for pitcher in pitchers], 
            value=pitchers[0]
        ), 
    ], style=style),
    
    html.Div([
        dcc.Markdown('###### Wind Direction'), 
        dcc.Dropdown(
            id='wind_direction', 
            options=[{'label': wd, 'value': wd} for wd in wind_directions], 
            value=wind_directions[0]
        ), 
    ], style=style),
    html.Div([
        dcc.Markdown('###### Attendance'), 
        dcc.Slider(
            id='attendance', 
            min=0, 
            max=60000, 
            step=5000, 
            value=15000, 
            marks={n: str(n) for n in range(0,61000,5000)}
        )
    ], style=style),

    dcc.Markdown('## Prediction:'), 
    html.Div(id='prediction-content', style={'marginBottom': '5em'}), 

])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('inning', 'value'),
     Input('wind_speed', 'value'),
     Input('batter', 'value'),
     Input('pitcher', 'value'),
     Input('wind_direction', 'value'),
     Input('attendance', 'value')
    ])

def predict(inning, wind_speed, batter, pitcher, wind_direction, attendance):

    df = pd.DataFrame(
        columns = ['inning', 'pitcher_team_score', 'p_throws', 'stand', 'top',
       'attendance', 'away_team', 'elapsed_time', 'home_team', 'venue_name',
       'weather', 'delay', 'year', 'wind_speed', 'wind_direction',
       'temperature', 'batter', 'pitcher'],
        data = [[inning, 0, 'L', 'L', True, attendance, 'sln', 10, 'chn', 'Wrigley Field', 
                 'clear', 0, 2015, wind_speed, wind_direction, 44, batter, pitcher]]
    )

    pipeline = load('model/logreg_pickle.joblib')
    y_pred = pipeline.predict(df)[0]
    #y_pred_log = pipeline.predict(df)
    #y_pred = np.expm1(y_pred_log)[0]
    
    if y_pred == 'Out':
        message = dcc.Markdown('# Batter is out!')
    else: 
        message = dcc.Markdown('# Batter got on base!')
    return message

