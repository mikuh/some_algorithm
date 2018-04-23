from bayes_prob.lib.thinkbayes import Pdf, EstimatedPdf, Suite, MakeCdfFromList, GaussianPdf
import scipy.stats
import csv
import numpy
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

def ReadData(filename='showcases.2011.csv'):
    """Reads a CSV file of data.
    Args:
      filename: string filename
    Returns: sequence of (price1 price2 bid1 bid2 diff1 diff2) tuples
    """
    fp = open(filename)
    reader = csv.reader(fp)
    res = []

    for t in reader:
        _heading = t[0]
        data = t[1:]
        try:
            data = [int(x) for x in data]
            # print heading, data[0], len(data)
            res.append(data)
        except ValueError:
            pass

    fp.close()
    return zip(*res)

prices = ReadData()

showcase1, showcase2 = [], []
[(showcase1.append(price[0]), showcase2.append(price[1])) for price in prices]


def draw(showcase, label, color):
    pdf = EstimatedPdf(showcase)

    low, high = 0, 75000
    n = 101
    xs = numpy.linspace(low, high, n)
    pmf = pdf.MakePmf(xs)

    print(pmf.Items())
    X, Y = [], []
    [(X.append(x), Y.append(y))for x, y in sorted(pmf.Items())]
    plt.plot(X, Y, color=color, linewidth=1.0, linestyle="-", label=label)
    plt.legend(loc='upper right')


draw(showcase1, u'展品一价格分布', "blue")
draw(showcase2, u'展品二价格分布', "red")


plt.grid()
plt.show()

