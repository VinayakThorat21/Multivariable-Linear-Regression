# To create a module that can be imported into other Jupyter Notebooks or Python modules
from sklearn.linear_model import LinearRegression as linreg
from sklearn.metrics import mean_squared_error as mse

import pandas as pd
import numpy as np

CHARLES = 2
ROOMS = 4
PTRATIO = 8

# Set features: applicable features only and target
features = pd.read_csv('load_boston.csv')
features = features.drop(['srnum', 'indus', 'age', 'medv'], axis = 1)

target = np.array([24. , 21.6, 34.7, 33.4, 36.2, 28.7, 22.9, 27.1, 16.5, 18.9, 15. ,
        18.9, 21.7, 20.4, 18.2, 19.9, 23.1, 17.5, 20.2, 18.2, 13.6, 19.6,
        15.2, 14.5, 15.6, 13.9, 16.6, 14.8, 18.4, 21. , 12.7, 14.5, 13.2,
        13.1, 13.5, 18.9, 20. , 21. , 24.7, 30.8, 34.9, 26.6, 25.3, 24.7,
        21.2, 19.3, 20. , 16.6, 14.4, 19.4, 19.7, 20.5, 25. , 23.4, 18.9,
        35.4, 24.7, 31.6, 23.3, 19.6, 18.7, 16. , 22.2, 25. , 33. , 23.5,
        19.4, 22. , 17.4, 20.9, 24.2, 21.7, 22.8, 23.4, 24.1, 21.4, 20. ,
        20.8, 21.2, 20.3, 28. , 23.9, 24.8, 22.9, 23.9, 26.6, 22.5, 22.2,
        23.6, 28.7, 22.6, 22. , 22.9, 25. , 20.6, 28.4, 21.4, 38.7, 43.8,
        33.2, 27.5, 26.5, 18.6, 19.3, 20.1, 19.5, 19.5, 20.4, 19.8, 19.4,
        21.7, 22.8, 18.8, 18.7, 18.5, 18.3, 21.2, 19.2, 20.4, 19.3, 22. ,
        20.3, 20.5, 17.3, 18.8, 21.4, 15.7, 16.2, 18. , 14.3, 19.2, 19.6,
        23. , 18.4, 15.6, 18.1, 17.4, 17.1, 13.3, 17.8, 14. , 14.4, 13.4,
        15.6, 11.8, 13.8, 15.6, 14.6, 17.8, 15.4, 21.5, 19.6, 15.3, 19.4,
        17. , 15.6, 13.1, 41.3, 24.3, 23.3, 27. , 50. , 50. , 50. , 22.7,
        25. , 50. , 23.8, 23.8, 22.3, 17.4, 19.1, 23.1, 23.6, 22.6, 29.4,
        23.2, 24.6, 29.9, 37.2, 39.8, 36.2, 37.9, 32.5, 26.4, 29.6, 50. ,
        32. , 29.8, 34.9, 37. , 30.5, 36.4, 31.1, 29.1, 50. , 33.3, 30.3,
        34.6, 34.9, 32.9, 24.1, 42.3, 48.5, 50. , 22.6, 24.4, 22.5, 24.4,
        20. , 21.7, 19.3, 22.4, 28.1, 23.7, 25. , 23.3, 28.7, 21.5, 23. ,
        26.7, 21.7, 27.5, 30.1, 44.8, 50. , 37.6, 31.6, 46.7, 31.5, 24.3,
        31.7, 41.7, 48.3, 29. , 24. , 25.1, 31.5, 23.7, 23.3, 22. , 20.1,
        22.2, 23.7, 17.6, 18.5, 24.3, 20.5, 24.5, 26.2, 24.4, 24.8, 29.6,
        42.8, 21.9, 20.9, 44. , 50. , 36. , 30.1, 33.8, 43.1, 48.8, 31. ,
        36.5, 22.8, 30.7, 50. , 43.5, 20.7, 21.1, 25.2, 24.4, 35.2, 32.4,
        32. , 33.2, 33.1, 29.1, 35.1, 45.4, 35.4, 46. , 50. , 32.2, 22. ,
        20.1, 23.2, 22.3, 24.8, 28.5, 37.3, 27.9, 23.9, 21.7, 28.6, 27.1,
        20.3, 22.5, 29. , 24.8, 22. , 26.4, 33.1, 36.1, 28.4, 33.4, 28.2,
        22.8, 20.3, 16.1, 22.1, 19.4, 21.6, 23.8, 16.2, 17.8, 19.8, 23.1,
        21. , 23.8, 23.1, 20.4, 18.5, 25. , 24.6, 23. , 22.2, 19.3, 22.6,
        19.8, 17.1, 19.4, 22.2, 20.7, 21.1, 19.5, 18.5, 20.6, 19. , 18.7,
        32.7, 16.5, 23.9, 31.2, 17.5, 17.2, 23.1, 24.5, 26.6, 22.9, 24.1,
        18.6, 30.1, 18.2, 20.6, 17.8, 21.7, 22.7, 22.6, 25. , 19.9, 20.8,
        16.8, 21.9, 27.5, 21.9, 23.1, 50. , 50. , 50. , 50. , 50. , 13.8,
        13.8, 15. , 13.9, 13.3, 13.1, 10.2, 10.4, 10.9, 11.3, 12.3,  8.8,
         7.2, 10.5,  7.4, 10.2, 11.5, 15.1, 23.2,  9.7, 13.8, 12.7, 13.1,
        12.5,  8.5,  5. ,  6.3,  5.6,  7.2, 12.1,  8.3,  8.5,  5. , 11.9,
        27.9, 17.2, 27.5, 15. , 17.2, 17.9, 16.3,  7. ,  7.2,  7.5, 10.4,
         8.8,  8.4, 16.7, 14.2, 20.8, 13.4, 11.7,  8.3, 10.2, 10.9, 11. ,
         9.5, 14.5, 14.1, 16.1, 14.3, 11.7, 13.4,  9.6,  8.7,  8.4, 12.8,
        10.5, 17.1, 18.4, 15.4, 10.8, 11.8, 14.9, 12.6, 14.1, 13. , 13.4,
        15.2, 16.1, 17.8, 14.9, 14.1, 12.7, 13.5, 14.9, 20. , 16.4, 17.7,
        19.5, 20.2, 21.4, 19.9, 19. , 19.1, 19.1, 20.1, 19.9, 19.6, 23.2,
        29.8, 13.8, 13.3, 16.7, 12. , 14.6, 21.4, 23. , 23.7, 25. , 21.8,
        20.6, 21.2, 19.1, 20.6, 15.2,  7. ,  8.1, 13.6, 20.1, 21.8, 24.5,
        23.1, 19.7, 18.3, 21.2, 17.5, 16.8, 22.4, 20.6, 23.9, 22. , 11.9])
target = pd.DataFrame(np.log(target), columns=['price'])

# Create a primary property stats variable to hold mean of all the above features at start
property_stats = features.mean().values.reshape(1, 11)

# Build a LinearRegression Model
regression = linreg().fit(features, target)
fitted_values = regression.predict(features)

# MSE and RMSE
model_mse = mse(target, fitted_values)
model_rmse = round(np.sqrt(model_mse), 3)

# Dependent constants
ZILLOW_MEDIAN_PRICE = 583.3
SCALE_FACTOR = ZILLOW_MEDIAN_PRICE / np.median(target)

# Function to return log price estimates
def log_price_estimates(
        number_of_rooms,
        students_per_class,
        near_river = False,
        high_confidence = True
):
    property_stats[0][ROOMS] = number_of_rooms
    property_stats[0][PTRATIO] = students_per_class

    if near_river:
        property_stats[0][CHARLES] = 1
    else:
        property_stats[0][CHARLES] = 0

    log_price_estimate = regression.predict(property_stats)[0][0]

    if high_confidence:
        upper_bound = log_price_estimate + 2 * model_rmse
        lower_bound = log_price_estimate - 2 * model_rmse
        interval = 95
    else:
        upper_bound = log_price_estimate + model_rmse
        lower_bound = log_price_estimate - model_rmse
        interval = 68
        
    return log_price_estimate, upper_bound, lower_bound, interval

# Function that returns actual price and range scaled up to today's home prices
def price_estimates(rooms, students_per_teacher = 21, near_river = False, scale_down_range = False):
    # Adding a quick Docs
    '''
        Estimates Price for the house in Boston\n
        All the inner parameters are mean from the training dataset\n

        Keywords\n
        rooms                   -- Number of Rooms\n
        students_per_teacher    -- Pupil-Teacher Ratio\n
        near_river              -- True if Near Charles river\n
        scale_down_range        -- True if more deviation from estimated price is allowed
    '''

    # Validation of values provided
    if rooms < 1 or students_per_teacher < 1 or students_per_teacher > 70:
        print('Values provided aren\'t realistic...')
        return
    
    estimate, upper, lower, interval = log_price_estimates(rooms, students_per_teacher, near_river=near_river, high_confidence=scale_down_range)

    # Scale up to actual values
    estimate = round(np.e ** estimate * SCALE_FACTOR * 1000, 3)
    upper = round(np.e ** upper * SCALE_FACTOR * 1000, 3)
    lower = round(np.e ** lower * SCALE_FACTOR * 1000, 3)

    return estimate, upper, lower, interval