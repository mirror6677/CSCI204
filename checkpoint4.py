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

    prefix(dt.root)
    postfix(dt.root)

def prefix(root):
    if root == None:
        return

    else:
        try:
            f = open('prefix.txt', 'r')
            text = f.read()
            text += root.data + '\n'
            f.close()
        except:
            pass

        f = open('prefix.txt', 'w')

        try:
            f.write(text)
        except:
            f.write(root.data + '\n')

        f.close()

        for i in root.children:
            prefix(i)

def postfix(root):
    if root == None:
        return

    else:
        for i in root.children:
            postfix(i)

        try:
            f = open('postfix.txt', 'r')
            text = f.read()
            text += root.data + '\n'
            f.close()
        except:
            pass

        f = open('postfix.txt', 'w')

        try:
            f.write(text)
        except:
            f.write(root.data + '\n')

        f.close()

main()
