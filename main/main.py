from graph import tgff_tools

if __name__=='__main__':
    path='/home/lianghong/schedule/example.tgff'
    graph=tgff_tools.read_graph(path)[0]
    pe=tgff_tools.read_pe(path)[0]
    arc=tgff_tools.read_arc(path)[0]

    tgff_tools.build_graph(graph,arc,pe)
    graph.update_rank_u()
    print(graph)
