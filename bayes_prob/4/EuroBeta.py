from bayes_prob.lib.thinkbayes import Beta
import matplotlib.pyplot as plt
import numpy as np
beta = Beta()
beta.Update((140, 110))
print(beta.Mean())

X = np.array(range(0, 101))/100
Y = [beta.EvalPdf(x) for x in X]

plt.plot(X, Y)
plt.show()