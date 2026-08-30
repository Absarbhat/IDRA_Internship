# IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DATASETS
matches = pd.read_csv("datasets/matches.csv")
deliveries = pd.read_csv("datasets/deliveries.csv")


print(matches.head())
print(deliveries.head())


# 1.MOST SUCCESSFUL TEAM(MOST WINS)

name_fixes = {
    'Kings XI Punjab':'Punjab Kings',
    'Royal Challengers Bangalore':'Royal Challengers Bangaluru'
}
clean_winners = matches['winner'].replace(name_fixes)
team_wins_df = clean_winners.value_counts()
team_wins_df.columns = ['Team','Wins']
team_wins_df.to_csv("outputs/csv/team_wins.csv",index=False)

# PLOTTING
plt.figure(figsize=(9,5))
team_wins_df.head(5).plot(kind='bar', color='midnightblue')
plt.title("Most successful Teams",fontweight='bold',fontsize= 16)
plt.xlabel("Teams",fontweight='bold',fontsize= 12)
plt.ylabel("Wins",fontweight='bold',fontsize= 12)
plt.xticks(rotation=45,ha='right')
plt.tight_layout()

plt.savefig("graphs/bar/team_wins.png",dpi=400)
plt.show()


# 2.TOP BATSMEN(MOST RUNS)

top_batsmen = deliveries.groupby('batter')['batsman_runs'].sum().reset_index()
top_batsmen = top_batsmen.sort_values(by='batsman_runs',ascending=False)
top_batsmen.to_csv("outputs/csv/top_batsmen.csv",index=False)

# PLOTTING
top_batsmen.head(5).plot(kind='bar', x='batter', y='batsman_runs', color='teal')
plt.title("Most Runs",fontweight='bold',fontsize= 16)
plt.xlabel("Batter",fontweight='bold',fontsize= 12)
plt.ylabel("Runs",fontweight='bold',fontsize= 12)
plt.xticks(rotation=45,ha='right')
plt.tight_layout()

plt.savefig("graphs/bar/top_batsmen.png",dpi=400)
plt.show()


# 3.STRIKE RATE(FAST SCORERS)

runs = deliveries.groupby('batter')['batsman_runs'].sum()
balls = deliveries.groupby('batter')['ball'].count()
strike_rate = (runs/balls) * 100
strike_rate = strike_rate[runs >=1000]
strike_rate = strike_rate.sort_values(ascending=False)

strike_rate.reset_index().rename(columns={'batter':'Batter',0:'Strike Rate'}).to_csv("outputs/csv/strike_rate.csv",index=False)

# PLOTTING
plt.figure(figsize=(9,5))
strike_rate.head(5).plot(kind='bar',color='magenta')
plt.title("Best Strike Rate",fontweight='bold',fontsize= 16)
plt.xlabel("Batter",fontweight='bold',fontsize= 12)
plt.ylabel("Strike Rates",fontweight='bold',fontsize= 12)
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.savefig("graphs/bar/strike-rate.png",dpi=400)
plt.show()



# 4.TOSS IMPACT

toss_win_match = matches[matches['toss_winner'] ==matches['winner']]
toss_percent = (len(toss_win_match) / len(matches)) * 100

pd.DataFrame({
    "Metric": ["Toss Win + Match Win", "Others"],
    "Count": [len(toss_win_match), len(matches) - len(toss_win_match)]
}).to_csv("outputs/csv/toss_impact.csv",index=False)

sizes = [len(toss_win_match), len(matches) - len(toss_win_match)]

# PLOTTING
plt.pie(sizes, labels=["Win Match", "Lose Match"], autopct="%1.1f%%")
plt.title("Toss Impact",y=1.05,fontweight='bold',fontsize= 16)
plt.savefig("graphs/pie/toss_impact.png",dpi=400)
plt.show()


# 5.TOP SIX HITTERS

sixes = deliveries[deliveries['batsman_runs'] == 6]
top_sixes = sixes['batter'].value_counts()

top_sixes.reset_index().rename(columns={'batter':'Batter','count':'Sixes'}).to_csv("outputs/csv/top_sixes.csv",index=False)

# PLOTTING
top_sixes.head(5).plot(kind='bar',color='gray')
plt.title("Six Hitters",fontweight='bold',fontsize= 16)
plt.xlabel("Batter",fontweight='bold',fontsize= 12)
plt.ylabel("Sixes",fontweight='bold',fontsize= 12)
plt.xticks(rotation=45,ha='right')
plt.tight_layout()

plt.savefig("graphs/bar/top_sixes.png",dpi=400)
plt.show()


# 6.BEST BOWLERS(MOST WICKETS)
bowler_wickets = deliveries[deliveries['dismissal_kind'].notna() & (deliveries['dismissal_kind'] !='run out')]
top_bowlers = bowler_wickets['bowler'].value_counts()
top_bowlers.reset_index().rename(columns={'bowler':'Bowler','count':'Wickets'}).to_csv("outputs/csv/top_bowlers.csv",index=False)

# PLOTTING
plt.figure(figsize=(9,5))
top_bowlers.head(5).plot(kind='bar',color='red')
plt.title("Most Wickets",fontweight='bold',fontsize= 16)
plt.xlabel("Bowler",fontweight='bold',fontsize= 12)
plt.ylabel("Wickets",fontweight='bold',fontsize= 12)
plt.xticks(rotation=45,ha='right')
plt.tight_layout()

plt.savefig("graphs/bar/top_bowlers.png",dpi=400)
plt.show()


# 7.HOME ADVANTAGE

stadium_home_teams = {
    'Eden Gardens': 'Kolkata Knight Riders',
    'Wankhede Stadium': 'Mumbai Indians',
    'M. Chinnaswamy Stadium': 'Royal Challengers Bengaluru',
    'M Chinnaswamy Stadium': 'Royal Challengers Bengaluru',
    'MA Chidambaram Stadium, Chepauk': 'Chennai Super Kings',
    'M. A. Chidambaram Stadium': 'Chennai Super Kings',
    'Rajiv Gandhi International Cricket Stadium': 'Sunrisers Hyderabad',
    'Rajiv Gandhi International Stadium, Uppal': 'Sunrisers Hyderabad',
    'Sawai Mansingh Stadium': 'Rajasthan Royals',
    'Arun Jaitley Stadium': 'Delhi Capitals',
    'Feroz Shah Kotla': 'Delhi Capitals', 
    'Narendra Modi Stadium': 'Gujarat Titans',
    'Sardar Patel Stadium, Motera': 'Gujarat Titans',
    'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium': 'Lucknow Super Giants',
    'Ekana Cricket Stadium': 'Lucknow Super Giants',
    'Maharaja Yadavindra Singh International Cricket Stadium': 'Punjab Kings',
    'Punjab Cricket Association IS Bindra Stadium, Mohali': 'Punjab Kings'
}

home_matches = matches[matches['venue'].isin(stadium_home_teams.keys())].copy()
home_matches['home_team'] = home_matches['venue'].map(stadium_home_teams)

name_fixes = {
    'Kings XI Punjab': 'Punjab Kings',
    'Royal Challengers Bangalore': 'Royal Challengers Bengaluru'
}
home_matches['winner'] = home_matches['winner'].replace(name_fixes)

home_matches['home_win'] = home_matches['winner'] == home_matches['home_team']

home_advantage_stats = home_matches.groupby('home_team')['home_win'].mean() * 100
top_5_home_teams = home_advantage_stats.sort_values(ascending=False).head(5)
top_5_home_teams.reset_index().rename(columns={'home_win':'Home Win Percentage (%)'}).to_csv("outputs/csv/home_advantage.csv",index=False)

# PLOTTING
plt.figure(figsize=(9, 5))
top_5_home_teams.plot(kind='bar', color="orchid", width=0.4)
plt.title("Top 5 IPL Teams with Highest Home Ground Win Percentage", fontweight='bold', fontsize=16, pad=20, color='#111827')
plt.ylabel("Win Percentage (%)", fontweight='bold', fontsize=12, labelpad=10)
plt.xlabel("Team", fontweight='bold', fontsize=12, labelpad=10)

plt.xticks(rotation=25, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig("graphs/bar/home_advantage.png", dpi=400)
plt.show()


# 8.MATCH TYPE(CHASING VS DEFENDING)

chasing_wins = matches[
    ((matches['toss_winner'] == matches['winner']) & (matches['toss_decision'] == 'field')) |
    ((matches['toss_winner'] != matches['winner']) & (matches['toss_decision'] == 'bat'))
]

defending_wins = matches[
    ((matches['toss_winner'] == matches['winner']) & (matches['toss_decision'] == 'bat')) |
    ((matches['toss_winner'] != matches['winner']) & (matches['toss_decision'] == 'field'))
]

pd.DataFrame({
    "Type": ["Chasing Win", "Defending Win"],
    "Count": [len(chasing_wins), len(defending_wins)]
}).to_csv("outputs/csv/match_type.csv",index=False)

# PLOTTING
plt.pie([len(chasing_wins), len(defending_wins)], 
        labels=["Chasing", "Defending"], 
        colors=['maroon', 'salmon'], 
        autopct="%1.1f%%")

plt.title("Chasing VS Defending", y=1.05, fontweight='bold', fontsize=16)

plt.savefig("graphs/pie/match_type.png", dpi=400)
plt.show()

# 9.IPL WEATHER & DISRUPTION INDEX ACROSS SEASONS


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


if 'method' in matches.columns:
    disrupted = matches[(matches['method'] == 'D/L') | (matches['result'] == 'no result')]
else:
    disrupted = matches[matches['result'].isin(['no result', 'Tie'])]

disrupt_stats = disrupted.groupby('season').size().reset_index(name='disrupted_count')
all_seasons = pd.DataFrame({'season': matches['season'].unique()})
disrupt_stats = pd.merge(all_seasons, disrupt_stats, on='season', how='left').fillna(0)

disrupt_stats['season'] = disrupt_stats['season'].astype(str).replace({'2007/08': '2008', '2009/10': '2010', '2020/21': '2020'})
disrupt_stats = disrupt_stats.sort_values('season', ascending=True)

disrupt_stats.to_csv("outputs/csv/weather_disruptions.csv", index=False)

# PLOTTING
plt.figure(figsize=(10, 6))

num_seasons = len(disrupt_stats)
colors = cm.plasma(np.linspace(0.2, 0.85, num_seasons))

for idx, row in enumerate(disrupt_stats.itertuples()):
    plt.hlines(y=row.season, xmin=0, xmax=row.disrupted_count, color=colors[idx], linewidth=2, alpha=0.6)
    plt.scatter(row.disrupted_count, row.season, color=colors[idx], s=120, zorder=3, edgecolors='black', linewidths=0.5)

plt.title("IPL Weather & Disruption Index Across Seasons", fontweight='bold', fontsize=16, pad=20, color='#111827')
plt.xlabel("Number of Disrupted Matches (DLS / No-Result)", fontweight='bold', fontsize=12, labelpad=12)
plt.ylabel("Season", fontweight='bold', fontsize=12, labelpad=12)

max_count = int(disrupt_stats['disrupted_count'].max())
plt.xticks(range(0, max_count + 2), fontsize=10)
plt.yticks(fontsize=10)

plt.grid(axis='x', linestyle=':', alpha=0.5)
plt.tight_layout()

plt.savefig("graphs/bar/weather_disruptions_lollipop.png", dpi=400)
plt.show()


# IMPORTING TO EXCEL
with pd.ExcelWriter("outputs/excel/final_report.xlsx") as writer:
    # 1. Most Successful Team
    team_wins_df.reset_index().to_excel(writer, sheet_name="Team Wins", index=False)
    
    # 2. Top Batsmen
    top_batsmen.to_excel(writer, sheet_name="Batting", index=False)
    
    # 3. Strike Rate (Rounding to 2 decimal places)
    strike_rate_df = strike_rate.reset_index()
    strike_rate_df.columns = ['Batter', 'Strike Rate']
    strike_rate_df['Strike Rate'] = strike_rate_df['Strike Rate'].round(2) # Rounding step
    strike_rate_df.to_csv("outputs/csv/strike_rate.csv", index=False) # Updates CSV file too
    strike_rate_df.to_excel(writer, sheet_name="Strike Rate", index=False)
    
    # 4. Toss Impact
    pd.DataFrame({
        "Metric": ["Toss Win + Match Win", "Others"],
        "Count": [len(toss_win_match), len(matches) - len(toss_win_match)]
    }).to_excel(writer, sheet_name="Toss Decision Impact", index=False)
    
    # 5. Top Six Hitters
    top_sixes_df = top_sixes.reset_index()
    top_sixes_df.columns = ['Batter', 'Sixes']
    top_sixes_df.to_excel(writer, sheet_name="Sixes Leaderboard", index=False)
    
    # 6. Best Bowlers
    top_bowlers_df = top_bowlers.reset_index()
    top_bowlers_df.columns = ['Bowler', 'Wickets']
    top_bowlers_df.to_excel(writer, sheet_name="Bowling", index=False)
    
    # 7. Home Advantage (Rounding to 2 decimal places)
    top_5_home_teams_df = top_5_home_teams.reset_index()
    top_5_home_teams_df.columns = ['Team', 'Home Win Percentage (%)']
    top_5_home_teams_df['Home Win Percentage (%)'] = top_5_home_teams_df['Home Win Percentage (%)'].round(2) # Rounding step
    top_5_home_teams_df.to_csv("outputs/csv/home_advantage.csv", index=False) # Updates CSV file too
    top_5_home_teams_df.to_excel(writer, sheet_name="Home Advantage", index=False)
    
    # 8. Match Type (Chasing vs Defending)
    pd.DataFrame({
        "Type": ["Chasing Win", "Defending Win"],
        "Count": [len(chasing_wins), len(defending_wins)]
    }).to_excel(writer, sheet_name="Chasing vs Defending", index=False)
    
    # 9. Weather & Disruptions
    disrupt_stats.to_excel(writer, sheet_name="Weather Disruptions", index=False)

print("All 9 datasets have been successfully compiled into outputs/excel/final_report.xlsx!")
