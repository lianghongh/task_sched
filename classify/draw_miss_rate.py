from matplotlib import pyplot as plt
import numpy as np
from classify.classify_app import read


if __name__=='__main__':
    dir = "/Users/lianghong/Downloads/gem5_result"
    name=["bwaves","gamess","gromacs","hmmer","leslie3d","mcf","sjeng","astar","bzip2","calculix","gobmk","h264ref","lbm","libquantum","milc","namd","soplex","tonto","zeusmp","omnetpp","GemsFDTD"]
    for i in name:
        file=dir+"/"+i+"/miss_rate"
        x=np.arange(1,12)
        y=read(file)
        cx=np.arange(1,11)
        cy=[]
        for k in range(10):
            cy.append((y[k]-y[k+1])/(128*(2**(k+1)-2**k)/1024))
        ff=plt.figure()
        pic1=ff.add_subplot(2,1,1)
        pic1.plot(x,y,marker='o',label="Miss Rate")
        pic1.set_title(i+" Cache miss rate")
        pic1.set_ylabel("Miss Rate")
        pic1.grid()
        pic1.legend()

        pic2 = ff.add_subplot(2, 1, 2)

        pic2.plot(cx, cy, marker='o', label="Cache Capacity Gain")
        # pic2.set_title(i + "Miss change rate")
        pic2.set_ylabel("Miss Rate per MB")
        pic2.grid()
        pic2.legend()

        ff.savefig(dir+"/"+i)
        plt.close()
        count,cc=0,0
        for ss in cy:
            if ss!=0:
                count+=1
                cc+=ss

        if count!=0:
            print("The %s average capacity enhancement is %f" %(i,cc/count))
        else:
            print("The %s average capacity enhancement is 0.0" %(i))
