def link_graph(nodes):
    """Turns unlink graph into linked graph"""
    output = {}
    for i in nodes:
        output[i] = {}

    for i in nodes:
        node = nodes[i]
        output[i]["id"] = i
        output[i]["joins"] = list(map(lambda n: output[n],node))
    return output

def find_paths(current_node,target_nodes,max_visits=2,path=[]):
    """Finds all possible paths from start going via target nodes""" 
    if path.count(current_node) > max_visits:
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