from random import randint
from sklearn.svm import SVC
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

fun_level = [6,7,8,9]
def getRow():
    res = []
    money_index = randint(0,4)
    iniMoney = initialMoney[money_index]
    res.append(iniMoney)

    final_Money_Rand = randint(0,fin_Money)/100.0
    finalMoney = final_Money_Rand * iniMoney
    res.append(int(finalMoney))

    totZombies = randint(totZombies_l,totZombies_h)
    res.append(totZombies)

    noOfKilled = randint(percentage_dead,100)/100.0 * totZombies
    res.append(int(noOfKilled))

    noOfKilled_lastSeg = randint(percentage_dead_last_seg,100)/100.0 * totZombies
    res.append(int(noOfKilled_lastSeg))

    noOfTowUpgrade = randint(noOfTowerUpgrades_l,noOfTowerUpgrades_h)
    res.append(noOfTowUpgrade)

    towInd = randint(0,1)
    noOfdiffTow = noOfTower[towInd]
    res.append(noOfdiffTow)

    return res

for i in range(0,5000,1):
    row = getRow()
    f_level_index = randint(0,len(fun_level)-1)
    _fun_level = fun_level[f_level_index]
    funLevelOuput.append(_fun_level)
    outputMatrix.append(row)

testData = []
testLabel =[]
'''
for i in range(0,500,1):
    row = getRow()
    f_level_index = randint(0,len(fun_level)-1)
    _fun_level = fun_level[f_level_index]
    testLabel.append(_fun_level)
    testData.append(row)
'''
testData.append(data_parsing.getData('sample_log.json'))
clf = SVC()
clf.fit(outputMatrix, funLevelOuput)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

#print(clf.predict([[testData, testLabel]]))
print testData
print clf.predict(testData)
