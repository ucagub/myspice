import numpy as np

class Graph:

    def __init__(self, component_list):
        """ Creates the graph
            Input: component list
            Output: graph of components
        """
        self.node_list = {}
        self.nodeNums = []
        self.component_list = component_list
        for component in component_list:
            component.addComponent(self)


    def connectNode(self, component):
        nodes = component.getNodes()

        for nodeNum in nodes:
            if not(nodeNum in self.nodeNums):
                self.node_list[nodeNum] = node(nodeNum)

            # assumung resistors and sources only
            buffNode = self.node_list[nodeNum]
            buffNode.addAdjEdge()

    def DCanalysis(self):
        for node in

'''component constructor'''
class Component:

    def __init__(self, name, type, nodes, model):
        self.name = name
        self.type = type
        self.nodes = nodes
        self.model = model

    def getName(self):
         return self.name

    def getType(self):
        return self.type

    def getNodes(self):
        return self.nodes

    def getModel(self):
        return self.model

class Resistor(Component):
    def __init__(self, name, type, nodes, value):
        Component.__init__(self, name, type, nodes, value)
        self.value = value
    def addComponent(self, graph):
        nodes = self.nodes

        for nodeNum in nodes:
            if not(nodeNum in graph.nodeNums):
                graph.node_list[nodeNum] = node(nodeNum)
                graph.nodeNums = graph.nodeNums + [nodeNum]


        # add node edges
        buffNode0 = graph.node_list[nodes[0]]
        buffEdge0t1 = edge([0, -1], [1/self.value, 1/self.value], "notIsource")
        buffNode0.addAdjEdge(buffEdge0t1)

        buffNode1 = graph.node_list[nodes[1]]
        buffEdge1t0= edge([1, 0], [1/self.value, 1/self.value], "notIsource")
        buffNode1.addAdjEdge(buffEdge1t0)

class Isupply(Component):
    def __init__(self, name, type, nodes, value):
        ''' n independent current source whose current flows through the source from node n+ to node n-
        '''
        Component.__init__(self, name, type, nodes, value)
        self.value = value

    def addComponent(self, graph):
        nodes = self.nodes
        for nodeNum in nodes:
            if not(nodeNum in graph.nodeNums):
                graph.node_list[nodeNum] = node(nodeNum)

        # add node edges
        buffNode0 = graph.node_list[nodes[0]] #n+
        buffEdge0t1 = edge([1], [self.value], "Isource")
        buffNode0.addAdjEdge(buffEdge0t1)

        buffNode1 = graph.node_list[nodes[1]] #n-
        buffEdge1t0 = edge([-1], [self.value], "Isource")
        buffNode1.addAdjEdge(buffEdge1t0)

class node:
    def __init__(self, num):
        self.name = "node" + str(num)
        self.num = num
        self.adj_node = None
        self.voltage = None
        self.adj_edge = None

    def addAdjNode(self, adj_node):
        try:
            self.adj_node = self.adj_node + [adj_node]
        except TypeError:
            self.adj_node = [adj_node]

    def getName(self):
        return self.name

    def addAdjEdge(self, adj_edge):
        try:
            self.adj_edge = self.adj_edge + [adj_edge]
        except TypeError:
            self.adj_edge = [adj_edge]



class edge:
    def __init__(self, VolVars, Vweights, type):
        '''indicates the voltage waits; effectively the current'''

        #node voltage dependence array
        self.V = VolVars

        #conductance array
        self.G = Vweights

        self.type = type




def read_netlist(file_name):
    '''
    input: file name
    return: component list
    '''


    def make_component(component_info):
        '''feeds the info to the component constructor'''
        cmp_info_array = component_info.split(" ")
        name = cmp_info_array[0]
        type = getType(name)
        nodes = getNodes(cmp_info_array, type)
        model = getModel(cmp_info_array, type)

        component_types = {"Resistor" : Resistor,
                           "Current_Source" : Isupply
                           }
        buffComp = component_types[type]

        return buffComp(name, type, nodes, model)


    def getType(name):
        """
        input: name of component
        return: the component type
        """
        first_letter = name.lower()[0]
        dict = {
            'r' : "Resistor",
            'c' : "Capacitor",
            'l' : "Inductor",
            'n' : "NPN",
            'p' : "PNP",
            'v' : "Voltage_Source",  #assume DC
            'i' : "Current_Source"  #assume DC
        }

        if first_letter in dict:
            return dict[first_letter]
        else:
            return "unknown"


    def getNodes(cmp_info_array, type):
        '''
            input: cmp_info_array & component type
            return: the nodes in array format
        '''
        if type in ("Resistor", "Capacitor", "Inductor", "Voltage_Source", "Current_Source"):
            return [int(cmp_info_array[1]), int(cmp_info_array[2])]

        elif type in ("NPN", "PNP"):
            return [int(cmp_info_array[1]), int(cmp_info_array[2]), int(cmp_info_array[3])]



    def getModel(cmp_info_array, type):
        '''
            input: cmp_info_array & component type
            return: the model for the component
        '''
        if type in ("Resistor", "Capacitor", "Inductor"):
            return convValue(cmp_info_array[3])
        elif type in ("NPN", "PNP", "Voltage_Source", "Current_Source"):
            return cmp_info_array[4]



    def convValue(value):
        '''
        :param value: raw string value
        :return: float value
        '''

        def is_number(s):
            '''check if the string is numeric'''
            try:
                float(s)
                return True
            except ValueError:
                return False

        def parse_num(value, dict):
            """
            :input: raw value string, dict
            :return: num_part, post_fix
            """
            if value[len(value)-1] in dict:
                return float(value[:len(value)-1]), value[len(value)-1]
            else:
                return float(value[:len(value)-3]), "Meg"


        dict = {
            'f' : 10**-15,
            'p' : 10**-12,
            'n' : 10**-9,
            'u' : 10**-6,
            'm' : 10**-3,
            'k' : 10**3,
            'Meg' : 10**6,
            'G' : 10**9,
            'T' : 10**12,
        }


        if is_number(value):
            return float(value)
        else:
            num_part, post_fix = parse_num(value, dict)
            return num_part * dict[post_fix]


    """function body"""
    file = open(file_name, "r")
    component_list = []

    """assumes no .model part"""
    for component_info in iter(lambda: file.readline().strip(), ''):
        if component_info == "\n":
            continue    #skip new line
        else:
            component_list += [make_component(component_info)]
    file.close()
    return component_list

def DC_char(component_list):
    return






