from bayes_prob.lib.thinkbayes import Suite

class Dice(Suite):
    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0 / hypo



if __name__ == '__main__':
    suite = Dice([4, 6, 8, 12, 20])

    suite.Update(6)
    suite.Print()


    for roll in [6, 8, 7, 7, 5, 4]:
        suite.Update(roll)

    suite.Print()