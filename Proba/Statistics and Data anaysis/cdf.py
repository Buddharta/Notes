import scipy.stats as stats

# Normal Distribution parmeters
mu = 985
sigma = 50

# Ordered sampled values
sample_values = [852, 875, 910, 933, 957, 963, 981, 998, 1010, 1015, 1018, 1023, 1035, 1048, 1063]

# CDF Values
cdf_sample_values = stats.norm.cdf(sample_values, loc=mu, scale=sigma)

# Print results
for value, cdf in zip(sample_values, cdf_sample_values):
    print(f"Valor: {value}, CDF: {cdf}")

