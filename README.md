# Polymarket's Binary Arbitrage Bot    


![images](https://github.com/user-attachments/assets/d0db897d-0f4d-45e7-b25d-06eb83048944)


## How does binary arbitrage work?

Let’s consider this market about Kamala winning Vermont by 32 points. We would classify this as Binary because there is 1 yes and 1 no option to place a bet on. Now, the first instance of arbitrage could be within the **same** market. If we add the 72c yes and the 35c no, we get a total of **107**, indicating that there is no arbitrage opportunity here. If for example, it were 72 and 25, we would say there is a **3%** arbitrage opportunity because that total adds up to **97**. 

### Explanation:

If you owned both positions, winning the 72c bet would earn you 28c. However, you would lose 25c from the no position and be left with 3 cents **(per contract)**. Conversely, winning the 25c no bet would net you 75 cents, but you subtract 72 because you also own the 72c yes position, netting you 3 cents again. We see here that regardless of the outcome of this binary market, you are guaranteed a 3 cent profit per contract. 

*Credits to explanation: u/areebkhan280*

## Technical Overview

The bot currently uses Polymarket’s Gamma Markets API, a RESTful service provided by Polymarket. This API serves as a hosted index of all on-chain market data and supplies:

    Resolved and unresolved market outcomes

    Market metadata (e.g., question text, categories, volumes)

    Token pairings and market structures

    Real-time price data for YES/NO or categorical outcomes

By querying this API regularly, the bot identifies pricing discrepancies that signal arbitrage opportunities — for example:

    Binary arbitrage: where YES + NO < $1

    Multi-market arbitrage: where the total of all mutually exclusive YES markets < $1 or > $1


Once an arbitrage signal is detected, the bot logs or alerts the user with actionable information (email,logging file...etc)

## How to install:

    pip install polymarket-arbitrage-bot
    python3 -m bot.main


## Future Updates:

In the future, we aim to expand its functionality to include working with cross-binary prediction markets, such as Kalshi, Robinhood...etc in order to catch potential arbitrage opportunities.

## Disclaimer

**I do not hold any responsibility for any direct or indirect losses, damages, or inconveniences that may arise from your use of this bot. Your use of this bot is at your own risk.**
