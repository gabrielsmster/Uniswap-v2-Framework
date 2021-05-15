"""
Model parameters.
"""

# These are the initial conditions of the DAI-ETH Uniswap instance - https://etherscan.io/address/0x09cabEC1eAd1c0Ba254B09efb3EE13841712bE14

# Future modelling
initial_values = {
    'DAI_balance': 106247577754018368903373773,
    'ETH_balance': 84374461520147628767601,
    'UNI_supply': 2327236733612883397790535
}

# aDAI data
# initial_values = {
#     'DAI_balance': 103040751403186867748,
#     'ETH_balance': 534036552023069922,
#     'UNI_supply': 10135742937287
# }

# DAI data
# initial_values = {
#     'DAI_balance': 193590257945653248000,
#     'ETH_balance': 981912652754222464,
#     'UNI_supply': 13787266724292765696
# }

# Original data
# initial_values = {
#     'DAI_balance': 5900000000000000000000,
#     'ETH_balance': 30000000000000000000,
#     'UNI_supply': 30000000000000000000
# }


### Parameters

# These are the parameters of Uniswap that represent the fee collected on each swap. Notice that these are hardcoded in the Uniswap smart contracts, but we model them as parameters in order to be able to do A/B testing and parameter sweeping on them in the future.

sys_params = {
    'fee_numerator': [997],
    'fee_denominator': [1000]
}
