# Directories

experimentType = 'Open'

BASE_PATH = '/home/marcos/ClasificadorEmotiv_MathiasGatti/'

IMGsDirSource = BASE_PATH + 'informe/IMGs/'
DatasetsDirSource = BASE_PATH + 'Datasets/'
IMGsDir = IMGsDirSource + experimentType + '/'
DatasetsDir = DatasetsDirSource + experimentType + '/'

# Metrics

metricasMatrix = ["pli", "plv", "coh",'cohy','imcoh','ppc','pli2_unbiased','wpli2_debiased']

# Distancies

lamda = 0.9

# Electrodes

biosemiLabels = ['C26', 'D6', 'C32', 'D11', 'D23', 'D31', 'A15', 'A28', 'B11', 'B26', 'B30', 'C10', 'C6', 'C13']
emotivLabels = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']

biosemi2emotiv = {0:8, 1:10, 2:9, 3:11, 4:12, 5:13, 6:0, 7:1, 8:2, 9:3, 10:4, 11:6, 12:5, 13:7}

electrodeDistances = {'AF3': {'AF3': 0.0,
  'AF4': 0.752,
  'F3': 0.35168309598273273,
  'F4': 0.9712677282809308,
  'F7': 0.6106978057926851,
  'F8': 1.2608282238274968,
  'FC5': 0.7467697101516638,
  'FC6': 1.3732068307432788,
  'O1': 1.8623567891250055,
  'O2': 1.9832066987583519,
  'P7': 1.565545211739348,
  'P8': 1.915115612698095,
  'T7': 1.4299611218491222,
  'T8': 1.4299611218491222},
 'AF4': {'AF3': 0.752,
  'AF4': 0.0,
  'F3': 0.9712677282809308,
  'F4': 0.35168309598273273,
  'F7': 1.2608282238274968,
  'F8': 0.6106978057926851,
  'FC5': 1.3732068307432788,
  'FC6': 0.7467697101516638,
  'O1': 1.9832066987583519,
  'O2': 1.8623567891250055,
  'P7': 1.915115612698095,
  'P8': 1.565545211739348,
  'T7': 1.8834236937025084,
  'T8': 1.8834236937025084},
 'F3': {'AF3': 0.35168309598273273,
  'AF4': 0.9712677282809308,
  'F3': 0.0,
  'F4': 1.09,
  'F7': 0.6026690717134903,
  'F8': 1.4583655268827496,
  'FC5': 0.5060395241480649,
  'FC6': 1.4768263269592672,
  'O1': 1.7250921743489536,
  'O2': 1.910382948521055,
  'P7': 1.3940638471748703,
  'P8': 1.9253659418406674,
  'T7': 1.2520395401104552,
  'T8': 1.2520395401104552},
 'F4': {'AF3': 0.9712677282809308,
  'AF4': 0.35168309598273273,
  'F3': 1.09,
  'F4': 0.0,
  'F7': 1.4583655268827496,
  'F8': 0.6026690717134903,
  'FC5': 1.4768263269592672,
  'FC6': 0.5060395241480649,
  'O1': 1.910382948521055,
  'O2': 1.7250921743489536,
  'P7': 1.9253659418406674,
  'P8': 1.3940638471748703,
  'T7': 1.9353095385493246,
  'T8': 1.9353095385493246},
 'F7': {'AF3': 0.6106978057926851,
  'AF4': 1.2608282238274968,
  'F3': 0.6026690717134903,
  'F4': 1.4583655268827496,
  'F7': 0.0,
  'F8': 1.618,
  'FC5': 0.4441045034673708,
  'FC6': 1.747746208692784,
  'O1': 1.616282462937713,
  'O2': 1.9006033252627967,
  'P7': 1.174,
  'P8': 1.9990497742677644,
  'T7': 0.9697943080880604,
  'T8': 0.9697943080880604},
 'F8': {'AF3': 1.2608282238274968,
  'AF4': 0.6106978057926851,
  'F3': 1.4583655268827496,
  'F4': 0.6026690717134903,
  'F7': 1.618,
  'F8': 0.0,
  'FC5': 1.747746208692784,
  'FC6': 0.4441045034673708,
  'O1': 1.9006033252627967,
  'O2': 1.616282462937713,
  'P7': 1.9990497742677644,
  'P8': 1.174,
  'T7': 2.0428570679320663,
  'T8': 2.0428570679320663},
 'FC5': {'AF3': 0.7467697101516638,
  'AF4': 1.3732068307432788,
  'F3': 0.5060395241480649,
  'F4': 1.4768263269592672,
  'F7': 0.4441045034673708,
  'F8': 1.747746208692784,
  'FC5': 0.0,
  'FC6': 1.766,
  'O1': 1.4564497279343356,
  'O2': 1.7923821607012271,
  'P7': 0.9965946066480592,
  'P8': 1.962291723979898,
  'T7': 0.7986950669686148,
  'T8': 0.7986950669686148},
 'FC6': {'AF3': 1.3732068307432788,
  'AF4': 0.7467697101516638,
  'F3': 1.4768263269592672,
  'F4': 0.5060395241480649,
  'F7': 1.747746208692784,
  'F8': 0.4441045034673708,
  'FC5': 1.766,
  'FC6': 0.0,
  'O1': 1.7923821607012271,
  'O2': 1.4564497279343356,
  'P7': 1.962291723979898,
  'P8': 0.9965946066480592,
  'T7': 2.0411716757783998,
  'T8': 2.0411716757783998},
 'O1': {'AF3': 1.8623567891250055,
  'AF4': 1.9832066987583519,
  'F3': 1.7250921743489536,
  'F4': 1.910382948521055,
  'F7': 1.616282462937713,
  'F8': 1.9006033252627967,
  'FC5': 1.4564497279343356,
  'FC6': 1.7923821607012271,
  'O1': 0.0,
  'O2': 0.618,
  'P7': 0.6178745827431324,
  'P8': 1.1754543802291948,
  'T7': 0.905260183593645,
  'T8': 0.905260183593645},
 'O2': {'AF3': 1.9832066987583519,
  'AF4': 1.8623567891250055,
  'F3': 1.910382948521055,
  'F4': 1.7250921743489536,
  'F7': 1.9006033252627967,
  'F8': 1.616282462937713,
  'FC5': 1.7923821607012271,
  'FC6': 1.4564497279343356,
  'O1': 0.618,
  'O2': 0.0,
  'P7': 1.1754543802291948,
  'P8': 0.6178745827431324,
  'T7': 1.4332689908038896,
  'T8': 1.4332689908038896},
 'P7': {'AF3': 1.565545211739348,
  'AF4': 1.915115612698095,
  'F3': 1.3940638471748703,
  'F4': 1.9253659418406674,
  'F7': 1.174,
  'F8': 1.9990497742677644,
  'FC5': 0.9965946066480592,
  'FC6': 1.962291723979898,
  'O1': 0.6178745827431324,
  'O2': 1.1754543802291948,
  'P7': 0.0,
  'P8': 1.618,
  'T7': 0.29296586831916094,
  'T8': 0.29296586831916094},
 'P8': {'AF3': 1.915115612698095,
  'AF4': 1.565545211739348,
  'F3': 1.9253659418406674,
  'F4': 1.3940638471748703,
  'F7': 1.9990497742677644,
  'F8': 1.174,
  'FC5': 1.962291723979898,
  'FC6': 0.9965946066480592,
  'O1': 1.1754543802291948,
  'O2': 0.6178745827431324,
  'P7': 1.618,
  'P8': 0.0,
  'T7': 1.8217005791292926,
  'T8': 1.8217005791292926},
 'T7': {'AF3': 1.4299611218491222,
  'AF4': 1.8834236937025084,
  'F3': 1.2520395401104552,
  'F4': 1.9353095385493246,
  'F7': 0.9697943080880604,
  'F8': 2.0428570679320663,
  'FC5': 0.7986950669686148,
  'FC6': 2.0411716757783998,
  'O1': 0.905260183593645,
  'O2': 1.4332689908038896,
  'P7': 0.29296586831916094,
  'P8': 1.8217005791292926,
  'T7': 0.0,
  'T8': 0.0},
 'T8': {'AF3': 1.4299611218491222,
  'AF4': 1.8834236937025084,
  'F3': 1.2520395401104552,
  'F4': 1.9353095385493246,
  'F7': 0.9697943080880604,
  'F8': 2.0428570679320663,
  'FC5': 0.7986950669686148,
  'FC6': 2.0411716757783998,
  'O1': 0.905260183593645,
  'O2': 1.4332689908038896,
  'P7': 0.29296586831916094,
  'P8': 1.8217005791292926,
  'T7': 0.0,
  'T8': 0.0}
  }

# Para generar electrodeDistances se ejecuta electrodeDistancesGenerator

def distance(x1,x2):
    return math.sqrt(pow(x1[0]-x2[0],2)+pow(x1[1]-x2[1],2)+pow(x1[2]-x2[2],2))

def electrodeDistancesGenerator():
  import csv
  import math

  matrix = []
  with open('distances.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        matrix.append((row[0],(float(row[1]),float(row[2]),float(row[3]))))

  distanceDict = {}
  for i in range(size):
    distanceDict[matrix[i][0]] = {}
    for j in range(size):
        distanceDict[matrix[i][0]][matrix[j][0]] = (distance(matrix[i][1],matrix[j][1]))

  print(distanceDict)