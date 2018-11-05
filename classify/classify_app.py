
def read(fp):
    r=[]
    with open(fp,encoding="utf-8") as f:
        line=f.readline()
        while line!= '':
            if line!='\n':
                r.append(float(line))
            line=f.readline()
    return r

def classify_app(miss_rate,pth,ps,cth):
    """
    IS:密集流型
    IF:密集友好型
    SS:敏感流型
    SF:敏感友好型
    """
    cy=[]
    for k in range(10):
        cy.append((miss_rate[k] - miss_rate[k + 1]) / (128 * (2 ** (k + 1) - 2 ** k) / 1024))
    count,cc=0,0
    for ss in cy:
        if ss != 0:
            count += 1
            cc += ss
    if count!=0:
        pg=cc/count
    else:
        pg=0

    if pg>pth:
        for p in cy:
            if p<0:
                return "SS"
        for c in range(cth+1,11):
            if cy[c]<=ps:
                return "SF"
        return "SS"
    else:
        for p in cy:
            if p<0:
                return "IS"
        for c in range(cth+1,11):
            if cy[c]<=ps:
                return "IF"
        return "IS"



def do_classify(pth,ps,cth):
    dir = "/Users/lianghong/Downloads/gem5_result"
    name = ["bwaves", "gamess", "gromacs", "hmmer", "leslie3d", "mcf", "sjeng", "astar", "bzip2", "calculix", "gobmk",
            "h264ref", "lbm", "libquantum", "milc", "namd", "soplex", "tonto", "zeusmp", "omnetpp", "GemsFDTD"]
    for i in name:
        file = dir + "/" + i + "/miss_rate"
        miss_rate = read(file)
        t=classify_app(miss_rate,pth,ps,cth)
        print("%s : %s" %(i,t))


if __name__=="__main__":
    do_classify(pth=0.3,ps=0.1,cth=8)