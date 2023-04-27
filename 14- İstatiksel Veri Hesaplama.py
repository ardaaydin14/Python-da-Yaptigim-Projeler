import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

n = 30  #length of data set
random_array = np.random.rand(n)  #creating random variables

plt.hist(random_array)
plt.show()

mean = np.mean(random_array)  #mean
variance = np.var(random_array)  #variance
mode = np.argmax(np.bincount(random_array.astype(int)))  #mode
median = np.median(random_array)  #median
std = np.std(random_array)  #standart deviation

z_score = (random_array - mean) / std  #calculated z scores
sorted_z_score = np.sort(z_score)  # ranked z scores
cumulative_probs = norm.cdf(z_score)  #calculated cumulative probabilities

#Scatterplot of the ordered Z-Values
plt.plot(sorted_z_score, cumulative_probs, 'bo', markersize=5)
plt.xlabel("Z scores")
plt.ylabel("Cumulative Probabilities")
plt.title("Cumulative Probability Plot of the Standard Normal Distribution")
plt.show()

print("Mean:", mean)
print("Variance:", variance)
print("Mode:", mode)
print("Median:", median)
print("Z score:", z_score)
print("Sorted Z scores:", sorted_z_score)
for i in range(len(random_array)):
    print(f"Z score: {z_score[i]:.2f}, Cumulative Probability: {cumulative_probs[i]:.4f}")