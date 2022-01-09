import csv

from sklearn.svm import OneClassSVM
from numpy import genfromtxt, where, quantile
import matplotlib.pyplot as plt
import Calculations as CLC




###################################################################
######## Import Data from CSV to String Arrays    #################
###################################################################
#Open FIles
# KinectData = csv.reader(open(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\FeaturesExtracted.csv"), delimiter=",")
#
# #Create arrays to import data into
# NumberOfArrays = 33
# i = 1
# for i in range(NumberOfArrays + 1):
#     globals()["column" + str(i)] = []
#
# #Skip First row
# next(KinectData)
#
# #Data import
# for Column in KinectData:
#     column1.append(Column[0])
#     column2.append(Column[1])
#     column3.append(Column[2])
#     column4.append(Column[3])
#     column5.append(Column[4])
#     column6.append(Column[5])
#     column7.append(Column[6])
#     column8.append(Column[7])
#     column9.append(Column[8])
#     column10.append(Column[9])
#     column11.append(Column[10])
#     column12.append(Column[11])
#     column13.append(Column[12])
#     column14.append(Column[13])
#     column15.append(Column[14])
#     column16.append(Column[15])
#     column17.append(Column[16])
#     column18.append(Column[17])
#     column19.append(Column[18])
#     column20.append(Column[19])
#     column21.append(Column[20])
#     column22.append(Column[21])
#     column23.append(Column[22])
#     column24.append(Column[23])
#     column25.append(Column[24])
#     column26.append(Column[25])
#     column27.append(Column[26])
#     column28.append(Column[27])
#     column29.append(Column[28])
#     column30.append(Column[29])
#     column31.append(Column[30])
#     column32.append(Column[31])
#     column33.append(Column[32])
#
#
#
# ###################################################################
# ###################################################################
# ###################################################################
#
#
#
# ###################################################################
# #########     Convert String Arrays to Double   ###################
# ###################################################################
#
# MaxRHX = CLC.ConvertStrArrayToDouble(column1)
# ROMRHX = CLC.ConvertStrArrayToDouble(column2)
# MaxRHY = CLC.ConvertStrArrayToDouble(column3)
# ROMRHY = CLC.ConvertStrArrayToDouble(column4)
# MaxRHZ = CLC.ConvertStrArrayToDouble(column5)
# ROMRHZ = CLC.ConvertStrArrayToDouble(column6)
# MaxRSX = CLC.ConvertStrArrayToDouble(column7)
# ROMRSX = CLC.ConvertStrArrayToDouble(column8)
# MaxRSY = CLC.ConvertStrArrayToDouble(column9)
# ROMRSY = CLC.ConvertStrArrayToDouble(column10)
# MaxRSZ = CLC.ConvertStrArrayToDouble(column11)
# ROMRSZ = CLC.ConvertStrArrayToDouble(column12)
# MaxREX = CLC.ConvertStrArrayToDouble(column13)
# ROMREX = CLC.ConvertStrArrayToDouble(column14)
# MaxREY = CLC.ConvertStrArrayToDouble(column15)
# ROMREY = CLC.ConvertStrArrayToDouble(column16)
# MaxREZ = CLC.ConvertStrArrayToDouble(column17)
# ROMREZ = CLC.ConvertStrArrayToDouble(column18)
# MaxRWX = CLC.ConvertStrArrayToDouble(column19)
# ROMRWX = CLC.ConvertStrArrayToDouble(column20)
# MaxRWY = CLC.ConvertStrArrayToDouble(column21)
# ROMRWY = CLC.ConvertStrArrayToDouble(column22)
# MaxRWZ = CLC.ConvertStrArrayToDouble(column23)
# ROMRWZ = CLC.ConvertStrArrayToDouble(column24)
# MaxAccX = CLC.ConvertStrArrayToDouble(column25)
# ROMAccX = CLC.ConvertStrArrayToDouble(column26)
# OscAccX = CLC.ConvertStrArrayToDouble(column27)
# MaxAccY = CLC.ConvertStrArrayToDouble(column28)
# ROMAccY = CLC.ConvertStrArrayToDouble(column29)
# OscAccY = CLC.ConvertStrArrayToDouble(column30)
# MaxAccZ = CLC.ConvertStrArrayToDouble(column31)
# ROMAccZ = CLC.ConvertStrArrayToDouble(column32)
# OscAccZ = CLC.ConvertStrArrayToDouble(column33)


TrainData   = genfromtxt(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\FeaturesExtracted_TrainData.csv", skip_header=1, delimiter=',')
TestData    = genfromtxt(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\FeaturesExtracted_TestData.csv", skip_header=1, delimiter=',')
#print(x)

svm = OneClassSVM(kernel='rbf', degree= 3, gamma='scale', nu=0.2)
print(svm,"\n")
svm.fit(TrainData)


pred = svm.predict(TestData)
scores = svm.score_samples(TestData)

x= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

plt.scatter(x,scores)
plt.show()

i = 1
for item in scores:
    print("\n Sample" , i, "Score is ", item, end = " ")
    i = i + 1


f = open(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\Results.csv", 'a', newline='')
writer = csv.writer(f)
# writer.writerow(header)
writer.writerow(scores)
f.close()




# j = 1
# for item in scores:
#     print ("\n Sample Number",j)
#     j = j + 1
#     if item > 3:
#         print("Movement Fully Done")
#     elif item > 0 and item < 3:
#         print("Movement Partially Done")
#     else :
#         print("Movement Is Not Done")


# print("\nPredection Scores:\n",pred)
# j = 0
# print ("\nOutlined samples are:")
# for item in pred:
#     j = j + 1
#     if (item == -1):
#         print(j, end =", ")



# thresh = quantile(scores, 0.03)
# print("\n Threshold is \n ",thresh)

# anom_index = where(pred==-1)
# values = x[anom_index]

# for item in anom_index:
#     print("\n Outlined samples are samples number\n", item)

#plt.scatter(x[:,0], x[:,1])
#plt.scatter(values[:,0], values[:,1], color='r')
#plt.show()