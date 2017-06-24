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

class node:
    def __init__(self, num):
        self.name = "node" + str(num)
        self.num = num
        self.adj_node = None
        self.voltage = None

    def addAdjNode(self, adj_node):
        try:
            self.adj_node = self.adj_node + [adj_node]
        except TypeError:
            self.adj_node = [adj_node]

    def getName(self):
        return self.name

class edge:
    def __init__(self, node1, node2):
        self.begin = node1.num
        self.end = node2.num




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
        return Component(name, type, nodes, model)


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
            'v' : "Voltage_Source"  #assume DC
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
        if type in ("Resistor", "Capacitor", "Inductor", "Voltage_Source"):
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
        elif type in ("NPN", "PNP", "Voltage_Source"):
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

