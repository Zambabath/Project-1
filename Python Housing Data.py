import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
plt.interactive(True)

#Import data
df = pd.read_csv('Housing data.csv')

#Make the data from a series into a string into an integer
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

#House price increases on average per year
print('Average increase 1996 to 1997 is ' + str(((sum_1997-sum_1996)/sum_1996)*100) + '%')
print('Average increase 1997 to 1998 is ' + str(((sum_1998-sum_1997)/sum_1997)*100) + '%')
print('Average increase 1998 to 1999 is ' + str(((sum_1999-sum_1998)/sum_1998)*100) + '%')
print('Average increase 1999 to 2000 is ' + str(((sum_2000-sum_1999)/sum_1999)*100) + '%')
print('Average increase 1996 to 2000 is ' + str(((sum_2000-sum_1996)/sum_1996)*100) + '%')

print('Average increase 2000 to 2001 is ' + str(((sum_2001-sum_2000)/sum_2000)*100) + '%')
print('Average increase 2001 to 2002 is ' + str(((sum_2002-sum_2001)/sum_2001)*100) + '%')
print('Average increase 2002 to 2003 is ' + str(((sum_2003-sum_2002)/sum_2002)*100) + '%')
print('Average increase 2003 to 2004 is ' + str(((sum_2004-sum_2003)/sum_2003)*100) + '%')
print('Average increase 2004 to 2005 is ' + str(((sum_2005-sum_2004)/sum_2004)*100) + '%')
print('Average increase 2005 to 2006 is ' + str(((sum_2006-sum_2005)/sum_2005)*100) + '%')
print('Average increase 1996 to 2006 is ' + str(((sum_2006-sum_1996)/sum_1996)*100) + '%')

print('Average increase 2006 to 2007 is ' + str(((sum_2007-sum_2006)/sum_2006)*100) + '%')
print('Average increase 2007 to 2008 is ' + str(((sum_2008-sum_2007)/sum_2007)*100) + '%')
print('Average increase 2008 to 2009 is ' + str(((sum_2009-sum_2008)/sum_2008)*100) + '%')
print('Average increase 2009 to 2010 is ' + str(((sum_2010-sum_2009)/sum_2009)*100) + '%')
print('Average increase 2010 to 2011 is ' + str(((sum_2011-sum_2010)/sum_2010)*100) + '%')
print('Average increase 2011 to 2012 is ' + str(((sum_2012-sum_2011)/sum_2011)*100) + '%')
print('Average increase 1996 to 2012 is ' + str(((sum_2012-sum_1996)/sum_1996)*100) + '%')

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

#Subplots of data side by side
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