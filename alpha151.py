# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:22:15 2018

@author: dell
"""

def run_formula(dv, param = None):
    defult_param = {'t1':20,'t2':20,'t3':1}
    if not param:
        param = defult_param
    
    alpha151 = dv.add_formula('alpha151','''Sma(close-Delay(close,%s),%s,%s)'''
           %(param['t1'],param['t2'],param['t3']),
           is_quarterly=False)
    
    return alpha151