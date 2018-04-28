# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:09:52 2018

@author: dell
"""

def run_formula(dv, param = None):
    defult_param = {'t1':3,'t2':3,'t3':6,'t4':6,'t5':12}
    if not param:
        param = defult_param
    
    alpha27 = dv.add_formula("alpha27", 
           '''Ta('WMA',0,0,0,0,(close_adj-Delay(close_adj,%s))/Delay(close_adj,%s)*100+
           (close_adj-Delay(close_adj,%s))/Delay(close_adj,%s)*100,0,%s)'''
           %(param['t1'],param['t2'],param['t3'],param['t4'],param['t5']),
           is_quarterly=False)
    
    return alpha27 