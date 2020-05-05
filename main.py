track_graph = {
    "0":["16"],
    "1":["15","7"],
    "2":["17","5"],
    "3":["8"],
    "4":["5"],
    "5":["6","2"],
    "6":["16"],
    "7":["4","1","10"],
    "8":["7","13"],
    "9":["0"],
    "10":["11","7"],
    "11":["10","12"],
    "12":["11","13"],
    "13":["8","9"],
    "14":["3"],
    "15":["1"],
    "16":["14","17","18"],
    "17":["16","2"],
    "18":["16"]
}

def link_graph(nodes):
    output = {}
    for i in nodes:
        output[i] = {}

    for i in nodes:
        node = nodes[i]
        output[i]["id"] = i
        output[i]["joins"] = list(map(lambda n: output[n],node))
    return output

def find_paths(current_node,target_nodes,path=[]):
    print(current_node["id"])
    if current_node in path:
        return []
    new_path = path.copy()
    new_path.append(current_node)
    possible_routes = []
    if current_node in target_nodes:
        target_nodes = target_nodes.copy()
        target_nodes.remove(current_node)
    if len(target_nodes) == 0:
        possible_routes.append(new_path)
        return possible_routes
    for n in current_node["joins"]:
        output = find_paths(n,target_nodes,new_path)
        if len(output) > 0:
            possible_routes.extend(output)
    return possible_routes



def __main__(args):
    graph = link_graph(track_graph)
    print(graph)
    output = find_paths(graph["0"],[graph["9"]])
    for s in output:
        print(list(map(lambda n: n["id"],s)))
if __name__ == "__main__":
    __main__({})