from tools.Graph import TaskGraph


class Tgff_tools:

    def __init__(self):
        pass

    @staticmethod
    def read_graph(path: str, read_mode: str = "r") -> list:
        '''
        read graph list from specified file
        '''
        with open(path, read_mode, encoding='utf-8') as f:
            graph_list = list()
            line = f.readline()
            while 1:
                while not '@TASK' in line and not '@ARC' in line:
                    line = f.readline()
                if '@ARC' in line:
                    break
                g = TaskGraph()
                line = f.readline()
                g.period = int(line.split()[1])
                f.readline()
                line = f.readline()
                index = 0
                while line != '\n':
                    g.nodes[index].task = index
                    g.nodes[index].type = int(line.split()[3])
                    index += 1
                    line = f.readline()
                line = f.readline()
                g.task_num = index
                while line != '\n':
                    tmp = line.split()
                    from_v = int(tmp[3].split('_')[1])
                    to_v = int(tmp[5].split('_')[1])
                    g.add_arc(from_v, to_v, int(tmp[7]))
                    line = f.readline()
                line = f.readline()
                while line != '\n' and line != '}\n':
                    tmp = line.split()
                    g.nodes[int(tmp[3].split('_')[1])].deadline = int(tmp[5])
                    line = f.readline()

                graph_list.append(g)

            return graph_list

    @staticmethod
    def read_pe(path: str, read_mode: str = "r") -> list:
        '''
        read pe list from specified file
        '''

        with open(path, read_mode, encoding='utf-8') as f:
            pe_list = []
            line = f.readline()
            while 1:
                while not '@PE' in line and line != '':
                    line = f.readline()
                if line == '':
                    break
                tag = f.readline().split()[1]
                line = f.readline()
                g = dict()
                g[tag] = float(line)

                for i in range(3):
                    f.readline()
                line = f.readline()
                while line != '}\n':
                    tmp = line.split()
                    g[tmp[0]] = float(tmp[2])
                    line = f.readline()
                pe_list.append(g)

            return pe_list

    @staticmethod
    def read_arc(path: str, read_mode: str = "r") -> list:
        '''
        read arc list from specified file
        '''

        with open(path, read_mode, encoding='utf-8') as f:
            arc_list = []
            line = f.readline()
            while 1:
                while not '@ARC' in line and not '@PE' in line:
                    line = f.readline()
                if '@PE' in line:
                    break
                arc = {}
                tag = f.readline().split()[1]
                line = f.readline()
                arc[tag] = float(line)
                for i in range(3):
                    f.readline()
                line = f.readline()
                while line != '}\n':
                    tmp = line.split()
                    arc[tmp[0]] = float(tmp[1])
                    line = f.readline()

                arc_list.append(arc)
            return arc_list

    @staticmethod
    def build_graph(g: TaskGraph, arc: dict, pe: dict) -> None:
        '''
        build graph from arc and pe dictionary
        '''
        g.arc_dict = arc
        g.task_dict = pe
        for i in range(g.task_num):
            g.nodes[i].exec_time = g.task_dict[str(g.nodes[i].type)]
            arc_node = g.nodes[i].next
            while arc_node != None:
                arc_node.weight = g.arc_dict[str(arc_node.type)]
                arc_node = arc_node.next
