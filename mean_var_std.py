import numpy as np

def calculate(list):
    try:
        twod_array = np.array(list, dtype=float).reshape(3,3)
    except ValueError:
        raise ValueError("List must contain nine numbers.")

    calculations = {
        #Calculating mean
        "mean": [
            np.mean(twod_array, axis=0).tolist(),
            np.mean(twod_array, axis=1).tolist(),
            np.mean(twod_array).item()
        ],
        #Calculating variance
        "variance": [
            np.var(twod_array, axis=0).tolist(),
            np.var(twod_array, axis=1).tolist(),
            np.var(twod_array).item()
        ],
        #calculating Standard deviation
        "standard deviation": [
            np.std(twod_array, axis=0).tolist(),
            np.std(twod_array, axis=1).tolist(),
            np.std(twod_array).item()
        ],
        #finding max
        "max": [
            np.max(twod_array, axis=0).tolist(),
            np.max(twod_array, axis=1).tolist(),
            np.max(twod_array).item()
        ],
        #finding min
        "min": [
            np.min(twod_array, axis=0).tolist(),
            np.min(twod_array, axis=1).tolist(),
            np.min(twod_array).item()
        ],
        #calculating sum
        "sum": [
            np.sum(twod_array, axis=0).tolist(),
            np.sum(twod_array, axis=1).tolist(),
            np.sum(twod_array).item()
        ]
    }
    return calculations