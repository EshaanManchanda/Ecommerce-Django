# cython_modules/distance.pyx

import numpy as np
cimport numpy as np
from libc.math cimport sqrt

def cosine_similarity(np.ndarray[np.float32_t, ndim=1] v1, np.ndarray[np.float32_t, ndim=1] v2):
    """
    Calculate cosine similarity between two vectors.
    """
    cdef int i
    cdef float dot_product = 0.0
    cdef float norm_v1 = 0.0
    cdef float norm_v2 = 0.0
    
    for i in range(len(v1)):
        dot_product += v1[i] * v2[i]
        norm_v1 += v1[i] * v1[i]
        norm_v2 += v2[i] * v2[i]
    
    return dot_product / (sqrt(norm_v1) * sqrt(norm_v2))
