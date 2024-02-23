from random import random
from numpy.random import random_sample
from time import perf_counter

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

    x = random_sample(size = NUM_POINTS)
    y = random_sample(size = NUM_POINTS)
    points = zip(x,y)

    # Check if points are within circle
    circle = 0
    for point in points:
        if point[0] ** 2 + point[1] ** 2 <= 1:
            circle += 1

    pi = (circle / NUM_POINTS) * 4

    return pi

def main():

    NUM_SAMPLES = 10000000

    start_time = perf_counter()
    pi = calculatePi(NUM_SAMPLES)
    end_time = perf_counter()
    print(f"Approximated value of pi: {pi}")
    print(f"Calculated with {NUM_SAMPLES} samples in {end_time-start_time} seconds without numpy")

    start_time = perf_counter()
    pi = calculatePiWithNumpy(NUM_SAMPLES)
    end_time = perf_counter()
    print(f"Approximated value of pi: {pi}")
    print(f"Calculated with {NUM_SAMPLES} samples in {end_time-start_time} seconds with numpy")

if __name__ == "__main__":
    main()