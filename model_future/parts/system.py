import numpy as np
import pandas as pd
from .utils import *

# Uniswap events from Kaggle/BigQuery
uniswap_events = pd.read_pickle('model/parts/uniswap_events.pickle')

# Behaviors
def actionDecoder(params, step, history, current_state):
    '''
    In this simplified model of Uniswap, we have not modeled user behavior. Instead, we map events to actions.
    '''
    prev_timestep = current_state['timestep']
    if step > 1:
        prev_timestep -= 1
        
    #skip the first two events, as they are already accounted for in the initial conditions of the system
    data_counter = prev_timestep + 2 
    
    action = {
        'eth_sold': 0,
        'tokens_sold': 0,
        'eth_deposit': 0,
        'UNI_burn': 0,        
    }
    
    #### event = uniswap_events['event'][data_counter]
    
    # If 0 = TokenPurchase
    # If 1 = EthPurchase
    # If 2 = AddLiquidity
    
    ### ETH purchase
    ETH_eth_mean = -1000000000000000000
    ETH_eth_std = int(abs(ETH_eth_mean*0.1))
    ETH_token_mean = int(1259000000000000000000)
    ETH_token_std = int(abs(ETH_token_mean*0.1))

    ### Token purchase
    Token_eth_mean = 1000000000000000000
    Token_eth_std = int(abs(Token_eth_mean*0.1))
    Token_token_mean = -1259000000000000000000
    Token_token_std = int(abs(Token_token_mean*0.1))

    ### Liquidity
    LIQ_eth_mean = 16471119085359648768
    LIQ_eth_std = int(abs(ETH_eth_mean*0.3))

    p_token = 0.5
    p_eth = 0.5
    p_liquidity = 0.
    rand_action = np.random.choice(np.arange(0, 3), p=[p_token,p_eth,p_liquidity])
    
    if rand_action == 0:
        action['action_id'] = 'TokenPurchase'
        action['eth_sold'] = int(np.random.normal(Token_eth_mean, Token_eth_std, 1)[0])
    elif rand_action == 1:
        action['action_id'] = 'EthPurchase'
        action['tokens_sold'] = int(np.random.normal(ETH_token_mean, ETH_token_std, 1)[0])
    elif rand_action == 2:
        action['action_id'] = 'AddLiquidity'
        action['eth_deposit'] = int(np.random.normal(LIQ_eth_mean, LIQ_eth_std, 1)[0])

    # action['action_id'] = event
    
    # if event == 'TokenPurchase':
    #     action['eth_sold'] = uniswap_events['eth_delta'][data_counter] #OK
    # elif event == 'EthPurchase':
    #     action['tokens_sold'] = uniswap_events['token_delta'][data_counter]
    # elif event == 'AddLiquidity':
    #     action['eth_deposit'] = uniswap_events['eth_delta'][data_counter]
    # elif event == 'Transfer':
    #     UNI_delta = uniswap_events['uni_delta'][data_counter]
    #     if UNI_delta < 0:
    #         action['UNI_burn'] = -UNI_delta

    return action


# Mechanisms
def mechanismHub_DAI(params, step, history, current_state, input_):
    action = input_['action_id']
    if action == 'TokenPurchase':
        return ethToToken_DAI(params, step, history, current_state, input_)
    elif action == 'EthPurchase':
        return tokenToEth_DAI(params, step, history, current_state, input_)
    elif action == 'AddLiquidity':
        return addLiquidity_DAI(params, step, history, current_state, input_)
    elif action == 'Transfer':
        return removeLiquidity_DAI(params, step, history, current_state, input_)
    return('DAI_balance', current_state['DAI_balance'])
    
def mechanismHub_ETH(params, step, history, current_state, input_):
    action = input_['action_id']
    if action == 'TokenPurchase':
        return ethToToken_ETH(params, step, history, current_state, input_)
    elif action == 'EthPurchase':
        return tokenToEth_ETH(params, step, history, current_state, input_)
    elif action == 'AddLiquidity':
        return addLiquidity_ETH(params, step, history, current_state, input_)
    elif action == 'Transfer':
        return removeLiquidity_ETH(params, step, history, current_state, input_)
    return('ETH_balance', current_state['ETH_balance'])

def mechanismHub_UNI(params, step, history, current_state, input_):
    action = input_['action_id']
    if action == 'AddLiquidity':
        return addLiquidity_UNI(params, step, history, current_state, input_)
    elif action == 'Transfer':
        return removeLiquidity_UNI(params, step, history, current_state, input_)
    return('UNI_supply', current_state['UNI_supply'])