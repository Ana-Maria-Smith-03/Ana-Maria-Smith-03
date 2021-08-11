import pandas as pd

df = pd.read_csv('WM_6-circular-foot.csv')

velocity_x = df[df.columns[1]]

velocity_values = velocity_x[352:591].values.astype('float64')

velocity_y = df[df.columns[2]]

velocity_y_values = velocity_y[352:591].values.astype('float64')


velocity_pairs = []
for num in range(len(velocity_values)):
    velocity_pairs.append([velocity_values[num], velocity_y_values[num]])

print(velocity_pairs)

force_x = df[df.columns[6]]

force_values = force_x[352:591].values.astype('float64')

force_y = df[df.columns[7]]

force_y_values = force_y[352:591].values.astype('float64')


force_pairs = []
for num in range(len(force_values)):
    force_pairs.append([force_values[num], force_y_values[num]])

print(force_pairs)

import argparse
from numpy import dot
from numpy.linalg import norm

from math import asin
import csv

def calculations(force, velocity):
    a = abs(dot(force, velocity))
    b = norm(force) * norm(velocity)
    phi = asin(a/b)
    print(phi)
    c = b * phi
    return {'b': b, 'c': c, 'phi': phi}


if __name__ == '__main__':
    c_values = []
    b_values = []
    phi_values = []

    for index, value in enumerate(force_pairs):
        force = force_pairs[index]
        velocity = velocity_pairs[index]
        results = calculations(force, velocity)
        c_values.append(results['c'])
        b_values.append(results['b'])
        phi_values.append(results['phi'])

    phi_df = pd.DataFrame(phi_values)

    phi_df.to_csv('phi_values_2_6-circ.csv')

    b_sum = 0
    for b_item in b_values:
        b_sum = b_sum + b_item

    c_sum = 0
    for c_item in c_values:
        c_sum = c_sum + c_item

    PHI = c_sum / b_sum

    print("This is PHI: " + str(PHI))

