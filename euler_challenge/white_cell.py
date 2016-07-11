import math
import matplotlib.pyplot as plt
import numpy as np


def slope_tang(x, y):
    return 4 * x / y


def reflect(x0, y0, x1, y1):
    # Find the slope of the tangent and it's negative recipricol
    slope_tangent = slope_tang(x1, y1)
    # slope_neg_rec_tan = -1 * slope_tangent**-1

    slope_inc = (y1 - y0) / (x1 - x0)

    # tan(a-b) = (a-b)/(1+a*b)
    inc_angle = (slope_inc - slope_tangent) / (1 + slope_inc * slope_tangent)
    # find the angle between neg rec and incidence angle
    slope_ref = (inc_angle - slope_tangent) / (1 + inc_angle * slope_tangent)
    intercept_ref = y1 - slope_ref * x1
    print slope_ref, intercept_ref
    # print slope_ref, intercept_ref
    # Solve quadratic equation with new reflected line
    # 2b +- sqrt(b**2 - 4ac)/2a: b = slope*intercept, a = slope**2, c =
    # intercept**2 - 100
    a = 4 + slope_ref * slope_ref
    b = 2 * slope_ref * intercept_ref
    c = intercept_ref * intercept_ref - 100
    print a, b, c, math.sqrt(b * b - 4 * a * c)
    res_a = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    res_b = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    print "Sols ", res_a, res_b
    return res_a, res_b, slope_ref, intercept_ref


x0, y0 = 0.0, 10.1
x1, y1 = 1.4, -9.6
result = 0
y_end = math.sqrt(100 - 4 * 0.01**2)
# print x1, y1
plt_x = np.linspace(-5, 5, 500)
neg_y = -np.sqrt(100 - 4 * plt_x**2)
pos_y = np.sqrt(100 - 4 * plt_x**2)
plt.figure()
plt.plot(plt_x, neg_y)
plt.plot(plt_x, pos_y)
plt.plot([x0, x1], [y0, y1])
plt.axis([-10, 10, -10, 10])
while not ((x1 >= -0.01 and x1 <= 0.01) and y1 > y_end):
    res_a, res_b, slope, intercept = reflect(x0, y0, x1, y1)
    # print res_a, res_b, x1, slope, intercept
    x0, y0 = x1, y1
    temp1 = abs(res_a - x0)
    temp2 = abs(res_b - x0)
    x1 = res_a * (temp1 > temp2) + res_b * (temp2 > temp1)
    y1 = slope * x1 + intercept

    print "Points ", x0, y0, x1, y1
    result += 1
    plt.plot([x0, x1], [y0, y1])
    plt.show()
    if result == 3:
        break

print result
