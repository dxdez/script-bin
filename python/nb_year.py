# This function uses a while loop to simulate the population growth until it reaches or surpasses the target population p. 
# It converts the percentage to a decimal by dividing it by 100 before using it in the calculations. The loop increments the number of years and updates the population each year based on the growth rate and the number of inhabitants coming or leaving.

import math

def nb_year(p0, percent, aug, p):
    years = 0
    percent = percent / 100  # Convert the percentage to a decimal

    while p0 < p:
        p0 += math.floor(p0 * percent) + aug
        years += 1

    return years

