import tabula
import pandas as pd
import copy
import numpy as np
import re
 
df = tabula.read_pdf('StarHealth2.pdf',pages='3')

col=[]
value=[]
thisdict = {}
ff=[]
for i in range(len(df)):
    # print(df[i])
    #print(len(df))
    if i==1:
        dd=df[i]
        #print(len(dd))
        qq=df[i].columns
        #print(qq)
        
        FirstTwoHeader = re.search('Bonus.(.*)', qq[0])
        FirstTwoHeader=FirstTwoHeader.group(1)
        #print(FirstTwoHeader)
        
        aa=FirstTwoHeader.split(". ")
        Header1=aa[0]
        Header2=aa[1]
        Header3=qq[1]
        # print(Header1 + " " + Header2 + " " + Header3)
        
        Line1=dd.iloc[1]
        # print(Line1[0])
        
        
        Line2=dd.iloc[2]
        #print(Line2[0])
        aa=Line2[0].split(", ")
        Line2a=aa[0]
        Line2b=aa[1]
        # print(Line2a + " " + Line2b)
        
        
        ff.append({Header1:Line1[0],Header2:Line2a,Header3:Line2b})
        
        
        Line3=dd.iloc[3]
        # print(Line3[0])        
        ff.append({Header1:Line3[0],Header2:Line2a,Header3:Line2b})
                
        Line5=dd.iloc[5]
        #print(Line5[0])
        aa=Line5[0].split("- ")
        Line5a=aa[0]
        Line5b=aa[1]
        Line5c=Line5[1]
        # print(Line5a + " " + Line5b + " " + Line5c)
        ff.append({Header1:Line5a,Header2:Line5b,Header3:Line5c})
                
        Line7=dd.iloc[7]
        #print(Line5[0])
        aa=Line7[0].split("- ")
        Line7a=aa[0]
        Line7b=aa[1]
        Line7c=Line7[1]
        # print(Line7a + " " + Line7b + " " + Line7c)
        ff.append({Header1:Line7a,Header2:Line7b,Header3:Line7c})
        
        Line9=dd.iloc[9]
        #print(Line5[0])
        aa=Line9[0].split("- ")
        Line9a=aa[0]
        Line9b=aa[1]
        Line9c=Line9[1]
        # print(Line9a + " " + Line9b + " " + Line9c)
        ff.append({Header1:Line9a,Header2:Line9b,Header3:Line9c})
        
        Line11=dd.iloc[11]
        # print(Line11[0])
        
        Line13=dd.iloc[13]
        # print(Line13[0])
        
        Line14=dd.iloc[14]
        Line14a=Line14[0]
        Line14b=Line14[1]
        # print(Line14a + " " + Line14b)
                
        Line15=dd.iloc[15]
        # print(Line15[0])
        
        Line17=dd.iloc[17]
        # print(Line17[0])
        
        ff.append({Header1:Line11[0],Header2:Line14a,Header3:Line14b})        
        ff.append({Header1:Line13[0],Header2:Line14a,Header3:Line14b})
        ff.append({Header1:Line15[0],Header2:Line14a,Header3:Line14b})
        ff.append({Header1:Line17[0],Header2:Line14a,Header3:Line14b})
        
print(ff)