# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:33:59 2018

@author: dell
"""


def run_formula(dv, param = None):
    defult_param = {'t1':3,'t2':6,'t3':12,'t4':24}
    if not param:
        param = defult_param
    
    BondsPayableToAsset = dv.add_formula('BondsPayableToAsset', 
           '''bonds_payable/tot_assets''',
           is_quarterly=False)
    
    return BondsPayableToAsset