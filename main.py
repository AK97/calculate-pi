from random import random
import matplotlib.pyplot as plt
import numpy as np
import time

def calculatePi(n: int) -> float:
    NUM_POINTS = n

    # Generate random points in square from [0,0] to [1,1]
    points = []

    for i in range(0, NUM_POINTS):
        points.append((random(), random()))

    x, y = zip(*points)

    # Check if points are within circle
    circle = 0
    for point in points:
        if point[0] ** 2 + point[1] ** 2 <= 1:
            circle += 1

    pi = (circle / NUM_POINTS) * 4

    return pi

def calculatePiWithNumpy(n: int) -> float:
    NUM_POINTS = n

    # Generate random points in square from [0,0] to [1,1]
    points = []

    x = np.random.random_sample(size = NUM_POINTS)
    y = np.random.random_sample(size = NUM_POINTS)
    points = zip(x,y)

    # Check if points are within circle
    circle = 0
    for point in points:
        if point[0] ** 2 + point[1] ** 2 <= 1:
            circle += 1

    pi = (circle / NUM_POINTS) * 4

    return pi

NUM_SAMPLES = 10000000

start_time = time.perf_counter()
pi = calculatePi(NUM_SAMPLES)
end_time = time.perf_counter()
print(f"Approximated value of pi: {pi}")
print(f"Calculated with {NUM_SAMPLES} samples in {end_time-start_time} seconds")

start_time = time.perf_counter()
pi = calculatePiWithNumpy(NUM_SAMPLES)
end_time = time.perf_counter()
print(f"Approximated value of pi: {pi}")
print(f"Calculated with {NUM_SAMPLES} samples in {end_time-start_time} seconds")