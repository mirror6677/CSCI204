import decisionTree

def main():
    f = open('files.txt', 'r')
    f2 = open('files2.txt', 'r')
    text = f.readlines()
    text2 = f2.readlines()

    f.close()
    f2.close()

    aList = []
    for i in text:
        a = i.split()
        a[0] = a[0].split('.')[0]
        aList.append(a)
    bList = ['author', 'year', 'genre']

    dt = decisionTree.DecisionTree(aList, bList, 3)

    cList = []
    for j in text2:
        b = j.split()
        cList.append(b)

    print(dt.eval(cList))


main()
