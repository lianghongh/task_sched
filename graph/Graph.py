class TaskNode:

    def __init__(self):
        self.task=None
        self.deadline=None
        self.type=None
        self.exec_time=None
        self.next=None
        self.in_degree=0
        self.out_degree=0
        self.rank_u=None

    def __repr__(self):
        l = list()
        p = self.next
        while p != None:
            l.append(str(p))
            p = p.next
        arc='['+','.join(l)+']'
        return '[task:' + str(self.task) + ', exec_time:' + str(self.exec_time) + ', rank_u:'+'%.4f' % (self.rank_u,)+', in_degree:'+str(self.in_degree)+', out_degree:'+str(self.out_degree)+', deadline:' + str(self.deadline) + ", type:" + str(self.type) + ", arc_node:" + arc + "]"



class ArcNode:

    def __init__(self):
        self.task=None
        self.next=None
        self.type=None
        self.weight=None

    def __repr__(self):
        return '(task:' + str(self.task) + ', type:' + str(self.type) + ', weight:' + str(self.weight) + ')'


class TaskGraph:

    def __init__(self,max_node:int=100):
        self.nodes=[TaskNode() for i in range(max_node)]
        self.period=None
        self.task_num=0
        self.arc_num=0
        self.max_node=max_node

        self.arc_dict=None
        self.task_dict=None


    def add_arc(self,from_node:int,to_node:int,type:int)->None:
        if from_node<0 or from_node>self.max_node or to_node<0 or to_node>self.max_node:
            return
        arc=ArcNode()
        arc.task=to_node
        arc.type=type
        arc.next=self.nodes[from_node].next
        self.nodes[from_node].next=arc
        self.arc_num+=1
        self.nodes[from_node].out_degree+=1
        self.nodes[to_node].in_degree+=1

    def update_rank_u(self):
        for i in self.nodes:
            if i.in_degree==0:
                i.rank_u=self._rank_u(i)


    def _rank_u(self,node:TaskNode):
        if node.out_degree==0:
            node.rank_u=node.exec_time
            return node.rank_u
        max_u=0
        arc=node.next
        while arc!=None:
            self.nodes[arc.task].rank_u=self._rank_u(self.nodes[arc.task])
            dd=arc.weight+self.nodes[arc.task].rank_u
            if dd>max_u:
                max_u=dd
            arc=arc.next
        return max_u+node.exec_time


    def __repr__(self):
        pp = '\n'
        for i in range(self.task_num):
            pp = pp + "           " + str(self.nodes[i]) + '\n'
        s = "[period:" + str(self.period) + ", task_num:" + str(self.task_num) + ", arc_num:" + str(self.arc_num) + ", arc_dict:" + str(self.arc_dict) + ", task_dict:" + str(self.task_dict) + "]" + pp + "]"
        return "TaskGraph->" + s


