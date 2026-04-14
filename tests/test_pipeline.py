import numpy as np

def test_array_shape():
    X = np.zeros((1, 38))
    assert X.shape == (1, 38)