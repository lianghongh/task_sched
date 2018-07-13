from matplotlib import pyplot as plt
import numpy as np
import re


def read_data(path:str):
    r=[]
    with open(path,encoding="utf-8") as f:
        line=f.readline()
        while line:
            t=re.findall("\d*\.?\d+",line)
            r.append(list(map(float,t)))
            line=f.readline()
    return r


if __name__=='__main__':
    simple_ga_path="/Users/lianghong/Documents/sched_data/simple_ga"
    cuckoo_path="/Users/lianghong/Documents/sched_data/cuckoo"
    nsga_path="/Users/lianghong/Documents/sched_data/nsga2"
    simple_ga_data=read_data(simple_ga_path)
    size=len(simple_ga_data)
    simple_ga_data=list(zip(*simple_ga_data))
    cuckoo_data=list(zip(*read_data(cuckoo_path)))
    nsga_data=list(zip(*read_data(nsga_path)))

    fig=plt.figure()
    ax=fig.add_subplot(311)
    x=np.arange(size)
    ax.plot(x,simple_ga_data[0],label="simple_ga",color='r')
    ax.plot(x,cuckoo_data[0],label="cuckoo",color="g")
    ax.plot(x,nsga_data[0],label="nsga",color="b")
    # ax.set_xlabel("Generation")
    ax.set_ylabel("Power (mJ)")
    ax.set_title("Power Consumption",fontsize=11)
    ax.legend()

    ax2=fig.add_subplot(312)
    ax2.plot(x,simple_ga_data[1],label="simple_ga",color="r")
    ax2.plot(x,cuckoo_data[1],label="cuckoo",color="g")
    ax2.plot(x,nsga_data[1],label="nsga",color="b")
    # ax2.set_xlabel("Generation")
    ax2.set_ylabel("Time (ms)")
    ax2.set_title("Sched Length",fontsize=11)
    ax2.legend()

    ax3=fig.add_subplot(313)
    ax3.plot(x,simple_ga_data[2],label="simple_ga",color="r")
    ax3.plot(x,cuckoo_data[2],label="cuckoo",color="g")
    ax3.plot(x,nsga_data[2],label="nsga",color="b")
    ax3.set_xlabel("Generation")
    ax3.set_ylabel("Time (ms)")
    ax3.set_title("Constraint",fontsize=11)
    ax3.legend()

    # plt.tight_layout()
    plt.show()

