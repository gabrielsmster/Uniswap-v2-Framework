# Uniswap-v2-Framework

This repository contains a few analysis on Uniswap-v2 pair ETH-DAI dynamics. It includes data collection, LP's return analysis over time, modelling actual rules and shifts on trading fees and also future scenarios.

cadCAD has been used for modelling data.


<b>/notebooks/</b> Contains jupyter notebooks with all scripts

<b>/model/</b> Contains cadCAD configurations for modelling past data

<b>/model_future/</b> Contains cadCAD configurations for modelling future data

<b>/images/</b> Contains matplot graphs from scripts outcome

_______________

<b>scenarios.txt</b> - Description of analyzed scenarios

<b>History</b>

<b>V1</b> - Actual

<b>V2</b> - Fee to 0.25%

<b>V3</b> - Fee to 0.35%

<b>Future</b>

<b>V1</b> - Current volume (avg last 45 days) + stale price

<b>V2</b> - Double volume + stale price

<b>V3</b> - Current volume + 25% increase in eth demand

<b>V4</b> - Current volume + 60% increase in eth demand

<b>V5</b> - Current volume + 25% decrease in eth demand

<b>V6</b> - Current volume + 60% decrease in eth demand

<b>V7</b> - Double volume + 60% increase in eth demand

<b>V8</b> - Double volume + 60% decrease in eth demand
