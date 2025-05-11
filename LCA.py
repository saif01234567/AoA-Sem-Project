import random

# Problem settings
TEAM_SIZE = 5              # Number of elements in one solution
NUM_TEAMS = 6              # Total teams in the league
NUM_SEASONS = 10           # How many times matches are played
VALUE_RANGE = (1, 50)      # Range of numbers in each solution

# Fitness function: maximize the sum of numbers
def evaluate_team(team):
    return sum(team)

# Create a random team
def create_team():
    return [random.randint(*VALUE_RANGE) for _ in range(TEAM_SIZE)]

# Simulate a match between two teams
def play_match(team_a, team_b):
    score_a = evaluate_team(team_a)
    score_b = evaluate_team(team_b)
    return team_a if score_a > score_b else team_b

# Loser learns from winner
def update_team(loser, winner):
    new_team = loser[:]
    for i in range(len(loser)):
        if random.random() < 0.5:
            new_team[i] = winner[i]
        else:
            # Slight mutation
            new_team[i] = random.randint(*VALUE_RANGE)
    return new_team

# Main algorithm
def league_championship_algorithm():
    league = [create_team() for _ in range(NUM_TEAMS)]
    best_team = None
    best_score = float('-inf')

    for season in range(NUM_SEASONS):
        print(f"\n--- Season {season + 1} ---")
        random.shuffle(league)

        for i in range(0, NUM_TEAMS, 2):
            if i + 1 >= NUM_TEAMS:
                continue
            team_a = league[i]
            team_b = league[i + 1]

            winner = play_match(team_a, team_b)
            loser = team_b if winner == team_a else team_a

            updated_loser = update_team(loser, winner)

            # Replace the old loser
            if loser == team_a:
                league[i] = updated_loser
            else:
                league[i + 1] = updated_loser

            # Track best
            for team in league:
                score = evaluate_team(team)
                if score > best_score:
                    best_score = score
                    best_team = team

        print(f"Best team so far: {best_team} with score {best_score}")

    return best_team, best_score

# Run it!
if __name__ == "__main__":
    winner, score = league_championship_algorithm()
    print("\n🏆 Final Best Team:", winner)
    print("🎯 Final Score:", score)
