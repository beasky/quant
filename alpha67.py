# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:18:03 2018

@author: dell
"""


def run_formula(dv, param = None):
    defult_param = {'t1':1,'t2':24,'t3':1,'t4':1,'t5':24,'t6':1}
    if not param:
        param = defult_param
    
    alpha67 = dv.add_formula('alpha67', 
           '''Sma(Max(close_adj-Delay(close_adj,1),0),24,1)/Sma(Abs(close_adj-Delay(close_adj,1)),24,1)*100'''
           %(param['t1'],param['t2'],param['t3'],param['t4'],param['t5'],param['t6']),
           is_quarterly=False)
    
    return alpha67