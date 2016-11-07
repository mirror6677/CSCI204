import math

class DTNode:
    def __init__(self):
        self.data = None
        self.children = []
        self.edges = []
        self.childrenCount = []  # number of documents that have this attribute

class DecisionTree:
    def __init__(self, twoDlist, oneDlist, depth):
        self.root = self.train(twoDlist, oneDlist, depth)
        self.oneDlist = oneDlist

    def train(self, twoDlist, oneDlist, depth):
        if len(twoDlist) == 0:
            return False

        for i in range(len(twoDlist)-1):
            if twoDlist[i][0] != twoDlist[i+1][0]:
                break
            elif i == len(twoDlist) - 2:
                node = DTNode()
                node.data = twoDlist[i][0]
                return node

        if len(oneDlist) == 1:
            authorDict = {}
            for i in range(len(twoDlist)):
                if authorDict.get(twoDlist[i][0]) == None:
                    authorDict[twoDlist[i][0]] = 1
                else:
                    authorDict[twoDlist[i][0]] += 1

            maxFreq = [None, 0]
            for j in authorDict:
                if authorDict[j] > maxFreq[1]:
                    maxFreq = [j, authorDict[j]]
            node = DTNode()
            node.data = maxFreq[0]
            return node

        minIndex, attrDict = calculation(oneDlist, twoDlist)
        node = DTNode()
        node.data = oneDlist[minIndex]
        curAttr = []
        for attrType in attrDict:
            node.edges.append(attrType)
            node.childrenCount.append(attrDict[attrType][0])

        for i in twoDlist:
            curAttr.append(i[minIndex])

        oneDlist = oneDlist[0:minIndex] + oneDlist[minIndex+1:]
        for row in range(len(twoDlist)):
            twoDlist[row] = twoDlist[row][0:minIndex] + twoDlist[row][minIndex+1:]

        for edge in node.edges:
            new2Dlist = []
            for i in range(len(twoDlist)):
                if curAttr[i] == edge:
                    new2Dlist.append(twoDlist[i])
            node.children.append(self.train(new2Dlist,oneDlist,depth-1))

        return node

    def eval(self, twoDlist):
        for row in range(len(twoDlist)):
            runner = self.root
            while runner.children != []:
                decision = twoDlist[row][self.oneDlist.index(runner.data)]
                index = runner.edges.index(decision)
                runner = runner.children[index]
            twoDlist[row][0] = runner.data

        return twoDlist




def getDif(twoDlist, attrCol):
    #attrDict是attrCOl这一列有几个不同的东西如small，medium，large
    #attrDict【small】中有个{}记录small的个数和一个{}，在small情况下有几个yes, no, ave等
    attrDict = {}
    for i in range(len(twoDlist)):
        if attrDict.get(twoDlist[i][attrCol]) == None:
            attrDict[twoDlist[i][attrCol]] = [1, {}]
            attrDict[twoDlist[i][attrCol]][1][twoDlist[i][0]] = 1

        else:
            attrDict[twoDlist[i][attrCol]][0] += 1
            if attrDict[twoDlist[i][attrCol]][1].get(twoDlist[i][0]) == None:
                attrDict[twoDlist[i][attrCol]][1][twoDlist[i][0]] = 1
            else:
                attrDict[twoDlist[i][attrCol]][1][twoDlist[i][0]] += 1

    entropyList = []
    for attrType in attrDict:
        entropy = 0
        entire = attrDict[attrType][0]
        for targetType in attrDict[attrType][1]:
            entropy -= attrDict[attrType][1][targetType] / entire * math.log(attrDict[attrType][1][targetType] / entire, 2)
        entropyList.append(entropy*entire/len(twoDlist))
    return sum(entropyList), attrDict

def main():
    twoDlist = [['no', 'small'], ['no', 'small'], ['yes', 'small'], ['yes', 'medium'], ['yes', 'large'], ['no', 'medium'], ['no', 'large'], ['no', 'large'], ['yes', 'medium'], ['yes', 'large'], ['no', 'small'], ['no', 'small'], ['no', 'small'], ['no', 'medium'], ['no', 'medium']]

    print(getDif(twoDlist, 1))



def calculation(oneDlist, twoDlist):
    minIndex = 1
    minEntropy, attrDict = getDif(twoDlist, minIndex)
    for col in range(2, len(oneDlist)):
        currentEntropy, a = getDif(twoDlist, col)
        if currentEntropy < minEntropy:
            minIndex = col
            minEntropy = currentEntropy
            attrDict = a
    return minIndex, attrDict
