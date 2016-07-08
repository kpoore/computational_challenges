import math


def slope_tang(x, y):
    return 4 * x / y


def reflect(pos_ori, pos_fin):
    incident_vec = [pos_ori, pos_fin]
    # Find the slope of the tangent and it's negative recipricol
    slope_tangent = slope_tang(pos_fin[0], pos_fin[1])
    # slope_neg_rec_tan = -1 * slope_tangent**-1

    slope_inc = (pos_fin[1] - pos_ori[1]) / (pos_fin[0] - pos_ori[0])
    inc_angle = (slope_inc - slope_tangent) / (1 + slope_inc * slope_tangent)
    # find the angle between neg rec and incidence angle
    slope_ref = (slope_tangent - inc_angle) / (1 + inc_angle * slope_tangent)
    intercept_ref = pos_fin[1] - slope_ref * pos_fin[0]

    # Solve quadratic equation with new reflected line
    # 2b +- sqrt(b**2 - 4ac)/2a: b = slope*intercept, a = slope**2, c =
    # intercept**2 - 100
    a = 4 + slope_ref**2
    b = 2 * slope_ref * intercept_ref
    c = intercept_ref**2 - 100

    res_a = -2 * b + math.sqrt(b**b - 4 * a * c) / (2 * a)
    res_b = -2 * b - math.sqrt(b**b - 4 * a * c) / (2 * a)

    return res_a, res_b, slope_ref, intercept_ref


x0, y0 = 0.0, 10.1
x1, y1 = 1.4, -9.6
result = 0
while -0.01 <= x1 <= 0.01 and y1 > 0:
    res_a, res_b, slope, intercept = reflect([x0, y0], [x1, y1])

    x2 = max(math.abs(res_a - x1), math.abs(res_b - x1))
    y2 = slope * xO + intercept
    x0, y0 = x1, y1
    x1, y1 = x2, y2
    print x0, y0
    result += 1
