import os
from random import randint
from sklearn.svm import SVC

import cPickle
import data_parsing
initialMoney = [200,250,300,350,400]
totZombies_l = 30
totZombies_h = 70
percentage_dead = 70
percentage_dead_last_seg = 40
noOfTowerUpgrades_l = 5
noOfTowerUpgrades_h = 15
noOfTower = [3,4]

fin_Money = 20
outputMatrix = []
funLevelOuput = []
difficultyLevelOutput = []
fun_level = [0,1,2,3,4,5,6,7,8,9]
diff_level = [0,1,2,3,4,5,6,7,8,9]
def getRow():
    res = []
    money_index = randint(0,4)
    iniMoney = initialMoney[money_index]
    #res.append(iniMoney)

    final_Money_Rand = randint(0,fin_Money)/100.0
    finalMoney = final_Money_Rand * iniMoney
    #res.append(int(finalMoney))
    res.append(final_Money_Rand)
    totZombies = randint(totZombies_l,totZombies_h)
    res.append(totZombies)

    noOfKilled = (100 - randint(percentage_dead,100))/100.0 * totZombies
    #res.append(int(noOfKilled))
    res.append((100 - randint(percentage_dead,100))/100.0)

    noOfKilled_lastSeg = (100 - randint(percentage_dead_last_seg,100))/100.0 * totZombies
    #res.append(int(noOfKilled_lastSeg))
    res.append((100 - randint(percentage_dead_last_seg,100))/100.0)

    noOfTowUpgrade = randint(noOfTowerUpgrades_l,noOfTowerUpgrades_h)
    res.append(noOfTowUpgrade)

    towInd = randint(0,1)
    noOfdiffTow = noOfTower[towInd]
    res.append(noOfdiffTow)

    return res

def getRow_Low():
    res = []
    money_index = randint(0,4)
    iniMoney = initialMoney[money_index]
    #res.append(iniMoney)

    final_Money_Rand = (100-randint(0,fin_Money))/100.0
    finalMoney = final_Money_Rand * iniMoney
    #res.append(int(finalMoney))

    res.append(final_Money_Rand)


    totZombies = randint(totZombies_l,totZombies_h)
    res.append(totZombies)

    noOfKilled = randint(percentage_dead,100)/100.0 * totZombies
    #res.append(int(noOfKilled))
    res.append(randint(percentage_dead,100)/100.0)

    noOfKilled_lastSeg = randint(percentage_dead_last_seg,100)/100.0 * totZombies
    #res.append(int(noOfKilled_lastSeg))
    res.append(randint(percentage_dead_last_seg,100)/100.0)

    noOfTowUpgrade = randint(0,5)
    res.append(noOfTowUpgrade)

    towInd = randint(0,1)
    noOfdiffTow = noOfTower[towInd]
    res.append(noOfdiffTow)

    return res

'''
for i in range(0,500,1):
    row = getRow()
    f_level_index = randint(0,len(fun_level)-1)
    _fun_level = fun_level[f_level_index]
    testLabel.append(_fun_level)
    testData.append(row)
'''

def classification():
    for i in range(0,1000,1):
        row = getRow()
        f_level_index = randint(6,len(fun_level)-1)
        _fun_level = fun_level[f_level_index]
        d_level_index = randint(6,len(fun_level)-1)
        _difficulty_level = diff_level[d_level_index]
        difficultyLevelOutput.append(_difficulty_level)
        funLevelOuput.append(_fun_level)
        outputMatrix.append(row)
    '''
    with open("output_high.txt","wb") as fid:
        for i in range(0,len(outputMatrix)-1):
            fid.write(str(outputMatrix[i]) + ":" + str(funLevelOuput[i]) + ":" + str(difficultyLevelOutput[i]) + "\n")
    '''
    for i in range(0,1000,1):
        row = getRow_Low()
        f_level_index = randint(0,5)
        _fun_level = fun_level[f_level_index]
        d_level_index = randint(0,5)
        _difficulty_level = diff_level[d_level_index]
        difficultyLevelOutput.append(_difficulty_level)
        funLevelOuput.append(_fun_level)
        outputMatrix.append(row)

    clf = SVC()
    clf.fit(outputMatrix, funLevelOuput)
    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
        decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
        max_iter=-1, probability=False, random_state=None, shrinking=True,
        tol=0.001, verbose=False)


    clf_diff = SVC()
    clf_diff.fit(outputMatrix, difficultyLevelOutput)
    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
        decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
        max_iter=-1, probability=False, random_state=None, shrinking=True,
        tol=0.001, verbose=False)

    with open('funlevel_classifier.pkl', 'wb') as fid:
        cPickle.dump(clf, fid)

    with open('difflevel_classifier.pkl', 'wb') as fid:
        cPickle.dump(clf_diff, fid)

def evaluate(filename):
    testData = []
    testData.append(data_parsing.getData(filename))
    if not os.path.exists('funlevel_classifier.pkl') or not os.path.exists('difflevel_classifier.pkl'):
        classification()
    with open('funlevel_classifier.pkl', 'rb') as fid:
        clf_fun = cPickle.load(fid)
    with open('difflevel_classifier.pkl', 'rb') as fid:
        clf_diff = cPickle.load(fid)
    '''

    for i in range(0,50,1):
        row = getRow()
        fun_level = clf_fun.predict(row)
        diff_level = clf_diff.predict(row)
        print fun_level[0], diff_level[0]
    print "getting low"
    for i in range(0,50,1):
        row = getRow_Low()
        fun_level = clf_fun.predict(row)
        diff_level = clf_diff.predict(row)
        print fun_level[0], diff_level[0]

    print "printing sample jsn"
    '''
    fun_level = clf_fun.predict(testData)
    diff_level = clf_diff.predict(testData)
    return fun_level[0], diff_level[0]
if __name__ == '__main__':
    print evaluate('sample_log.json')
