# Birthday Plots

import ex35
from bokeh.plotting import figure, show, output_file


if __name__ == '__main__':
    month_names = list(ex35.create_months().values())
    counted = ex35.count_birthday_months()

    output_file("plot.html")
    p = figure(x_range=month_names)
    p.vbar(x=list(counted), top=list(counted.values()), width=0.4)

    show(p)
