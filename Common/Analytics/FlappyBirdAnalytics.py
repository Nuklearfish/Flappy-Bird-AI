import statistics

class Analytics:

    def __init__(self):
        self.scores = []
        self.prependNewlineOnPrint = True

    def saveRun(self, score):
        self.scores.append(score)

    def setNewlinePrint(self, shouldPrepend):
        self.prependNewlineOnPrint = shouldPrepend

    def opN(self):
        return '\n' if self.prependNewlineOnPrint else ''

    def printRunCount(self):
        print(self.opN() + 'Run count: {}'.format(len(self.scores)))
    
    def printLastRun(self):
        print(self.opN() + 'Score from latest run: {}'.format(self.scores[-1]))

    def printWorstRun(self):
        print(self.opN() + 'Worst run: {}'.format(min(self.scores)))
    
    def printBestRun(self):
        print(self.opN() + 'Best run: {}'.format(max(self.scores)))
    
    def printMeanValue(self):
        print(self.opN() + 'Mean value of all runs: {}'.format(statistics.fmean(self.scores)))

    def printAllRuns(self):
        for i, score in enumerate(self.scores):
            print(self.opN() + 'Run #{}: {}'.format(i, score))
    
