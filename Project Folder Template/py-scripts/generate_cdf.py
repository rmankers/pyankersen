
import numpy as np
def generate_cdf(input_array):

    sorted_array = np.sort(input_array)
    cdf_array = np.array(range(len(sorted_array))) / float(len(sorted_array))

    # Returns a sorted x array and the CDF array
    return sorted_array, cdf_array