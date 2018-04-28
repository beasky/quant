# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:29:44 2018

@author: dell
"""


def run_formula(dv, param = None):
    defult_param = {'t1':11,'t2':2}
    if not param:
        param = defult_param
    
    alpha188 = dv.add_formula('alpha188', 
           '''((high-low-Sma(high-low,%s,%s))/Sma(high-low,%s,%s))*100'''
           %(param['t1'],param['t2'],param['t1'],param['t2']),
           is_quarterly=False)
    
    return alpha188