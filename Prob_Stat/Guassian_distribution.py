import scipy.stats as stats

# Parameters for the normal distribution
mu = 50     # mean
sigma = 5   # standard deviation
x = 60      # value of interest

# Calculate the z-score
z = (x - mu) / sigma

# Calculate the probability using the cumulative distribution function (CDF)
probability = 1 - stats.norm.cdf(z)

# Print the result
print(f"The probability that a randomly selected value is greater than 60 is: {probability:.4f}")