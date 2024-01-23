import import_ipynb
import model 

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = input(f'Enter the day from these options -> {days} when the match will be played: ')
time = int(input('Enter the time (e.g. if the match starts at 7 pm you may enter 19) when it will begin: '))
team_h = input(f'Enter the name of the "Home Team from the folloing teams:\n{list(df_22_24.HomeTeam.unique())}: ')
team_a = input(f'Enter the name of the "Away Team":\n{list(df_22_24.HomeTeam.unique())}: ')
if prediction(day, time, team_h, team_a)[0][0] == 0:
    print(f'{team_h} will DO NOT WIN meaning that the match will be DRAW OR LOSE.')
else:
    print(f'{team_h} will WIN.')
print(f'The expected number of goals are: {prediction(day, time, team_h, team_a)[1][0]:.2f}')
