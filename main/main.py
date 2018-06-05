from tools.tgff_tools import Tgff_tools

if __name__=='__main__':
    path='/home/lianghong/schedule/example.tgff'
    graph=Tgff_tools.read_graph(path)[0]
    pe=Tgff_tools.read_pe(path)[0]
    arc=Tgff_tools.read_arc(path)[0]

    Tgff_tools.build_graph(graph,arc,pe)
    print(graph)
