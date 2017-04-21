from flask import Flask, render_template, request, redirect, url_for

from descent import GradientDescent
from util import Diff

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.form['f']
        p = request.form['p']
        eps = request.form['eps']
        option = request.form['options']
        if not f or f.isspace():
            f = None
        if not p or p.isspace():
            p = None
        if not eps or eps.isspace():
            eps = None
        return redirect(url_for('calculate', f=f, start_point=p, eps=eps, option=option))
    return render_template('index.html',
                           def_f=GradientDescent.def_f,
                           def_p=str(GradientDescent.def_x0) + ' ' + str(GradientDescent.def_y0),
                           def_eps=GradientDescent.def_eps)


@app.route('/calculate')
def calculate():
    f = request.args.get('f')
    start_point = request.args.get('start_point')
    eps = request.args.get('eps')
    option = request.args.get('option')
    if start_point is not None:
        start_point = [float(x) for x in start_point.split()]
    if eps is not None:
        eps = float(eps)
    find_min = True
    if option == 'max':
            find_min = False
    descent = GradientDescent(f, start_point, eps, find_min)
    length = Diff.length(descent.get_start_point())
    diff_by_direction = descent.calculate_diff_by_direction(length)
    mess = 'not monotonically'
    if Diff.is_increasing(diff_by_direction):
        mess = 'monotonically increasing'
    if Diff.is_decreasing(diff_by_direction):
        mess = 'monotonically decreasing'
    res = descent.calculate()
    report = descent.get_report()
    return render_template('index.html',
                           descent=descent,
                           point=' '.join(map(str, descent.get_start_point())),
                           length=length,
                           diff_by_direction=diff_by_direction,
                           mess=mess, report=report, res='; '.join(map(str, res)))


if __name__ == '__main__':
    app.run()
