# Auction Simulation using Sellers and Buyers Agents

## Introduction

This project implements an auction simulation using seller and buyer agents. The goal of the auction is to find an optimal price at which the sellers can sell their goods to the buyers. The auction runs for a predefined number of rounds and aims to maximize the total reward for all participants.

## Code Overview

The code is written in Python and consists of three classes: `Sellers`, `Buyers`, and the auction simulation function `run_auction`. The simulation proceeds as follows:

1. Initialization:
   - The `Sellers` and `Buyers` classes are defined with attributes like `c_valuation` (current valuation), `rp_seller` (number of rounds participated as a seller), `rp_buyer` (number of rounds participated as a buyer), `avg_deal` (average deal price), `alpha` (a random parameter), and `reward` (accumulated reward).

2. Auction Initialization:
   - The number of rounds (`T`) and the number of participants (`N`) are set.
   - Lists `sellers` and `buyers` are created with `N` instances of `Sellers` and `Buyers` classes, respectively.

3. Auction Simulation:
   - The `run_auction` function is called, which simulates the auction for `T` rounds.
   - In each round, the function calculates the price at which the sellers and buyers can trade.
   - After each round, the attributes of sellers and buyers are updated based on the auction outcome.

## Simulation Details

### Sellers and Buyers

Each seller and buyer agent has the following attributes:

- `c_valuation`: A random value representing the current valuation of the seller's/buyer's goods.
- `rp_seller`: The number of rounds the seller has participated in the auction.
- `rp_buyer`: The number of rounds the buyer has participated in the auction.
- `avg_deal`: The average deal price of the seller/buyer in the past rounds.
- `alpha`: A random parameter used in the valuation update formula.
- `reward`: The accumulated reward of the seller/buyer.

### Valuation Update

The valuation of sellers and buyers is updated based on the number of rounds they have participated in (`rp_seller` and `rp_buyer`) and the average deal price (`avg_deal`). The update formula for sellers is:

`c_valuation = avg_deal - sqrt((alpha * log(t)) / rp_seller)`

The update formula for buyers is:

`c_valuation = avg_deal + sqrt((alpha * log(t+1)) / rp_buyer)`

Where `t` represents the current round number.

### Finding Price

The function `findprice` calculates the trading price for sellers and buyers. It sorts the sellers and buyers based on their `c_valuation`, finds the highest bidder and lowest asker, and sets the price as the average of their valuations.

## Conclusion

This project demonstrates a basic auction simulation using seller and buyer agents. The simulation provides insights into how agents' valuations and trading strategies evolve over time. While the current implementation is simplistic, it can be extended and modified for more complex auction scenarios and agent interactions.

For more details, please refer to the code implementation and comments.

For any inquiries or suggestions, feel free to contact the author.
