import tabula
import pandas as pd
import copy
import numpy as np
 
df = tabula.read_pdf('StarHealth1.pdf',pages='2')

col=[]
value=[]
thisdict = {}
ff=[]
for i in range(len(df)):
    qq=df[i].columns
    #print(qq)
    
    cc=list(qq)

    if len(cc)>1 :
        val=df[i].values
        vl=list(val)
        
        for j in range(len(vl)):
            ff.append({cc[0]:vl[j][0],cc[1]:vl[j][1]})
print(ff)
                
