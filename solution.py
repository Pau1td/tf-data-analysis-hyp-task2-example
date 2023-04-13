import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import pareto, cauchy, norm, ttest_ind, ks_2samp, mannwhitneyu, permutation_test # нужен новый scipy

chat_id = 278913153 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы

    pval_tz = 0.03
    alternative = 'less'  
    pval = ks_2samp(x, y, alternative="two-sided", method='auto').pvalue
    #print(1-pval)


    if pval <= 1-pval_tz:
      return True
    else:
      return False
