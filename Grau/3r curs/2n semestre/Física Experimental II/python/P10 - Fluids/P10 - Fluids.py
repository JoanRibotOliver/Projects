# PROVA MEVA...

import matplotlib.pyplot as plt
import numpy as np

def adjust_exp_profile(x, y, start_index, end_index):
    # Fit an exponential curve to the selected data points
    log_y = np.log(y[start_index:end_index+1])
    coefficients = np.polyfit(x[start_index:end_index+1], log_y, deg=1)
    fitted_y = np.exp(np.polyval(coefficients, x))
    return fitted_y

# Read the data from the first text file
data1 = np.genfromtxt('Perfil_velocidades_Q10m3hora.txt', delimiter=',')
y1 = data1[:, 0]
x1 = data1[:, 1]
error1 = data1[:, 2]

# Read the data from the second text file
data2 = np.genfromtxt('Perfil_velocidades_Q15m3hora.txt', delimiter=',')
y2 = data2[:, 0]
x2 = data2[:, 1]
error2 = data2[:, 2]

# Read the data from the third text file
data3 = np.genfromtxt('Perfil_velocidades_Q30m3hora.txt', delimiter=',')
y3 = data3[:, 0]
x3 = data3[:, 1] + 3.5 # Shift x-coordinates by 3.5 units
error3 = data3[:, 2]

# Plot the first dataset
scatter1 = plt.errorbar(x1, y1, xerr=error1, fmt='o', label='Q = 10 m^3/s', markersize=3, capsize=3)

# Plot the second dataset
scatter2 = plt.errorbar(x2, y2, xerr=error2, fmt='o', label='Q = 15 m^3/s', markersize=3, capsize=3)

# Plot the third dataset
scatter3 = plt.errorbar(x3, y3, xerr=error3, fmt='o', label='Q = 30 m^3/s', markersize=3, capsize=3)

# DELTA
# Select the specific points to mark in each dataset
index1 = 14  # Index of the point in dataset 1
index2 = 17  # Index of the point in dataset 2
index3 = 12  # Index of the point in dataset 3

# Plot the marked points with bigger black dots and captions
plt.scatter(x1[index1], y1[index1], s=50, c='black', marker='o')
plt.text(x1[index1] - 0.4 , y1[index1], f'$\delta$', ha='left', va='center')

plt.scatter(x2[index2], y2[index2], s=50, c='black', marker='o')
plt.text(x2[index2] - 0.4 , y2[index2], f'$\delta$', ha='left', va='center')

plt.scatter(x3[index3], y3[index3], s=50, c='black', marker='o')
plt.text(x3[index3] - 0.4 , y3[index3], f'$\delta$', ha='left', va='center')

# DELTA* EXP
# Select the specific points to mark in each dataset
index7 = 4  # Index of the point in dataset 1
index8 = 4  # Index of the point in dataset 2
index9 = 6  # Index of the point in dataset 3

# Plot the marked points with bigger black dots and captions
plt.scatter(x1[index7], y1[index7], s=50, c='black', marker='o')
plt.text(x1[index7] - 0.6 , y1[index7], f'$\delta_e^*$', ha='left', va='center')

plt.scatter(x2[index8], y2[index8], s=50, c='black', marker='o')
plt.text(x2[index8] - 0.6 , y2[index8], f'$\delta_e^*$', ha='left', va='center')

plt.scatter(x3[index9], y3[index9], s=50, c='black', marker='o')
plt.text(x3[index9] - 0.6 , y3[index9], f'$\delta_e^*$', ha='left', va='center')

# Select the specific points to mark in each dataset
start_index1 = index7
end_index1 = index1

start_index2 = index8
end_index2 = index2

start_index3 = index9
end_index3 = index3

# Adjust the data points to the exponential speed profile
fitted_y1 = adjust_exp_profile(x1, y1, start_index1, end_index1)
fitted_y2 = adjust_exp_profile(x2, y2, start_index2, end_index2)
fitted_y3 = adjust_exp_profile(x3, y3, start_index3, end_index3)

# Plot the adjusted curves within the desired range
plt.plot(x1[start_index1:end_index1+1], fitted_y1[start_index1:end_index1+1], color='red', linestyle='--',
         label='Exponential Fit')
plt.plot(x2[start_index2:end_index2+1], fitted_y2[start_index2:end_index2+1], color='red', linestyle='--')
plt.plot(x3[start_index3:end_index3+1], fitted_y3[start_index3:end_index3+1], color='red', linestyle='--')

# Set labels and title
plt.xlabel('u (cm/s)')
plt.ylabel('y (cm)')
plt.title('Perfils de velocitats')

# Add gridlines
plt.grid(True)

# Format the exponent in the legend
#plt.legend(handles=[scatter1.lines[0], scatter2.lines[0], scatter3.lines[0]],
 #          labels=[r'Q = 10 $m^3/s$', r'Q = 15 $m^3/s$', r'Q = 30 $m^3/s$'])

# Format the exponent in the legend
plt.legend(handles=[scatter1.lines[0], scatter2.lines[0], scatter3.lines[0]], labels=[r'Q = 10 $m^3/s$', r'Q = 15 $m^3/s$', r'Q = 30 $m^3/s$'])

# Display the plot
plt.show()




