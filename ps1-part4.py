priorArrests = (int)(input('Prior arrests: '))
localOrdinanceArrests = (input('Prior arrests for local ordinance (Y/N): '))
releaseAge = (int)(input('Age at release: '))

recidivismRisk = 0
if priorArrests >= 2:
    recidivismRisk += 1
if priorArrests >= 5:
    recidivismRisk += 1
if localOrdinanceArrests == 'Y':
    recidivismRisk += 1
if releaseAge >= 18 and releaseAge <= 24:
    recidivismRisk += 1
if releaseAge >= 40:
    recidivismRisk -= 1

print(f'The recidivism risk score is {recidivismRisk}')