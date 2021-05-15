# Uniswap-v2-Framework

This repository contains a few analysis on Uniswap-v2 pair ETH-DAI dynamics. It includes data collection, LP's return analysis over time, modelling actual rules and shifts on trading fees and also future scenarios.

cadCAD has been used for modelling data.


/notebooks/ Contains jupyter notebooks with all scripts

/model/ Contains cadCAD configurations for modelling past data

/model_future/ Contains cadCAD configurations for modelling future data

/images/ Contains matplot graphs from scripts outcome



scenarios.txt - Description of analyzed scenarios

History
V1 - Actual
V2 - Fee to 0.25%
V3 - Fee to 0.35%

Future
V1 - Current volume (avg last 45 days) + stale price
V2 - Double volume + stale price
V3 - Current volume + 25% increase in eth demand
V4 - Current volume + 60% increase in eth demand
V5 - Current volume + 25% decrease in eth demand
V6 - Current volume + 60% decrease in eth demand
V7 - Double volume + 60% increase in eth demand
V8 - Double volume + 60% decrease in eth demand
