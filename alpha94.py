# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:15:18 2018

@author: dell
"""


def run_formula(dv, param = None):
    defult_param = {'t1':1,'t2':1,'t3':0,'t4':30}
    if not param:
        param = defult_param
    
    alpha94 = dv.add_formula('alpha94', 
           '''Ts_Sum(If(close_adj>Delay(close_adj,%s),volume,
           If(close_adj<Delay(close_adj,%s),-volume,%s)),%s)'''
           %(param['t1'],param['t2'],param['t3'],param['t4']),
           is_quarterly=False)
    
    return alpha94