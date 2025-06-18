import sys
import requests
import webbrowser

# Build a function that takes operation's values and determines whether there's an arbitrage opportunity withing these values.
# Identify binary arbitrage operation's variables 


def arb_calc():
    # Create a for loop that goes through each binary market in Polymarket
    # Web scrapes each event to extract its decimal odds
    # Determine whether there' an arbitrage opportunity
    # If there's an arbitrage opportunity it sends a notification via """ including the profit percentage and market's details
    # If there's no arbitrage opportunity it just keeps running 
    # The bot won't stop until the user manually stops it by pressing CTRL+C
    

def get_binary_market(url = "https://gamma-api.polymarket.com/markets"):
    response = requests.request("GET", url)
    return(response.text)



def calc_arb_percent(outcome_A_decimal, outcome_B_decimal):
    #Expects the decimal percentage of the two possible outcomes.
    try: 
        float(outcome_A_decimal, outcome_B_decimal)
    except ValueError:
        sys.exit("Outcome A & B weren't given as decimal numbers")
    else:
        # Player A wins
        player_A_wins = (1/outcome_A_decimal)x 100
        player_B_wins = (1/outcome_B_decimal)x 100
        total_prob = player_A_wins + player_B_wins
        # If total_prob < 100% then there's an arbitrage opportunity
        if total_prob < 100:
            # Returns true if there's an arbitrage opportunity and profit percentage
            return True, str("+", float(100-total_prob) + "%")
        elif total_prob >= 100:
            # returns false if there's no arbitrage opportunity and losing percentage
            return True, str("-", float(-(100-total_prob)) + "%")
        