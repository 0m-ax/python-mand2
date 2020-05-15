import xml.etree.ElementTree as ET
railML_ns = {'railML': 'https://www.railml.org/schemas/3.1'}

def load_file(name):
    """Loads railML from file"""
    tree = ET.parse(name)
    return railMLDoc(tree.getroot())

class railMLDoc:
    def __init__(self,root):
        super().__init__()
        self.elements_id_map = railMLDoc.build_id_map(root)
        self.root = root

    def deref_iter(self,input_iter):
        """Performs deref over an iterator"""
        it = iter(input_iter)
        try:
            while True:
                yield self.deref(next(it))
        except StopIteration:
            pass

    def deref(self,element):
        """Turns a <element ref="id"> element into element refrenced"""
        ref = element.get("ref")
        if ref is not None:
            return self.elements_id_map[ref]
        return element

    def to_graph(self,level_id):
        """Converts the railML document into a a unlinked graph"""
        level = self.elements_id_map[level_id]
        graph = {}
        for networkResource in self.deref_iter(level.findall('railML:networkResource', railML_ns)):
            if networkResource.tag == '{https://www.railml.org/schemas/3.1}netElement':
                graph[networkResource.get("id")] = []
        for networkResource in self.deref_iter(level.findall('railML:networkResource', railML_ns)):
            if networkResource.tag == '{https://www.railml.org/schemas/3.1}netRelation':
                elementA_id = self.deref(networkResource.find("railML:elementA",railML_ns)).get("id")
                elementB_id = self.deref(networkResource.find("railML:elementB",railML_ns)).get("id")
                navigability = networkResource.get("navigability")
                if navigability == "Both":
                    graph[elementA_id].append(elementB_id)
                    graph[elementB_id].append(elementA_id)
                elif navigability == "AB":
                    graph[elementA_id].append(elementB_id)
                elif navigability == "BA":
                    graph[elementB_id].append(elementA_id)
        return graph

    @staticmethod
    def build_id_map(root):
        """Creates refrencing every XML element by its id"""
        elements = {}
        for element in root.iter():
            id = element.get("id")
            if id is not None:
                elements[id] = element
        return elements
