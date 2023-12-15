import numpy as np
import sys


def integral_view(image):
    height, width = image.shape
    integral = np.zeros((height, width), dtype=np.int32)

    for y in range(height):
        for x in range(width):
            if x == 0 and y == 0:
                integral[y, x] = image[y, x]
            elif x == 0:
                integral[y, x] = integral[y-1, x] + image[y, x]
            elif y == 0:
                integral[y, x] = integral[y, x-1] + image[y, x]
            else:
                integral[y, x] = integral[y-1, x] + integral[y, x-1] - integral[y-1, x-1] + image[y, x]

    return integral


def generate_integer_matrix(rows, columns):
    return np.random.randint(0, 256, size=(rows, columns), dtype=np.int32)

def rect_sum(integral_image, x1, y1, x2, y2):

    sum_a = integral_image[y1-1, x1-1]
    sum_b = integral_image[y1-1, x2]
    sum_c = integral_image[y2, x2]
    sum_d = integral_image[y2, x1-1]

    sum_of_rect = sum_a + sum_c - sum_b - sum_d

    return sum_of_rect