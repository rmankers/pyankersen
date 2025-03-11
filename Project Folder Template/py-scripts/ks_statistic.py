from scipy import stats 

sample1 = [1,2,3,4,5]
sample2 = [6,7,8,9,10]


ks_statistic,p_value = stats.ks_2samp(x1,x2)

print('KS Statistic', ks_statistic)
print("p-value",p_value)