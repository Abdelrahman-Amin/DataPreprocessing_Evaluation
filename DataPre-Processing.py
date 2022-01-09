import csv
import Calculations as CLC
import matplotlib.pyplot as plt
import scipy.signal



###################################################################
######## Import Data from CSV to String Arrays    #################
###################################################################
#Open FIles
KinectData = csv.reader(open(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\KinectHandsData.csv"), delimiter=",")
AccelerometerData = csv.reader(open(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\accelerometer.csv"), delimiter=",")

#Create arrays to import data into
NumberOfArrays = 17
i = 1
for i in range(NumberOfArrays + 1):
    globals()["column" + str(i)] = []

#Skip First row
next(KinectData)

#Data import
for Column in KinectData:
    column1.append(Column[0])
    column2.append(Column[1])
    column3.append(Column[2])
    column4.append(Column[3])
    column5.append(Column[4])
    column6.append(Column[5])
    column7.append(Column[6])
    column8.append(Column[7])
    column9.append(Column[8])
    column10.append(Column[9])
    column11.append(Column[10])
    column12.append(Column[11])
    column13.append(Column[12])


#Skip First row
next(AccelerometerData)

for Column in AccelerometerData:
    column14.append(Column[0])
    column15.append(Column[1])
    column16.append(Column[2])
    column17.append(Column[3])

###################################################################
###################################################################
###################################################################



###################################################################
#########     Convert String Arrays to Double   ###################
###################################################################

TimeStamp = CLC.ConvertStrArrayToDouble(column1)
# print(column2)
RHX = CLC.ConvertStrArrayToDouble(column2)
RHY = CLC.ConvertStrArrayToDouble(column3)
RHZ = CLC.ConvertStrArrayToDouble(column4)
RSX = CLC.ConvertStrArrayToDouble(column5)
RSY = CLC.ConvertStrArrayToDouble(column6)
RSZ = CLC.ConvertStrArrayToDouble(column7)
REX = CLC.ConvertStrArrayToDouble(column8)
REY = CLC.ConvertStrArrayToDouble(column9)
REZ = CLC.ConvertStrArrayToDouble(column10)
RWX = CLC.ConvertStrArrayToDouble(column11)
RWY = CLC.ConvertStrArrayToDouble(column12)
RWZ = CLC.ConvertStrArrayToDouble(column13)


AccX = CLC.ConvertStrArrayToDouble(column15)
AccY = CLC.ConvertStrArrayToDouble(column16)
AccZ = CLC.ConvertStrArrayToDouble(column17)
###################################################################
###################################################################
###################################################################

###################################################################
###############   Signals pre-processing   ########################
###################################################################

#Calculate Mean
MeanValueRHX = CLC.CalculateMeanValue(RHX)
MeanValueRHY = CLC.CalculateMeanValue(RHY)
MeanValueRHZ = CLC.CalculateMeanValue(RHZ)
MeanValueRSX = CLC.CalculateMeanValue(RSX)
MeanValueRSY = CLC.CalculateMeanValue(RSY)
MeanValueRSZ = CLC.CalculateMeanValue(RSZ)
MeanValueREX = CLC.CalculateMeanValue(REX)
MeanValueREY = CLC.CalculateMeanValue(REY)
MeanValueREZ = CLC.CalculateMeanValue(REZ)
MeanValueRWX = CLC.CalculateMeanValue(RWX)
MeanValueRWY = CLC.CalculateMeanValue(RWY)
MeanValueRWZ = CLC.CalculateMeanValue(RWZ)

# print(RHX)


# plt.title('Acceleration in Z-axis Preprocessing')
# plt.xlabel('Frames')
# plt.ylabel('Acceleration')
# plt.plot(AccX)
# plt.show()

CLC.RemoveOutOfRange(RHX)
CLC.RemoveOutOfRange(RHY)
CLC.RemoveOutOfRange(RHZ)
CLC.RemoveOutOfRange(RSX)
CLC.RemoveOutOfRange(RSY)
CLC.RemoveOutOfRange(RSZ)
CLC.RemoveOutOfRange(REX)
CLC.RemoveOutOfRange(REY)
CLC.RemoveOutOfRange(REZ)
CLC.RemoveOutOfRange(RWX)
CLC.RemoveOutOfRange(RWY)
CLC.RemoveOutOfRange(RWZ)

RHX = scipy.signal.medfilt(RHX, 3)
RHY = scipy.signal.medfilt(RHY, 3)
RHZ = scipy.signal.medfilt(RHZ, 3)
RSX = scipy.signal.medfilt(RSX, 3)
RSY = scipy.signal.medfilt(RSY, 3)
RSZ = scipy.signal.medfilt(RSZ, 3)
REX = scipy.signal.medfilt(REX, 3)
REY = scipy.signal.medfilt(REY, 3)
REZ = scipy.signal.medfilt(REZ, 3)
RWX = scipy.signal.medfilt(RWX, 3)
RWY = scipy.signal.medfilt(RWY, 3)
RWZ = scipy.signal.medfilt(RWZ, 3)


AccX = scipy.signal.medfilt(AccX,3)
AccY = scipy.signal.medfilt(AccY,3)
AccZ = scipy.signal.medfilt(AccZ,3)

# plt.title('Acceleration in Z-axis Postprocessing')
# plt.xlabel('Frames')
# plt.ylabel('Acceleration')
# # print(RHX)
# plt.plot(AccX)
# plt.show()

#Normalize high values
# for item in RHX:
#     if item > (MeanValueRHX * 1.5):
#         item = (MeanValueRHX * 1.5)
#
# for item in RHY:
#     if item > (MeanValueRHY * 1.5):
#         item = (MeanValueRHY * 1.5)
#
# for item in RHZ:
#     if item > (MeanValueRHZ * 1.5):
#         item = (MeanValueRHZ * 1.5)
#
# for item in RSX:
#     if item > (MeanValueRSX * 1.5):
#         item = (MeanValueRSX * 1.5)
#
# for item in RSY:
#     if item > (MeanValueRSY * 1.5):
#         item = (MeanValueRSY * 1.5)
#
# for item in RSZ:
#     if item > (MeanValueRSZ * 1.5):
#         item = (MeanValueRSZ * 1.5)
#
# for item in REX:
#     if item > (MeanValueREX * 1.5):
#         item = (MeanValueREX * 1.5)
#
# for item in REY:
#     if item > (MeanValueREY * 1.5):
#         item = (MeanValueREY * 1.5)
#
# for item in REZ:
#     if item > (MeanValueREZ * 1.5):
#         item = (MeanValueREZ * 1.5)
#
# for item in RWX:
#     if item > (MeanValueRWX * 1.5):
#         item = (MeanValueRWX * 1.5)
#
# for item in RWY:
#     if item > (MeanValueRWY * 1.5):
#         item = (MeanValueRWY * 1.5)
#
# for item in RWZ:
#     if item > (MeanValueRWZ * 1.5):
#         item = (MeanValueRWZ * 1.5)


###################################################################
###################################################################
###################################################################







###################################################################
#################    Feature Extraction   #########################
###################################################################


###################################################################
###################################################################
###################################################################






###################################################################
###################   Features Extraction   #######################
###################################################################

ROMRHX = CLC.CalcROM(RHX)
MeanValueRHX = CLC.CalculateMeanValue(RHX)

ROMRHY = CLC.CalcROM(RHY)
MeanValueRHY = CLC.CalculateMeanValue(RHY)

ROMRHZ = CLC.CalcROM(RHZ)
MeanValueRHZ = CLC.CalculateMeanValue(RHZ)

ROMRSX = CLC.CalcROM(RSX)
MeanValueRSX = CLC.CalculateMeanValue(RSX)

ROMRSY = CLC.CalcROM(RSY)
MeanValueRSY = CLC.CalculateMeanValue(RSY)

ROMRSZ = CLC.CalcROM(RSZ )
MeanValueRSZ = CLC.CalculateMeanValue(RSZ)

ROMREX = CLC.CalcROM(REX)
MeanValueREX = CLC.CalculateMeanValue(REX)

ROMREY = CLC.CalcROM(REY)
MeanValueREY = CLC.CalculateMeanValue(REY)

ROMREZ = CLC.CalcROM(REZ )
MeanValueREZ = CLC.CalculateMeanValue(REZ)

ROMRWX = CLC.CalcROM(RWX )
MeanValueRWX = CLC.CalculateMeanValue(RWX)

ROMRWY = CLC.CalcROM(RWY )
MeanValueRWY = CLC.CalculateMeanValue(RWY)

ROMRWZ = CLC.CalcROM(RWZ )
MeanValueRWZ = CLC.CalculateMeanValue(RWZ)




MaxAccX = CLC.FindMax(AccX)
ROMAccX = CLC.CalcROM(AccX)
OscAccX = CLC.CalculateOscilliations(AccX)


MaxAccY = CLC.FindMax(AccY)
ROMAccY = CLC.CalcROM(AccY)
OscAccY = CLC.CalculateOscilliations(AccY)


MaxAccZ = CLC.FindMax(AccZ)
ROMAccZ = CLC.CalcROM(AccZ)
OscAccZ = CLC.CalculateOscilliations(AccZ)


###################################################################
###################################################################
###################################################################





###################################################################
##############   Writing Features To CSV File   ###################
###################################################################
headerKinect = ['ROMRHX', 'ROMRHY', 'ROMRHZ', 'ROMRSX', 'ROMRSY', 'ROMRSZ', 'ROMREX', 'ROMREY', 'ROMREZ', 'ROMRWX', 'ROMRWY', 'ROMRWZ']
valuesKinect = [ROMRHX, ROMRHY, ROMRHZ, ROMRSX, ROMRSY, ROMRSZ, ROMREX, ROMREY, ROMREZ, ROMRWX, ROMRWY, ROMRWZ]

headerAcc =['MaxAccX', 'OscAccX', 'MaxAccY', 'OscAccY', 'MaxAccZ', 'OscAccZ']
valuesAcc = [MaxAccX, OscAccX, MaxAccY, OscAccY, MaxAccZ, OscAccZ]

MotionScore = ['ScoreOfMotion']
ScoreOfMotion = 1


header = []
values = []


for item in headerKinect:
    header.append(item)
for item in headerAcc:
    header.append(item)
for item in MotionScore:
    header.append(item)


for item in valuesKinect:
    values.append(item)
for item in valuesAcc:
    values.append(item)

#values.append(ScoreOfMotion)


# write to CSV file
f = open(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\FeaturesExtracted.csv", 'a', newline='')
writer = csv.writer(f)
# writer.writerow(header)
writer.writerow(values)
f.close()
###################################################################
###################################################################
###################################################################