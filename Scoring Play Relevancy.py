# This is a list of tuples in format: (time of scoring play, type of score, team that scored)
# Type of score: 0 for free throw, 1 for 2pt, 2 for 3pt
# Team that scored: 0 for home, 1 for away

import math
import matplotlib.pyplot as plt
import mpld3

mock_game = [
    (120, 1, 0),  # 2:00 - Home team 2pt
    (145, 2, 1),  # 2:25 - Away team 3pt
    (210, 1, 0),  # 3:30 - Home team 2pt
    (240, 0, 1),  # 4:00 - Away team free throw
    (241, 0, 1),  # 4:01 - Away team free throw (second of two)
    (300, 2, 0),  # 5:00 - Home team 3pt
    (330, 1, 1),  # 5:30 - Away team 2pt
    (400, 1, 0),  # 6:40 - Home team 2pt
    (450, 1, 1),  # 7:30 - Away team 2pt
    (480, 0, 0),  # 8:00 - Home team free throw
    (510, 2, 1),  # 8:30 - Away team 3pt
    (570, 1, 0),  # 9:30 - Home team 2pt
    (600, 1, 1),  # 10:00 - Away team 2pt (end of 1st quarter)
    (660, 1, 0),  # 11:00 - Home team 2pt
    (700, 2, 1),  # 11:40 - Away team 3pt
    (760, 1, 0),  # 12:40 - Home team 2pt
    (800, 0, 1),  # 13:20 - Away team free throw
    (801, 0, 1),  # 13:21 - Away team free throw (second of two)
    (850, 2, 0),  # 14:10 - Home team 3pt
    (900, 1, 1),  # 15:00 - Away team 2pt
    (960, 1, 0),  # 16:00 - Home team 2pt
    (1000, 1, 1),  # 16:40 - Away team 2pt
    (1050, 0, 0),  # 17:30 - Home team free throw
    (1051, 0, 0),  # 17:31 - Home team free throw (second of two)
    (1100, 2, 1),  # 18:20 - Away team 3pt
    (1150, 1, 0),  # 19:10 - Home team 2pt
    (1200, 1, 1),  # 20:00 - Away team 2pt (end of 2nd quarter / first half)
    (1260, 2, 1),  # 21:00 - Away team 3pt
    (1300, 1, 0),  # 21:40 - Home team 2pt
    (1350, 1, 1),  # 22:30 - Away team 2pt
    (1400, 0, 0),  # 23:20 - Home team free throw
    (1401, 0, 0),  # 23:21 - Home team free throw (second of two)
    (1450, 2, 1),  # 24:10 - Away team 3pt
    (1500, 1, 0),  # 25:00 - Home team 2pt
    (1560, 1, 1),  # 26:00 - Away team 2pt
    (1600, 2, 0),  # 26:40 - Home team 3pt
    (1650, 1, 1),  # 27:30 - Away team 2pt
    (1700, 0, 0),  # 28:20 - Home team free throw
    (1750, 2, 1),  # 29:10 - Away team 3pt
    (1800, 1, 0),  # 30:00 - Home team 2pt (end of 3rd quarter)
    (1850, 1, 1),  # 30:50 - Away team 2pt
    (1880, 2, 0),  # 31:20 - Home team 3pt
    (1910, 1, 1),  # 31:50 - Away team 2pt
    (1940, 0, 0),  # 32:20 - Home team free throw
    (1941, 0, 0),  # 32:21 - Home team free throw (second of two)
    (1970, 2, 1),  # 32:50 - Away team 3pt
    (2000, 1, 0),  # 33:20 - Home team 2pt
    (2040, 1, 1),  # 34:00 - Away team 2pt
    (2080, 2, 0),  # 34:40 - Home team 3pt
    (2110, 1, 1),  # 35:10 - Away team 2pt
    (2140, 0, 0),  # 35:40 - Home team free throw
    (2170, 2, 1),  # 36:10 - Away team 3pt
    (2200, 1, 0),  # 36:40 - Home team 2pt
    (2230, 1, 1),  # 37:10 - Away team 2pt
    (2260, 2, 0),  # 37:40 - Home team 3pt
    (2290, 0, 1),  # 38:10 - Away team free throw
    (2291, 0, 1),  # 38:11 - Away team free throw (second of two)
    (2320, 1, 0),  # 38:40 - Home team 2pt
    (2350, 1, 1),  # 39:10 - Away team 2pt
    (2380, 0, 0),  # 39:40 - Home team free throw
    (2381, 0, 0),  # 39:41 - Home team free throw (second of two)
]

complex_mock_game = [
    # First Quarter
    (30, 2, 0),    # Home team 3pt
    (50, 1, 1),    # Away team 2pt
    (70, 1, 0),    # Home team 2pt
    (90, 2, 1),    # Away team 3pt
    (110, 0, 0),   # Home team free throw
    (111, 0, 0),   # Home team free throw
    (130, 1, 1),   # Away team 2pt
    (150, 2, 0),   # Home team 3pt
    (170, 1, 1),   # Away team 2pt
    (190, 1, 0),   # Home team 2pt
    (210, 2, 1),   # Away team 3pt
    (230, 1, 0),   # Home team 2pt
    (250, 1, 1),   # Away team 2pt
    (270, 0, 0),   # Home team free throw
    (290, 2, 1),   # Away team 3pt
    (310, 1, 0),   # Home team 2pt
    (330, 1, 1),   # Away team 2pt
    (350, 2, 0),   # Home team 3pt
    (370, 1, 1),   # Away team 2pt
    (390, 1, 0),   # Home team 2pt
    (410, 2, 1),   # Away team 3pt
    (430, 1, 0),   # Home team 2pt
    (450, 1, 1),   # Away team 2pt
    (470, 0, 0),   # Home team free throw
    (471, 0, 0),   # Home team free throw
    (490, 2, 1),   # Away team 3pt
    (510, 1, 0),   # Home team 2pt
    (530, 1, 1),   # Away team 2pt
    (550, 2, 0),   # Home team 3pt
    (570, 1, 1),   # Away team 2pt
    (590, 1, 0),   # Home team 2pt
    
    # Second Quarter
    (610, 2, 1),   # Away team 3pt
    (630, 1, 0),   # Home team 2pt
    (650, 1, 1),   # Away team 2pt
    (670, 2, 0),   # Home team 3pt
    (690, 1, 1),   # Away team 2pt
    (710, 1, 0),   # Home team 2pt
    (730, 2, 1),   # Away team 3pt
    (750, 1, 0),   # Home team 2pt
    (770, 1, 1),   # Away team 2pt
    (790, 0, 0),   # Home team free throw
    (791, 0, 0),   # Home team free throw
    # Home team scoring run
    (810, 2, 0),   # Home team 3pt
    (830, 1, 0),   # Home team 2pt
    (850, 2, 0),   # Home team 3pt
    (870, 1, 0),   # Home team 2pt
    (890, 2, 0),   # Home team 3pt
    (910, 1, 0),   # Home team 2pt
    (930, 2, 0),   # Home team 3pt
    # Away team comeback
    (950, 2, 1),   # Away team 3pt
    (970, 2, 1),   # Away team 3pt
    (990, 1, 1),   # Away team 2pt
    (1010, 2, 1),  # Away team 3pt
    (1030, 1, 1),  # Away team 2pt
    (1050, 0, 1),  # Away team free throw
    (1051, 0, 1),  # Away team free throw
    (1070, 2, 0),  # Home team 3pt
    (1090, 1, 1),  # Away team 2pt
    (1110, 1, 0),  # Home team 2pt
    (1130, 2, 1),  # Away team 3pt
    (1150, 1, 0),  # Home team 2pt
    (1170, 1, 1),  # Away team 2pt
    (1190, 0, 0),  # Home team free throw
    
    # Third Quarter
    (1210, 2, 1),  # Away team 3pt
    (1230, 1, 0),  # Home team 2pt
    (1250, 1, 1),  # Away team 2pt
    (1270, 2, 0),  # Home team 3pt
    (1290, 1, 1),  # Away team 2pt
    (1310, 1, 0),  # Home team 2pt
    (1330, 2, 1),  # Away team 3pt
    (1350, 1, 0),  # Home team 2pt
    (1370, 1, 1),  # Away team 2pt
    (1390, 0, 0),  # Home team free throw
    (1391, 0, 0),  # Home team free throw
    (1410, 2, 1),  # Away team 3pt
    (1430, 1, 0),  # Home team 2pt
    (1450, 1, 1),  # Away team 2pt
    (1470, 2, 0),  # Home team 3pt
    (1490, 1, 1),  # Away team 2pt
    (1510, 1, 0),  # Home team 2pt
    (1530, 2, 1),  # Away team 3pt
    (1550, 1, 0),  # Home team 2pt
    (1570, 1, 1),  # Away team 2pt
    (1590, 0, 0),  # Home team free throw
    (1610, 2, 1),  # Away team 3pt
    (1630, 1, 0),  # Home team 2pt
    (1650, 1, 1),  # Away team 2pt
    (1670, 2, 0),  # Home team 3pt
    (1690, 1, 1),  # Away team 2pt
    (1710, 1, 0),  # Home team 2pt
    (1730, 2, 1),  # Away team 3pt
    (1750, 1, 0),  # Home team 2pt
    (1770, 1, 1),  # Away team 2pt
    (1790, 0, 0),  # Home team free throw
    
    # Fourth Quarter
    (1810, 2, 1),  # Away team 3pt
    (1830, 1, 0),  # Home team 2pt
    (1850, 1, 1),  # Away team 2pt
    (1870, 2, 0),  # Home team 3pt
    (1890, 1, 1),  # Away team 2pt
    (1910, 1, 0),  # Home team 2pt
    (1930, 2, 1),  # Away team 3pt
    (1950, 1, 0),  # Home team 2pt
    (1970, 1, 1),  # Away team 2pt
    (1990, 0, 0),  # Home team free throw
    (1991, 0, 0),  # Home team free throw
    # Rapid back-and-forth scoring
    (2010, 2, 1),  # Away team 3pt
    (2030, 2, 0),  # Home team 3pt
    (2050, 2, 1),  # Away team 3pt
    (2070, 2, 0),  # Home team 3pt
    (2090, 2, 1),  # Away team 3pt
    (2110, 2, 0),  # Home team 3pt
    # Close game finish
    (2130, 1, 1),  # Away team 2pt
    (2150, 1, 0),  # Home team 2pt
    (2170, 1, 1),  # Away team 2pt
    (2190, 1, 0),  # Home team 2pt
    (2210, 0, 1),  # Away team free throw
    (2211, 0, 1),  # Away team free throw
    (2230, 1, 0),  # Home team 2pt
    (2250, 1, 1),  # Away team 2pt
    (2270, 0, 0),  # Home team free throw
    (2271, 0, 0),  # Home team free throw
    (2290, 1, 1),  # Away team 2pt
    (2310, 1, 0),  # Home team 2pt
    (2330, 0, 1),  # Away team free throw
    (2350, 2, 0),  # Home team 3pt
    (2370, 1, 1),  # Away team 2pt
    (2390, 0, 0),  # Home team free throw
    (2391, 0, 0),  # Home team free throw
]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def calculate_multiplier(elapsed: float, total: float, ceiling: float) -> float:
    """
    :param elapsed: The amount of time elapsed in the game in seconds
    :param total: The total amount of time in the game in seconds
    :param ceiling: The maximum multiplier value
    :return: A multiplier between 1 and 1.5 that represents the relevancy of a scoring play based on the time remaining
    """
    e = math.e
    result = 1 + (ceiling - 1) * ((math.exp(elapsed / total) - 1) / ((e - 1)))
    return result

def scoring_play_relevancy(game):


    time_and_relevancy = []
    home_score = 0  
    away_score = 0 
    

    for play in game:

        print(f"Home score: {home_score}, Away score: {away_score}")
        score_diff = abs(home_score - away_score)
        time = play[0]
        score_type = play[1] + 1
        team = play[2]

        # Set the initial relevancy score

        if score_type == 1:
            relevancy = 15
        elif score_type == 2:
            relevancy = 25
        else:
            relevancy = 30

        print(f"Initial relevancy: {relevancy}")

        # Update the relevancy score based on the time left in the game
    

        relevancy *= calculate_multiplier(time, 2400, 1.5)
        print(f"Relevancy after time left in game: {relevancy}")

        # Update the relevancy score based on the time left in the quarter

        relevancy *= calculate_multiplier(time % 600, 600, 1.5)
        print(f"Relevancy after time left in quarter: {relevancy}")

        # Update the relevancy score based on the score difference
        if home_score > 10 and away_score > 10:
            if score_diff <= 3:
                relevancy *= 1.25
            elif score_diff <= 6:
                relevancy *= 1.1

            print(f"Relevancy after score difference: {relevancy}")

            # Update the relevancy score based on whether the lead is changing

            if home_score < away_score and home_score + score_type > away_score:
                relevancy *= 1.5
            elif away_score < home_score and away_score + score_type > home_score:
                relevancy *= 1.5
            elif home_score == away_score and home_score + score_type > away_score:
                relevancy *= 1.25
            elif home_score == away_score and away_score + score_type > home_score:
                relevancy *= 1.25

        print(f"Relevancy after lead change: {relevancy}")

        # Update the score
        if team == 0:
            home_score += score_type
        else:
            away_score += score_type

        time_and_relevancy.append((time, relevancy))

    return time_and_relevancy

def plot_interactive_relevancy_scores(game):
    # Get relevancy scores and additional play information
    time_and_relevancy = scoring_play_relevancy(game)
    
    # Separate data for plotting
    times, relevancies = zip(*time_and_relevancy)
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    scatter = ax.scatter(times, relevancies, c=relevancies, cmap='viridis', s=50)
    
    # Customize the plot
    ax.set_title('Scoring Play Relevancy Over Time', fontsize=16)
    ax.set_xlabel('Game Time (seconds)', fontsize=12)
    ax.set_ylabel('Relevancy Score', fontsize=12)
    
    # Add vertical lines to separate quarters
    for quarter_end in [600, 1200, 1800]:
        ax.axvline(x=quarter_end, color='r', linestyle='--', alpha=0.5)
    
    # Add labels for quarters
    for i, quarter_mid in enumerate([300, 900, 1500, 2100]):
        ax.text(quarter_mid, ax.get_ylim()[1], f'Q{i+1}', horizontalalignment='center')
    
    # Create tooltip
    labels = []
    for play, (time, relevancy) in zip(game, time_and_relevancy):
        score_type = ["Free Throw", "2-Pointer", "3-Pointer"][play[1]]
        team = "Home" if play[2] == 0 else "Away"
        label = f"Time: {time}s\nRelevancy: {relevancy:.2f}\nPlay: {score_type} by {team}"
        labels.append(label)
    
    tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
    mpld3.plugins.connect(fig, tooltip)
    
    # Save the interactive plot as an HTML file
    mpld3.save_html(fig, "interactive_relevancy_plot.html")
    
    print("Interactive plot saved as 'interactive_relevancy_plot.html'")

def plot_relevancy_scores(game):
    # Get relevancy scores
    time_and_relevancy = scoring_play_relevancy(game)
    
    # Separate time and relevancy for plotting
    times, relevancies = zip(*time_and_relevancy)
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(times, relevancies, 'bo-')  # 'bo-' means blue color, circle markers, solid line
    
    # Customize the plot
    plt.title('Scoring Play Relevancy Over Time', fontsize=16)
    plt.xlabel('Game Time (seconds)', fontsize=12)
    plt.ylabel('Relevancy Score', fontsize=12)
    
    # Add vertical lines to separate quarters
    for quarter_end in [600, 1200, 1800]:
        plt.axvline(x=quarter_end, color='r', linestyle='--', alpha=0.5)
    
    # Add labels for quarters
    for i, quarter_mid in enumerate([300, 900, 1500, 2100]):
        plt.text(quarter_mid, plt.ylim()[1], f'Q{i+1}', horizontalalignment='center')
    
    # Improve the layout
    plt.tight_layout()
    
    # Show the plot
    plt.savefig('relevancy_plot.png', dpi=300, bbox_inches='tight')


plot_interactive_relevancy_scores(complex_mock_game)