def link_graph(nodes):
    """Turns unlink graph into linked graph
    {
        "nodeID":{
            "id":"nodeID",
            "joins":["node",...]
        }
    }
    """
    output = {}
    for i in nodes:
        output[i] = {}

    for i in nodes:
        node = nodes[i]
        output[i]["id"] = i
        output[i]["joins"] = list(map(lambda n: output[n],node))
    return output

def find_paths_depth_first(current_node,target_nodes,max_visits=2,fast_exit=False,path=[]):
    """Finds all possible paths from start going via target nodes""" 
    if path.count(current_node) > max_visits:
        return []
    new_path = path.copy()
    new_path.append(current_node)
    possible_routes = []
    # At a target node
    if current_node in target_nodes:
        target_nodes = target_nodes.copy()
        target_nodes.remove(current_node)
    # All Target nodes visited
    if len(target_nodes) == 0:
        possible_routes.append(new_path)
        return possible_routes
    for n in current_node["joins"]:
        output = find_paths_depth_first(n,target_nodes,max_visits,fast_exit,new_path)
        if len(output) > 0:
            possible_routes.extend(output)
        if fast_exit and len(possible_routes) > 0:
            return possible_routes
    return possible_routes

def find_paths_breath_first(current_node,target_nodes,max_visits=2,fast_exit=False):
    """Finds all possible paths from start going via target nodes""" 
    nodes_to_visit = [{
        "node":current_node,
        "path":[],
        "target_nodes":target_nodes
    }]
    possible_paths = []
    while len(nodes_to_visit) > 0:
        current = nodes_to_visit.pop(0)

        for joined_node in current["node"]["joins"]:
            if current["path"].count(joined_node) < max_visits:
                new_to_visit = {
                    "node": joined_node,
                    "path":  current["path"] + [current["node"]],
                    "target_nodes": current["target_nodes"]
                }
                if joined_node in new_to_visit["target_nodes"]:
                    # we only copy the array here to save memory
                    new_to_visit["target_nodes"] = new_to_visit["target_nodes"].copy()
                    new_to_visit["target_nodes"].remove(joined_node)
                if len(new_to_visit["target_nodes"]) == 0:
                    possible_paths.append(new_to_visit["path"]+[joined_node])
                    if fast_exit:
                        return possible_paths
                else:
                    nodes_to_visit.append(new_to_visit)
    
    return possible_paths

                