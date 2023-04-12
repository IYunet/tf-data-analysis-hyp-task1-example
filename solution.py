import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 426527714 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.02
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    standrart_error = ((p1*(1-p1))/x_cnt + (p2*(1-p2))/y_cnt)**0.5
    z = abs((p1 - p2) / standrart_error)
    critical_value = abs(norm.ppf(alpha/2))
    return z > critical_value
