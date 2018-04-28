# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:31:59 2018

@author: dell
"""

def run_formula(dv, param = None):
    defult_param = {'t1':6}
    if not param:
        param = defult_param
    
    mawavd= dv.add_formula('mawavd', 
           '''Ts_Sum(((close_adj-open_adj)*volume)/(high-low),%s)/%s'''
           %(param['t1']),
           is_quarterly=False)
    
    return mawavd