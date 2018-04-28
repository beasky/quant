# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:42:04 2018

@author: dell
"""



def run_formula(dv, param = None):
    defult_param = {'t1':4,'t2':4,'t3':60,'t4':4,'t5':13,'t6':14}
    if not param:
        param = defult_param

    
    alpha64=dv.add_formula("alpha64",
                 '''(Max(Rank(Decay_linear(Corr(Rank(vwap),Rank(volume),%s),%s)),
                 Rank(Decay_linear(Max(Corr(Rank(close), Rank(Ts_Mean(volume,%s)), %s), %s), %s))) * -1)'''
                 %(param['t1'],param['t2'],param['t3'],param['t4'],param['t5'],param['t6']),
                 is_quarterly=False,)
    return alpha64