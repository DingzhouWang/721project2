from flask import Flask, render_template, request, redirect, url_for

from descent import GradientDescent
from util import Diff

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.form['f']
        p = request.form['p']
        if not f or f.isspace():
            f = None
        if not p or p.isspace():
            p = None
        return redirect(url_for('calculate', f=f, start_point=p))
    return render_template('index.html',
                           def_f=GradientDescent.def_f,
                           def_p=[GradientDescent.def_x0, GradientDescent.def_y0])


@app.route('/calculate')
@app.route('/calculate/<f>/<start_point>')
def calculate(f=None, start_point=None):
    if start_point is not None:
        start_point = [float(x) for x in start_point.split()]
    descent = GradientDescent(f, start_point)
    point = descent.get_start_point()
    length = Diff.length(point)
    diff_by_direction = descent.calculate_diff_by_direction(length)
    mess = 'not monotonically'
    if Diff.is_increasing(diff_by_direction):
        mess = 'monotonically increasing'
    if Diff.is_decreasing(diff_by_direction):
        mess = 'monotonically decreasing'
    descent.calculate()
    report = descent.get_report()
    return render_template('index.html',
                           descent=descent,
                           point=point,
                           length=length,
                           diff_by_direction=diff_by_direction,
                           mess=mess, report=report)


if __name__ == '__main__':
    app.run()
