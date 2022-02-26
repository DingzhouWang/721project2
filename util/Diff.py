from math import *


class Diff(object):
    @staticmethod
    def length(start_point):
        return sqrt(sum([i ** 2 for i in start_point]))

    @staticmethod
    def diff_by_direction(grad, point, length):
        return 1 / length * sum(point[i] * grad[i] for i in range(len(grad)))

    @staticmethod
    def is_increasing(diff):
        return diff > 0

    @staticmethod
    def is_decreasing(diff):
        return diff < 0
#