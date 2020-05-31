
from numpy import *

num_mobile = 10
num_users = 5

ratings = random.randint(11, size = (num_mobile, num_users))
print (ratings)

did_rate = (ratings != 0) * 1
print (did_rate)
print (ratings != 0)

ratings.shape
did_rate.shape

user_ratings = zeros((num_mobile, 1))
print (user_ratings)

user_ratings[0] = 8
user_ratings[4] = 7
user_ratings[7] = 3

print (user_ratings)

ratings = append(user_ratings, ratings, axis = 1)
did_rate = append(((user_ratings != 0) * 1), did_rate, axis = 1)

print (ratings)

ratings.shape
did_rate
print (did_rate)

did_rate.shape

a = [10, 20, 30]
aSum = sum(a)
print (aSum)

aMean = aSum / 3
print (aMean)

aMean = mean(a)
print (aMean)

a = [10 - aMean, 20 - aMean, 30 - aMean]
print (a)

print (ratings)

def normalize_ratings(ratings, did_rate):
    num_mobile = ratings.shape[0]

    ratings_mean = zeros(shape = (num_mobile, 1))
    ratings_norm = zeros(shape = ratings.shape)

    for i in range(num_mobile):
        idx = where(did_rate[i] == 1)[0]
        ratings_mean[i] = mean(ratings[i, idx])
        ratings_norm[i, idx] = ratings[i, idx] - ratings_mean[i]

    return ratings_norm, ratings_mean

ratings, ratings_mean = normalize_ratings(ratings, did_rate)

num_users = ratings.shape[1]
num_features = 3

X = array([[1, 2], [1, 5], [1, 9]])
Theta = array([[0.23], [0.34]])
print (X)
print (Theta)

Y = X.dot(Theta)
print (Y)

movie_features = random.randn( num_mobile, num_features )
user_prefs = random.randn( num_users, num_features )
initial_X_and_theta = r_[movie_features.T.flatten(), user_prefs.T.flatten()]

print (movie_features)

print (user_prefs)

print (initial_X_and_theta)

initial_X_and_theta.shape


movie_features.T.flatten().shape


user_prefs.T.flatten().shape


initial_X_and_theta


def unroll_params(X_and_theta, num_users, num_mobile, num_features):
	# Retrieve the X and theta matrixes from X_and_theta, based on their dimensions (num_features, num_mobile, num_mobile)
	# --------------------------------------------------------------------------------------------------------------
	# Get the first 30 (10 * 3) rows in the 48 X 1 column vector
	first_30 = X_and_theta[:num_mobile * num_features]
	# Reshape this column vector into a 10 X 3 matrix
	X = first_30.reshape((num_features, num_mobile)).transpose()
	# Get the rest of the 18 the numbers, after the first 30
	last_18 = X_and_theta[num_mobile * num_features:]
	# Reshape this column vector into a 6 X 3 matrix
	theta = last_18.reshape(num_features, num_users ).transpose()
	return X, theta

def calculate_gradient(X_and_theta, ratings, did_rate, num_users, num_mobile, num_features, reg_param):
	X, theta = unroll_params(X_and_theta, num_users, num_mobile, num_features)

	# we multiply by did_rate because we only want to consider observations for which a rating was given
	difference = X.dot( theta.T ) * did_rate - ratings
	X_grad = difference.dot( theta ) + reg_param * X
	theta_grad = difference.T.dot( X ) + reg_param * theta

	# wrap the gradients back into a column vector
	return r_[X_grad.T.flatten(), theta_grad.T.flatten()]


def calculate_cost(X_and_theta, ratings, did_rate, num_users, num_mobile, num_features, reg_param):
	X, theta = unroll_params(X_and_theta, num_users, num_mobile, num_features)

	# we multiply (element-wise) by did_rate because we only want to consider observations for which a rating was given
	cost = sum( (X.dot( theta.T ) * did_rate - ratings) ** 2 ) / 2
	# '**' means an element-wise power
	regularization = (reg_param / 2) * (sum( theta**2 ) + sum(X**2))
	return cost + regularization

# import these for advanced optimizations (like gradient descent)

from scipy import optimize

# regularization paramater

reg_param = 30

# perform gradient descent, find the minimum cost (sum of squared errors) and optimal values of X (movie_features) and Theta (user_prefs)

minimized_cost_and_optimal_params = optimize.fmin_cg(calculate_cost, fprime=calculate_gradient, x0=initial_X_and_theta, 								args=(ratings, did_rate, num_users, num_mobile, num_features, reg_param), 								maxiter=100, disp=True, full_output=True )

cost, optimal_movie_features_and_user_prefs = minimized_cost_and_optimal_params[1], minimized_cost_and_optimal_params[0]

# unroll once again

movie_features, user_prefs = unroll_params(optimal_movie_features_and_user_prefs, num_users, num_mobile, num_features)

print (movie_features)

print (user_prefs)

# Make some predictions (movie recommendations). Dot product

all_predictions = movie_features.dot( user_prefs.T )


print (all_predictions)

# add back the ratings_mean column vector to my (our) predictions

predictions_for_user = all_predictions[:, 0:1] + ratings_mean

print (predictions_for_user)

print (user_ratings)
