import sympy as sympy
from sympy.parsing.sympy_parser import parse_expr

from util import Diff


class GradientDescent(object):
    def_x0 = 2.0
    def_y0 = 6.0
    def_eps = 0.01
    def_f = '2*x**2+y**2-32*x-6*y'

    def __init__(self, f=def_f, start_point=None, eps=def_eps, find_min=True):
        if start_point is None:
            start_point = [self.def_x0, self.def_y0]
        self.__start_point = start_point
        self.__eps = eps
        self.__f = parse_expr(f)
        self.__findMin = find_min
        self.__vars = self.__get_vars()
        self.__grad = self.__grad()
        self.__calculated_grad = self.__calculate_grad()

    @staticmethod
    def calculate_f(f, variables, point):
        res = []
        for i in f:
            for j in range(len(variables)):
                i = i.subs(variables[j], point[j]).evalf()
            res.append(i)
        return res

    def calculate_diff_by_direction(self, length):
        return Diff.diff_by_direction(self.__calculated_grad, self.__start_point, length)

    def calculate(self):
        point = self.__start_point
        while True:
            if self.__findMin:
                x_k = [parse_expr(i) for i in min(self.__grad, self.__vars)]
            else:
                x_k = [parse_expr(i) for i in max(self.__grad, self.__vars)]
            print()
            print('X_k=', point)
            x_val = self.calculate_f(x_k, self.__vars, point)
            print('X_k+1=', x_val)
            grad_k = self.calculate_f(self.__grad, self.__vars, x_val)

            print('Grad_k+1=', grad_k)
            scalar = str(sum(self.__calculated_grad[i] * grad_k[i] for i in range(len(self.__grad))))
            print('Scalar=', scalar)
            l = sympy.Symbol('l')
            lamb = sympy.solve(parse_expr(scalar), [l])
            print('Lambda=', lamb)
            x_k = [i.subs(l, lamb[0]).evalf() for i in x_k]
            x_val = self.calculate_f(x_k, self.__vars, point)
            print('X_k+1=', x_val)
            grad_k = [grad_k[i].subs(l, lamb[0]).evalf() for i in range(len(grad_k))]
            new_grad = grad_k
            prev = point
            point = x_val
            if all(grad == 0 for grad in new_grad) or all(
                            abs(point[i] - prev[i]) < self.__eps for i in range(0, len(point), 2)):
                break

        print()
        print('Result:', point)

    def __get_vars(self):
        return list(sorted(self.__f.free_symbols, key=lambda s: s.sort_key()))

    def __grad(self):
        return [self.__f.diff(i) for i in self.__vars]

    def __calculate_grad(self):
        return self.calculate_f(self.__grad, self.__vars, self.__start_point)

    def __max(self):
        return [str(self.__vars[i]) + '+l*(' + str(self.__grad[i]) + ')' for i in range(len(self.__vars))]

    def __min(self):
        return [str(self.__vars[i]) + '-l*(' + str(self.__grad[i]) + ')' for i in range(len(self.__vars))]

    def get_grad(self):
        return self.__grad

    def get_calculated_grad(self):
        return self.__calculated_grad

    def get_vars(self):
        return self.__vars

    def get_f(self):
        return self.__f

    def get_start_point(self):
        return self.__start_point

    def get_eps(self):
        return self.__eps

    def is_min(self):
        return self.__findMin
