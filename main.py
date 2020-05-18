import railml
import graph
import argparse

def __main__(args):
    track_graph = railml.load_file(args.file.name).to_graph(args.level)
    linked_graph = graph.link_graph(track_graph)
    target_nodes = list(map(lambda x:linked_graph[x],args.visit))
    possible_routes = graph.find_paths(linked_graph[args.start],target_nodes)
    sorted_possible_routes = sorted(possible_routes,key=len)
    for s in sorted_possible_routes[:10]:
        print(",".join(map(lambda x:x['id'],s)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Path find over railML')
    parser.add_argument('--level',help='level to path find on',required=True)
    parser.add_argument('--start',help='element to start on',required=True)
    parser.add_argument('--file',help='railML file',type=argparse.FileType('r'),required=True)
    parser.add_argument('--visit', nargs='+',help='elements to vist',required=True)

    __main__(parser.parse_args())
