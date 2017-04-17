import json

event_dict = dict()
type_dict = dict()


initial_Money = 0
final_Money = 0
numOfUpgrades = 0
towerCount = dict()
monsterKilled = dict()
monsterKilledLastSeg = dict()
totZoombies = 0
def read_game_statistics(filename):
    json_data = open(filename).read()
    json_data = json_data.rstrip(',')
    if json_data[0] != "[":
        json_data = "[" + json_data + "]"

    data = json.loads(json_data)

    return data

def parse_json(game_data):
    global totZoombies
    global initial_Money
    global final_Money
    global numOfUpgrades
    global towerCount
    global monsterKilled
    global monsterKilledLastSeg
    for event in game_data:
        event_key = event["Event"]
        type_key = event["Type"]
        if "Generated" == event_key:
             totZoombies += event["Num"]

        if event_key not in event_dict:
            event_dict[event_key] = []
        event_dict[event_key].append(event)

        if type_key not in type_dict:
            type_dict[type_key] = []
        type_dict[type_key].append(event)

    #print event_dict
    if 'GameStart' in event_dict:
        initial_Money = event_dict['GameStart'][0]['FinalMoney']

    if 'GameEnd' in event_dict:
        final_Money = event_dict['GameEnd'][0]['FinalMoney']

    if 'Upgraded' in event_dict:
        numOfUpgrades = len(event_dict['Upgraded'])

    if 'Built' in event_dict:
        built_array = event_dict['Built']
        for b in built_array:
            key =b['TowerIndex']
            if key in towerCount:
                towerCount[key] +=1
            else:
                towerCount[key] = 1

    if 'Killed' in event_dict:
        killed_array = event_dict['Killed']
        for z in killed_array:
            if z['MonsterIndex'] in monsterKilled:
                monsterKilled['MonsterIndex'] += 1
            else:
                monsterKilled['MonsterIndex'] = 1

            if z['DistanceLeft'] <= 4:
                if z['MonsterIndex'] in monsterKilledLastSeg:
                    monsterKilledLastSeg['MonsterIndex'] += 1
                else:
                    monsterKilledLastSeg['MonsterIndex'] = 1

def getData(filename):
    data = read_game_statistics(filename)
    parse_json(data)
    '''
    print initial_Money
    print final_Money
    print numOfUpgrades
    print(towerCount)
    print(monsterKilled)
    print monsterKilledLastSeg
    print totZoombies
    '''
    row = []
    row.append(initial_Money)
    row.append(final_Money)
    row.append(totZoombies)
    totmonsterkilled = 0
    totmonsterkilledlastseg = 0
    totTowerCount = 0
    for k,v in monsterKilled.iteritems():
        totmonsterkilled += int(v)
    for k,v in monsterKilled.iteritems():
        totmonsterkilledlastseg += int(v)
    for k,v in towerCount.iteritems():
        totTowerCount += int(v)
    row.append(totmonsterkilled)
    row.append(totmonsterkilledlastseg)
    row.append(numOfUpgrades)
    row.append(totTowerCount)

    return row
if __name__ == '__main__':
    row = getData('sample_log.json')




