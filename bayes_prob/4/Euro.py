from bayes_prob.lib.thinkbayes import Suite, Percentile, CredibleInterval

class Euro(Suite):
    def Likelihood(self, data, hypo):
        if data == 'H':
            return hypo/100.0
        else:
            return 1-hypo/100.0


suite = Euro(range(0, 101))
dataset = 'H'*140 + 'T'*110

for data in dataset:
    suite.Update(data)

suite.Show()

print("MaximumLikelihood P(H)", suite.MaximumLikelihood())
print("Mean", suite.Mean())
print("Median", Percentile(suite, 50))
print("CI", CredibleInterval(suite, 90))


print("P(H)=0.5", suite.Prob(50))


def TrianglePrior():
    suite = Euro()
    for x in range(0, 51):
        suite.Set(x, x)
    for x in range(51, 101):
        suite.Set(x, 100 - x)
    suite.Normalize()
    return suite

suite = TrianglePrior()
dataset = 'H'*140 + 'T'*110

for data in dataset:
    suite.Update(data)

suite.Show()

print("MaximumLikelihood P(H)", suite.MaximumLikelihood())
print("Mean", suite.Mean())
print("Median", Percentile(suite, 50))
print("CI", CredibleInterval(suite, 90))


print("P(H)=0.5", suite.Prob(50))
