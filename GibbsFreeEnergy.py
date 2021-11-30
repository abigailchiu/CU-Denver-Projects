#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:12:14 2021

@author: abbychiu

Copyright (c) <2021-present>, <The Regents of the University of Colorado> All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Redistributions and uses must be recognized by Cathy Tran and Abigail Chiu. You must publish your results in a public domain with a proper citation to this program (e.g. journal articles, BioMagResBank, PDB).

4. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY COPYRIGHT HOLDER AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
IN NO EVENT SHALL COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
import sys #lets us access system-specifc parameters and function

def delta_G(H,T,S):
    G = H - (T*S) #delta G = deltaH(enthalpy) - T(K)deltaS (entropy)
    return G

try:
    user_delta_H = input("Input the value of delta H (change in enthalpy) with units (e.g. 1 kJ/mol). ")
    user_delta_H = user_delta_H.split()
    user_delta_H_value = float(user_delta_H[0])
except:
    print('The input format is incorrect. Please input like this "1 kJ/mol".')
    sys.exit()

try:
    user_temp = input("Input the value of temperature in Kelvin. ")
    user_temp = user_temp.split()
    user_temp_value = float(user_temp[0])
except:
    print('The input format is incorrect. Please input like this "1 K".')
    sys.exit()

try:
    user_delta_S = input("Input the value of delta S (change in entropy) with the units match delta H/K*mol ")
    user_delta_S = user_delta_S.split()
    user_delta_S_value = float(user_delta_S[0])
except:
    print('The input format is incorrect. Please input like this "1 kJ/K*mol".')
    sys.exit()

user_delta_G = delta_G(user_delta_H_value, user_temp_value, user_delta_S_value)

print('The calculated delta G is {:.2f}'.format(user_delta_G) + ' ' + user_delta_H[1])
# f means float '.2' means 2 digits after the decimal point

if user_delta_G < 0:
    print('The reaction is spontaneous.')
elif user_delta_G > 0:
    print('The reaction is nonspontaneous, and the reverse reaction is spontaneous.')
elif user_delta_G == 0:
    print('The reaction is in equilibrium.')




