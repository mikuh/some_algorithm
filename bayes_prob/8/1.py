import urllib.request as urllib2
import csv

class TrainSpotting(object):
    """Represents one observation of a train."""

    def __init__(self, t):
        self.timestamp = int(t[0])
        self.tripid = t[2]
        self.seconds = int(t[6])

def ReadCsv(url = 'http://developer.mbta.com/lib/rthr/red.csv'):
    """Reads data from the red line.
    Returns: list of TrainSpotting objects
    """
    fp = urllib2.urlopen(url)
    print(fp.read())
    # reader = csv.reader(fp)
    #
    # tss = []
    # for t in reader:
    #     if t[5] != 'Kendall/MIT': continue
    #     if t[3] != 'Braintree': continue
    #
    #     ts = TrainSpotting(t)
    #     tss.append(ts)
    #
    # fp.close()
    # return tss


ReadCsv()
# print(tss)