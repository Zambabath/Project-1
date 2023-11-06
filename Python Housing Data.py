import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
plt.interactive(True)

#Import data
df = pd.read_csv('Housing data.csv')

#Make the data from a series into a string into an integer and sum all of England and Wales
df["Yr1996"] = df["Yr1996"].str.replace(',', '').fillna(0).astype(int)
sum_1996 = df['Yr1996'].sum()

df["Yr1997"] = df["Yr1997"].str.replace(',', '').fillna(0).astype(int)
sum_1997 = df['Yr1997'].sum()

df["Yr1998"] = df["Yr1998"].str.replace(',', '').fillna(0).astype(int)
sum_1998 = df['Yr1998'].sum()

df["Yr1999"] = df["Yr1999"].str.replace(',', '').fillna(0).astype(int)
sum_1999 = df['Yr1999'].sum()

df["Yr2000"] = df["Yr2000"].str.replace(',', '').fillna(0).astype(int)
sum_2000 = df['Yr2000'].sum()

df["Yr2001"] = df["Yr2001"].str.replace(',', '').fillna(0).astype(int)
sum_2001 = df['Yr2001'].sum()

df["Yr2002"] = df["Yr2002"].str.replace(',', '').fillna(0).astype(int)
sum_2002 = df['Yr2002'].sum()

df["Yr2003"] = df["Yr2003"].str.replace(',', '').fillna(0).astype(int)
sum_2003 = df['Yr2003'].sum()

df["Yr2004"] = df["Yr2004"].str.replace(',', '').fillna(0).astype(int)
sum_2004 = df['Yr2004'].sum()

df["Yr2005"] = df["Yr2005"].str.replace(',', '').fillna(0).astype(int)
sum_2005 = df['Yr2005'].sum()

df["Yr2006"] = df["Yr2006"].str.replace(',', '').fillna(0).astype(int)
sum_2006 = df['Yr2006'].sum()

df["Yr2007"] = df["Yr2007"].str.replace(',', '').fillna(0).astype(int)
sum_2007 = df['Yr2007'].sum()

df["Yr2008"] = df["Yr2008"].str.replace(',', '').fillna(0).astype(int)
sum_2008 = df['Yr2008'].sum()

df["Yr2009"] = df["Yr2009"].str.replace(',', '').fillna(0).astype(int)
sum_2009 = df['Yr2009'].sum()

df["Yr2010"] = df["Yr2010"].str.replace(',', '').fillna(0).astype(int)
sum_2010 = df['Yr2010'].sum()

df["Yr2011"] = df["Yr2011"].str.replace(',', '').fillna(0).astype(int)
sum_2011 = df['Yr2011'].sum()

df["Yr2012"] = df["Yr2012"].str.replace(',', '').fillna(0).astype(int)
sum_2012 = df['Yr2012'].sum()

#Remove any prices that are zero
remove = 0
if remove < 10000:
    df = df.replace(remove, float("nan"))

#All the data on one graph
fig, ax = plt.subplots()
colors = ['blue', 'red', 'green', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'gray', 'brown', 'pink', 'olive']
labels = ['Dataset {}'.format(i+1) for i in range(12)]
for column in df.columns:
    
    if pd.api.types.is_numeric_dtype(df[column]):
        ax.plot(df.index, df[column], label=column)
ax.legend()
plt.title('All Data')
plt.show(block=True)

#Total house prices per year
print(sum_1996,sum_1997,sum_1998,sum_1999,sum_2000,sum_2001,sum_2002,sum_2003,sum_2004,sum_2005,sum_2006,sum_2007,sum_2008,sum_2009,sum_2010,sum_2011,sum_2012)

#Total house price increases on average per year
print('Average total increase 1996 to 1997 is ' + str(((sum_1997-sum_1996)/sum_1996)*100) + '%')
print('Average total increase 1997 to 1998 is ' + str(((sum_1998-sum_1997)/sum_1997)*100) + '%')
print('Average total increase 1998 to 1999 is ' + str(((sum_1999-sum_1998)/sum_1998)*100) + '%')
print('Average total increase 1999 to 2000 is ' + str(((sum_2000-sum_1999)/sum_1999)*100) + '%')
print('Average total increase 1996 to 2000 is ' + str(((sum_2000-sum_1996)/sum_1996)*100) + '%')

print('Average total increase 2000 to 2001 is ' + str(((sum_2001-sum_2000)/sum_2000)*100) + '%')
print('Average total increase 2001 to 2002 is ' + str(((sum_2002-sum_2001)/sum_2001)*100) + '%')
print('Average total increase 2002 to 2003 is ' + str(((sum_2003-sum_2002)/sum_2002)*100) + '%')
print('Average total increase 2003 to 2004 is ' + str(((sum_2004-sum_2003)/sum_2003)*100) + '%')
print('Average total increase 2004 to 2005 is ' + str(((sum_2005-sum_2004)/sum_2004)*100) + '%')
print('Average total increase 2005 to 2006 is ' + str(((sum_2006-sum_2005)/sum_2005)*100) + '%')
print('Average total increase 1996 to 2006 is ' + str(((sum_2006-sum_1996)/sum_1996)*100) + '%')

print('Average total increase 2006 to 2007 is ' + str(((sum_2007-sum_2006)/sum_2006)*100) + '%')
print('Average total increase 2007 to 2008 is ' + str(((sum_2008-sum_2007)/sum_2007)*100) + '%')
print('Average total increase 2008 to 2009 is ' + str(((sum_2009-sum_2008)/sum_2008)*100) + '%')
print('Average total increase 2009 to 2010 is ' + str(((sum_2010-sum_2009)/sum_2009)*100) + '%')
print('Average total increase 2010 to 2011 is ' + str(((sum_2011-sum_2010)/sum_2010)*100) + '%')
print('Average total increase 2011 to 2012 is ' + str(((sum_2012-sum_2011)/sum_2011)*100) + '%')
print('Average total increase 1996 to 2012 is ' + str(((sum_2012-sum_1996)/sum_1996)*100) + '%')

MeanYr1 = sum_1996/len(list(df['Yr1996']))
MeanYr2 = sum_1997/len(list(df['Yr1997']))
MeanYr3 = sum_1998/len(list(df['Yr1998']))
MeanYr4 = sum_1999/len(list(df['Yr1999']))
MeanYr5 = sum_2000/len(list(df['Yr2000']))
MeanYr6 = sum_2001/len(list(df['Yr2001']))
MeanYr7 = sum_2002/len(list(df['Yr2002']))
MeanYr8 = sum_2003/len(list(df['Yr2003']))
MeanYr9 = sum_2004/len(list(df['Yr2004']))
MeanYr10 = sum_2005/len(list(df['Yr2005']))
MeanYr11 = sum_2006/len(list(df['Yr2006']))
MeanYr12 = sum_2007/len(list(df['Yr2007']))
MeanYr13 = sum_2008/len(list(df['Yr2008']))
MeanYr14 = sum_2009/len(list(df['Yr2009']))
MeanYr15 = sum_2010/len(list(df['Yr2010']))
MeanYr16 = sum_2011/len(list(df['Yr2011']))
MeanYr17 = sum_2012/len(list(df['Yr2012']))

print(MeanYr1,MeanYr2,MeanYr3,MeanYr4,MeanYr5,MeanYr6,MeanYr7,MeanYr8,MeanYr9,MeanYr10,MeanYr11,MeanYr12,MeanYr13,MeanYr14,MeanYr15,MeanYr16,MeanYr17)

#Individual graphs of house prices
plt.plot(df['Yr1996'])
plt.title('1996')
plt.show(block = True)
plt.plot(df['Yr1997'])
plt.title('1997')
plt.show(block = True)
plt.plot(df['Yr1998'])
plt.title('1998')
plt.show(block = True)
plt.plot(df['Yr1999'])
plt.title('1999')
plt.show(block = True)
plt.plot(df['Yr2000'])
plt.title('2000')
plt.show(block = True)
plt.plot(df['Yr2001'])
plt.title('2001')
plt.show(block = True)
plt.plot(df['Yr2002'])
plt.title('2002')
plt.show(block = True)
plt.plot(df['Yr2003'])
plt.title('2003')
plt.show(block = True)
plt.plot(df['Yr2004'])
plt.title('2004')
plt.show(block = True)
plt.plot(df['Yr2005'])
plt.title('2005')
plt.show(block = True)
plt.plot(df['Yr2006'])
plt.title('2006')
plt.show(block = True)
plt.plot(df['Yr2007'])
plt.title('2007')
plt.show(block = True)
plt.plot(df['Yr2008'])
plt.title('2008')
plt.show(block = True)
plt.plot(df['Yr2009'])
plt.title('2009')
plt.show(block = True)
plt.plot(df['Yr2010'])
plt.title('2010')
plt.show(block = True)
plt.plot(df['Yr2011'])
plt.title('2011')
plt.show(block = True)
plt.plot(df['Yr2012'])
plt.title('2012')
plt.show(block = True)

#Subplots of data side by side with a y-axis of 1.8 million 
plt.figure(figsize=(12,8))

plt.subplot(4,5,1)
plt.plot(df['Yr1996'])
plt.ylim(0,1800000)
plt.title('1996')

plt.subplot(4,5,2)
plt.plot(df['Yr1997'])
plt.ylim(0,1800000)
plt.title('1997')

plt.subplot(4,5,3)
plt.plot(df['Yr1998'])
plt.ylim(0,1800000)
plt.title('1998')

plt.subplot(4,5,4)
plt.plot(df['Yr1999'])
plt.ylim(0,1800000)
plt.title('1999')

plt.subplot(4,5,5)
plt.plot(df['Yr2000'])
plt.ylim(0,1800000)
plt.title('2000')

plt.subplot(4,5,6)
plt.plot(df['Yr2001'])
plt.ylim(0,1800000)
plt.title('2001')

plt.subplot(4,5,7)
plt.plot(df['Yr2002'])
plt.ylim(0,1800000)
plt.title('2002')

plt.subplot(4,5,8)
plt.plot(df['Yr2003'])
plt.ylim(0,1800000)
plt.title('2003')

plt.subplot(4,5,9)
plt.plot(df['Yr2004'])
plt.ylim(0,1800000)
plt.title('2004')

plt.subplot(4,5,10)
plt.plot(df['Yr2005'])
plt.ylim(0,1800000)
plt.title('2005')

plt.subplot(4,5,11)
plt.plot(df['Yr2006'])
plt.ylim(0,1800000)
plt.title('2006')

plt.subplot(4,5,12)
plt.plot(df['Yr2007'])
plt.ylim(0,1800000)
plt.title('2007')

plt.subplot(4,5,13)
plt.plot(df['Yr2008'])
plt.ylim(0,1800000)
plt.title('2008')

plt.subplot(4,5,14)
plt.plot(df['Yr2009'])
plt.ylim(0,1800000)
plt.title('2009')

plt.subplot(4,5,15)
plt.plot(df['Yr2010'])
plt.ylim(0,1800000)
plt.title('2010')

plt.subplot(4,5,16)
plt.plot(df['Yr2011'])
plt.ylim(0,1800000)
plt.title('2011')

plt.subplot(4,5,17)
plt.plot(df['Yr2012'])
plt.ylim(0,1800000)
plt.title('2012')

plt.tight_layout()
plt.show(block=True)

#WALES


#Wales total house prices
sum1_1996 = df['W1'].sum()
df["W2"] = df["W2"].str.replace(',', '').fillna(0).astype(int)
sum1_1997 = df['W2'].sum()
df["W3"] = df["W3"].str.replace(',', '').fillna(0).astype(int)
sum1_1998 = df['W3'].sum()
df["W4"] = df["W4"].str.replace(',', '').fillna(0).astype(int)
sum1_1999 = df['W4'].sum()
df["W5"] = df["W5"].str.replace(',', '').fillna(0).astype(int)
sum1_2000 = df['W5'].sum()
df["W6"] = df["W6"].str.replace(',', '').fillna(0).astype(int)
sum1_2001 = df['W6'].sum()
df["W7"] = df["W7"].str.replace(',', '').fillna(0).astype(int)
sum1_2002 = df['W7'].sum()
df["W8"] = df["W8"].str.replace(',', '').fillna(0).astype(int)
sum1_2003 = df['W8'].sum()
df["W9"] = df["W9"].str.replace(',', '').fillna(0).astype(int)
sum1_2004 = df['W9'].sum()
df["W10"] = df["W10"].str.replace(',', '').fillna(0).astype(int)
sum1_2005 = df['W10'].sum()
df["W11"] = df["W11"].str.replace(',', '').fillna(0).astype(int)
sum1_2006 = df['W11'].sum()
df["W12"] = df["W12"].str.replace(',', '').fillna(0).astype(int)
sum1_2007 = df['W12'].sum()
df["W13"] = df["W13"].str.replace(',', '').fillna(0).astype(int)
sum1_2008 = df['W13'].sum()
df["W14"] = df["W14"].str.replace(',', '').fillna(0).astype(int)
sum1_2009 = df['W14'].sum()
df["W15"] = df["W15"].str.replace(',', '').fillna(0).astype(int)
sum1_2010 = df['W15'].sum()
df["W16"] = df["W16"].str.replace(',', '').fillna(0).astype(int)
sum1_2011 = df['W16'].sum()
df["W17"] = df["W17"].str.replace(',', '').fillna(0).astype(int)
sum1_2012 = df['W17'].sum()
print(sum1_1996,sum1_1997,sum1_1998,sum1_1999,sum1_2000,sum1_2001,sum1_2002,sum1_2003,sum1_2004,sum1_2005,sum1_2006,sum1_2007,sum1_2008,sum1_2009,sum1_2010,sum1_2011,sum1_2012)

MeanYrW1 = sum1_1996/len(list(df['W1']))
MeanYrW2 = sum1_1997/len(list(df['W2']))
MeanYrW3 = sum1_1998/len(list(df['W3']))
MeanYrW4 = sum1_1999/len(list(df['W4']))
MeanYrW5 = sum1_2000/len(list(df['W5']))
MeanYrW6 = sum1_2001/len(list(df['W6']))
MeanYrW7 = sum1_2002/len(list(df['W7']))
MeanYrW8 = sum1_2003/len(list(df['W8']))
MeanYrW9 = sum1_2004/len(list(df['W9']))
MeanYrW10 = sum1_2005/len(list(df['W10']))
MeanYrW11 = sum1_2006/len(list(df['W11']))
MeanYrW12 = sum1_2007/len(list(df['W12']))
MeanYrW13 = sum1_2008/len(list(df['W13']))
MeanYrW14 = sum1_2009/len(list(df['W14']))
MeanYrW15 = sum1_2010/len(list(df['W15']))
MeanYrW16 = sum1_2011/len(list(df['W16']))
MeanYrW17 = sum1_2012/len(list(df['W17']))

print(MeanYrW1,MeanYrW2,MeanYrW3,MeanYrW4,MeanYrW5,MeanYrW6,MeanYrW7,MeanYrW8,MeanYrW9,MeanYrW10,MeanYrW11,MeanYrW12,MeanYrW13,MeanYrW14,MeanYrW15,MeanYrW16,MeanYrW17)

#Wales average house price increase per year
print('Average total increase 1997 to 1998 is ' + str(((sum1_1998-sum1_1997)/sum1_1997)*100) + '%')
print('Average total increase 1998 to 1999 is ' + str(((sum1_1999-sum1_1998)/sum1_1998)*100) + '%')
print('Average total increase 1999 to 2000 is ' + str(((sum1_2000-sum1_1999)/sum1_1999)*100) + '%')
print('Average total increase 1997 to 2000 is ' + str(((sum1_2000-sum1_1997)/sum1_1997)*100) + '%')

print('Average total increase 2000 to 2001 is ' + str(((sum1_2001-sum1_2000)/sum1_2000)*100) + '%')
print('Average total increase 2001 to 2002 is ' + str(((sum1_2002-sum1_2001)/sum1_2001)*100) + '%')
print('Average total increase 2002 to 2003 is ' + str(((sum1_2003-sum1_2002)/sum1_2002)*100) + '%')
print('Average total increase 2003 to 2004 is ' + str(((sum1_2004-sum1_2003)/sum1_2003)*100) + '%')
print('Average total increase 2004 to 2005 is ' + str(((sum1_2005-sum1_2004)/sum1_2004)*100) + '%')
print('Average total increase 2005 to 2006 is ' + str(((sum1_2006-sum1_2005)/sum1_2005)*100) + '%')
print('Average total increase 1997 to 2006 is ' + str(((sum1_2006-sum1_1997)/sum1_1997)*100) + '%')

print('Average total increase 2006 to 2007 is ' + str(((sum1_2007-sum1_2006)/sum1_2006)*100) + '%')
print('Average total increase 2007 to 2008 is ' + str(((sum1_2008-sum1_2007)/sum1_2007)*100) + '%')
print('Average total increase 2008 to 2009 is ' + str(((sum1_2009-sum1_2008)/sum1_2008)*100) + '%')
print('Average total increase 2009 to 2010 is ' + str(((sum1_2010-sum1_2009)/sum1_2009)*100) + '%')
print('Average total increase 2010 to 2011 is ' + str(((sum1_2011-sum1_2010)/sum1_2010)*100) + '%')
print('Average total increase 2011 to 2012 is ' + str(((sum1_2012-sum1_2011)/sum1_2011)*100) + '%')
print('Average total increase 1997 to 2012 is ' + str(((sum1_2012-sum1_1997)/sum1_1997)*100) + '%')


#ENGLAND


#England total house prices
df["E1"] = df["E1"].str.replace(',', '').fillna(0).astype(int)
sum2_1996 = df['E1'].sum()
df["E2"] = df["E2"].str.replace(',', '').fillna(0).astype(int)
sum2_1997 = df['E2'].sum()
df["E3"] = df["E3"].str.replace(',', '').fillna(0).astype(int)
sum2_1998 = df['E3'].sum()
df["E4"] = df["E4"].str.replace(',', '').fillna(0).astype(int)
sum2_1999 = df['E4'].sum()
df["E5"] = df["E5"].str.replace(',', '').fillna(0).astype(int)
sum2_2000 = df['E5'].sum()
df["E6"] = df["E6"].str.replace(',', '').fillna(0).astype(int)
sum2_2001 = df['E6'].sum()
df["E7"] = df["E7"].str.replace(',', '').fillna(0).astype(int)
sum2_2002 = df['E7'].sum()
df["E8"] = df["E8"].str.replace(',', '').fillna(0).astype(int)
sum2_2003 = df['E8'].sum()
df["E9"] = df["E9"].str.replace(',', '').fillna(0).astype(int)
sum2_2004 = df['E9'].sum()
df["E10"] = df["E10"].str.replace(',', '').fillna(0).astype(int)
sum2_2005 = df['E10'].sum()
df["E11"] = df["E11"].str.replace(',', '').fillna(0).astype(int)
sum2_2006 = df['E11'].sum()
df["E12"] = df["E12"].str.replace(',', '').fillna(0).astype(int)
sum2_2007 = df['E12'].sum()
df["E13"] = df["E13"].str.replace(',', '').fillna(0).astype(int)
sum2_2008 = df['E13'].sum()
df["E14"] = df["E14"].str.replace(',', '').fillna(0).astype(int)
sum2_2009 = df['E14'].sum()
df["E15"] = df["E15"].str.replace(',', '').fillna(0).astype(int)
sum2_2010 = df['E15'].sum()
df["E16"] = df["E16"].str.replace(',', '').fillna(0).astype(int)
sum2_2011 = df['E16'].sum()
df["E17"] = df["E17"].str.replace(',', '').fillna(0).astype(int)
sum2_2012 = df['E17'].sum()
print(sum2_1996,sum2_1997,sum2_1998,sum2_1999,sum2_2000,sum2_2001,sum2_2002,sum2_2003,sum2_2004,sum2_2005,sum2_2006,sum2_2007,sum2_2008,sum2_2009,sum2_2010,sum2_2011,sum2_2012)

#England mean house prices
MeanYrE1 = sum2_1996/len(list(df['E1']))
MeanYrE2 = sum2_1997/len(list(df['E2']))
MeanYrE3 = sum2_1998/len(list(df['E3']))
MeanYrE4 = sum2_1999/len(list(df['E4']))
MeanYrE5 = sum2_2000/len(list(df['E5']))
MeanYrE6 = sum2_2001/len(list(df['E6']))
MeanYrE7 = sum2_2002/len(list(df['E7']))
MeanYrE8 = sum2_2003/len(list(df['E8']))
MeanYrE9 = sum2_2004/len(list(df['E9']))
MeanYrE10 = sum2_2005/len(list(df['E10']))
MeanYrE11 = sum2_2006/len(list(df['E11']))
MeanYrE12 = sum2_2007/len(list(df['E12']))
MeanYrE13 = sum2_2008/len(list(df['E13']))
MeanYrE14 = sum2_2009/len(list(df['E14']))
MeanYrE15 = sum2_2010/len(list(df['E15']))
MeanYrE16 = sum2_2011/len(list(df['E16']))
MeanYrE17 = sum2_2012/len(list(df['E17']))

print(MeanYrE1,MeanYrE2,MeanYrE3,MeanYrE4,MeanYrE5,MeanYrE6,MeanYrE7,MeanYrE8,MeanYrE9,MeanYrE10,MeanYrE11,MeanYrE12,MeanYrE13,MeanYrE14,MeanYrE15,MeanYrE16,MeanYrE17)

#England average house price increase per year (including 1996)
print('Average total increase 1996 to 1997 is ' + str(((sum2_1997-sum2_1996)/sum2_1996)*100) + '%')
print('Average total increase 1997 to 1998 is ' + str(((sum2_1998-sum2_1997)/sum2_1997)*100) + '%')
print('Average total increase 1998 to 1999 is ' + str(((sum2_1999-sum2_1998)/sum2_1998)*100) + '%')
print('Average total increase 1999 to 2000 is ' + str(((sum2_2000-sum2_1999)/sum2_1999)*100) + '%')
print('Average total increase 1996 to 2000 is ' + str(((sum2_2000-sum2_1996)/sum2_1996)*100) + '%')

print('Average total increase 2000 to 2001 is ' + str(((sum2_2001-sum2_2000)/sum2_2000)*100) + '%')
print('Average total increase 2001 to 2002 is ' + str(((sum2_2002-sum2_2001)/sum2_2001)*100) + '%')
print('Average total increase 2002 to 2003 is ' + str(((sum2_2003-sum2_2002)/sum2_2002)*100) + '%')
print('Average total increase 2003 to 2004 is ' + str(((sum2_2004-sum2_2003)/sum2_2003)*100) + '%')
print('Average total increase 2004 to 2005 is ' + str(((sum2_2005-sum2_2004)/sum2_2004)*100) + '%')
print('Average total increase 2005 to 2006 is ' + str(((sum2_2006-sum2_2005)/sum2_2005)*100) + '%')
print('Average total increase 1996 to 2006 is ' + str(((sum2_2006-sum2_1996)/sum2_1996)*100) + '%')

print('Average total increase 2006 to 2007 is ' + str(((sum2_2007-sum2_2006)/sum2_2006)*100) + '%')
print('Average total increase 2007 to 2008 is ' + str(((sum2_2008-sum2_2007)/sum2_2007)*100) + '%')
print('Average total increase 2008 to 2009 is ' + str(((sum2_2009-sum2_2008)/sum2_2008)*100) + '%')
print('Average total increase 2009 to 2010 is ' + str(((sum2_2010-sum2_2009)/sum2_2009)*100) + '%')
print('Average total increase 2010 to 2011 is ' + str(((sum2_2011-sum2_2010)/sum2_2010)*100) + '%')
print('Average total increase 2011 to 2012 is ' + str(((sum2_2012-sum2_2011)/sum2_2011)*100) + '%')
print('Average total increase 1996 to 2012 is ' + str(((sum2_2012-sum2_1996)/sum2_1996)*100) + '%')

#England average house price increase per year (excluding 1996)
print('Average total increase 1997 to 1998 is ' + str(((sum2_1998-sum2_1997)/sum2_1997)*100) + '%')
print('Average total increase 1998 to 1999 is ' + str(((sum2_1999-sum2_1998)/sum2_1998)*100) + '%')
print('Average total increase 1999 to 2000 is ' + str(((sum2_2000-sum2_1999)/sum2_1999)*100) + '%')
print('Average total increase 1996 to 2000 is ' + str(((sum2_2000-sum2_1997)/sum2_1997)*100) + '%')

print('Average total increase 2000 to 2001 is ' + str(((sum2_2001-sum2_2000)/sum2_2000)*100) + '%')
print('Average total increase 2001 to 2002 is ' + str(((sum2_2002-sum2_2001)/sum2_2001)*100) + '%')
print('Average total increase 2002 to 2003 is ' + str(((sum2_2003-sum2_2002)/sum2_2002)*100) + '%')
print('Average total increase 2003 to 2004 is ' + str(((sum2_2004-sum2_2003)/sum2_2003)*100) + '%')
print('Average total increase 2004 to 2005 is ' + str(((sum2_2005-sum2_2004)/sum2_2004)*100) + '%')
print('Average total increase 2005 to 2006 is ' + str(((sum2_2006-sum2_2005)/sum2_2005)*100) + '%')
print('Average total increase 1996 to 2006 is ' + str(((sum2_2006-sum2_1997)/sum2_1997)*100) + '%')

print('Average total increase 2006 to 2007 is ' + str(((sum2_2007-sum2_2006)/sum2_2006)*100) + '%')
print('Average total increase 2007 to 2008 is ' + str(((sum2_2008-sum2_2007)/sum2_2007)*100) + '%')
print('Average total increase 2008 to 2009 is ' + str(((sum2_2009-sum2_2008)/sum2_2008)*100) + '%')
print('Average total increase 2009 to 2010 is ' + str(((sum2_2010-sum2_2009)/sum2_2009)*100) + '%')
print('Average total increase 2010 to 2011 is ' + str(((sum2_2011-sum2_2010)/sum2_2010)*100) + '%')
print('Average total increase 2011 to 2012 is ' + str(((sum2_2012-sum2_2011)/sum2_2011)*100) + '%')
print('Average total increase 1996 to 2012 is ' + str(((sum2_2012-sum2_1997)/sum2_1997)*100) + '%')