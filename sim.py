import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

sns.set()
pal = sns.color_palette("Set1")
#the population
nod=250
#infection radius
radius=3
#size of area of population
ysize,xsize=50,50
colour=[]
time=[]
xdata,ydata=np.zeros(nod),np.zeros(nod)
susept=[]
infe=[]
recovered=[]
def dots():
    x=np.random.randint(-xsize,xsize)
    y=np.random.randint(-ysize,ysize)
    return x,y
for i in range(nod):
    x,y=dots()
    xdata[i]=x
    ydata[i]=y
colour.append(100)
for i in range(1,nod):
    colour.append(0)
cm=plt.get_cmap('plasma')
fig = plt.figure()
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)
ax1.set_ylim(-xsize-10,xsize+10)
ax1.set_xlim(-xsize-10,xsize+10)
la=ax2.stackplot(time,infe,susept,recovered, labels=['infected','suseptable','recovered'],colors=pal)
ax2.legend(loc='upper left')
ln = ax1.scatter(xdata, ydata) 

def flumps(frames):
    for i in range(len(xdata)):
        x=xdata[i]+np.random.uniform(-6,6)
        y=ydata[i]+np.random.uniform(-6,6)
        if x>=xsize:
                
                xdata[i]=xsize-np.random.randint(0,5)
               
        if x<=-xsize: 
            
            xdata[i]=-xsize+np.random.randint(0,5)   
            
        else: 
            xdata[i]=x
        
        if y>=ysize :
           
            ydata[i]=ysize-np.random.randint(0,5)
            
        if y<=-ysize:
            
            ydata[i]=-ysize+np.random.randint(0,5)
        else:
            
            ydata[i]=y
    
    for i in range(len(xdata)):
        c,d=xdata[i],ydata[i]
        lem=np.array([c,d])
        for j in range(len(ydata)):
            if i!=j:
                lomy=np.array([xdata[j],ydata[j]])
                distance = np.linalg.norm(lem - lomy)
                if distance<=radius:
                    #infection probability
                    ana=np.random.randint(0,2)
                    if colour[j]==0 and colour[i]==0:
                        continue
                    if colour[j]>=250 or colour[i]>=150:
                        continue
                    
                    if colour[j]==0 and colour[i]>0:
                        if ana==1:
                            colour[j]=100
                    if colour[i]==0 and colour[j]>0:
                        if ana==1:
                            colour[i]=10
        if colour[i]>0:
            if colour[i]<150:
                colour[i]=colour[i]+10
    
    ln.set_color(cm(colour))
    data=np.array([xdata,ydata])
    data=data.transpose()
    ln.set_offsets(data)
    su=0
    infec=0
    recov=0
    for i in range(len(colour)):
        if colour[i]==0:
            su+=1
        if colour[i]>0 and colour[i]<150:
            infec+=1
        if colour[i]==150:
            recov+=1
    
    print(frames)
    time.append(frames/15)
    infe.append(infec)
    susept.append(su)
    recovered.append(recov)
    #data=np.array([time,infe,susept,recovered])
    
    #data=data.transpose()
    #la.set_offsets(data)
    ax2.stackplot(time,infe,susept,recovered, labels=['infected','suseptable','recovered'],colors=pal)
    
    
    return ln,la
    
def init():
    
    return ln,la





ani = FuncAnimation(fig, flumps, frames=np.arange(0,1000,1),
                     init_func=init)
plt.show()