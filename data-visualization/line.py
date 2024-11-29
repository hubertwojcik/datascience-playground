from matplotlib import pyplot as plt

# Line
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gpd = [300.2, 543.3,1075.9, 2862.5,5979.6,10289.7,14958.3]

# plt.plot(years, gpd, color="green", marker='o',linestyle='solid')

# plt.title("GPD")
# plt.ylabel("BLN dol.")
# plt.show()


# 
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared=[256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x,y in zip(variance,bias_squared)]
xs = [i for i,_ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-.',label='bias^2')
plt.plot(xs, total_error, "b:",label="total error")

plt.legend(loc=9)
plt.xlabel("Level of model complexity")
plt.title("Compromise between the threshold value and model complexity")
plt.show()