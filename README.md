# Polymarket's Binary Arbitrage Bot


## Project Status: Under Active Development 🚧

This project is currently in active development. Until it reaches a more stable release, **expect frequent and potentially breaking updates**. I'm working hard to get things polished, and your feedback is welcome!

## How does binary arbitrage work?

Let’s consider this market about Kamala winning Vermont by 32 points. We would classify this as Binary because there is 1 yes and 1 no option to place a bet on. Now, the first instance of arbitrage could be within the **same** market. If we add the 72c yes and the 35c no, we get a total of **107**, indicating that there is no arbitrage opportunity here. If for example, it were 72 and 25, we would say there is a **3%** arbitrage opportunity because that total adds up to **97**. 

### Explanation:

If you owned both positions, winning the 72c bet would earn you 28c. However, you would lose 25c from the no position and be left with 3 cents **(per contract)**. Conversely, winning the 25c no bet would net you 75 cents, but you subtract 72 because you also own the 72c yes position, netting you 3 cents again. We see here that regardless of the outcome of this binary market, you are guaranteed a 3 cent profit per contract. 

*Credits to explanation: u/areebkhan280*

## How does the bot work?

The bot surfs through Polymarket's web while it's running., identifies any possible binary arbitrage opportunity and notifies the user.

## How to get started:

Istructions will be given later on, sorry for the inconvenience.

## How to contribute:

Contributions are limited while I'm constructing the project's main framework. However, any feedback or ideas are always welcomed.



## Future Updates:

In the future, we aim to expand its functionality to include working with cross-binary prediction markets, such as Kalshi, Robinhood...etc in order to catch potential arbitrage opportunities.

## Disclaimer

**I do not hold any responsibility for any direct or indirect losses, damages, or inconveniences that may arise from your use of this bot. Your use of this bot is at your own risk.**
