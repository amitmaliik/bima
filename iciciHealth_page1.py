import tabula
import pandas as pd
import copy
import numpy as np

df = tabula.read_pdf('iciciHealth.pdf',pages='1')

col=[]
value=[]
for i in range(len(df)):
    qq=df[i].columns #index
    cc=list(qq)
    
    val=df[i].values
    vl=list(val)
    value.append(val)
    
    y=0
    li=[]
    for i in vl:
        y=y+1
        ff=str(i)
        vv=ff.replace('nan','')
        li.append(vv)
        
    dic={'description':li}
    print(dic)

    

