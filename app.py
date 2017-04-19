from flask import Flask, render_template, request, redirect, url_for

from descent import GradientDescent

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.form['f']
        p = request.form['p']
        start_point = [float(x) for x in p.split()]
        return redirect(url_for('calculate', f=f, start_point=start_point))
    return render_template('index.html',
                           def_f=GradientDescent.def_f,
                           def_p=[GradientDescent.def_x0, GradientDescent.def_y0])


@app.route('/calculate/<f>/<start_point>')
def calculate(f, start_point):
    descent = GradientDescent(f, start_point)
    return render_template('index.html',
                           descent=descent)

# print('Gradient:', grad)
# print('Calculated gradient: ', calculated_grad)
# print('Length: ', length)
# print('Diff by direction: ', diff)
# print('Function is monotonically increasing', self.__is_increasing(diff))
#         print('Function is monotonically decreasing', self.__is_decreasing(diff))

if __name__ == '__main__':
    app.run()
