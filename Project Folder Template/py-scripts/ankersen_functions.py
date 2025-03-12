from scipy import stats 
import numpy as np



# Two Sided KS statistic for testing Distribution Similarity
def ks_statistic(x1,x2)
    ks_statistic,p_value = stats.ks_2samp(x1,x2)

    return ks_statistic,p_value


# CDF array generation, returning a sorted input array, and associated CDF function. Useful for Plotting 
def generate_cdf(input_array):
    
    sorted_array = np.sort(input_array)
    sorted_array = sorted_array[~np.isnan(sorted_array)]
    cdf_array = np.array(range(len(sorted_array))) / float(len(sorted_array))

    # Returns a sorted x array and the CDF array
    return sorted_array, cdf_array