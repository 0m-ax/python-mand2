import railml
import graph
import argparse
import draw
import time
def __main__(args):
    if args.benchmark:
        start_time = time.time_ns()
    track_graph = railml.load_file(args.file.name).to_graph(args.level)

    if args.benchmark:
        load_end_time = time.time_ns()
    linked_graph = graph.link_graph(track_graph)
    target_nodes = list(map(lambda x:linked_graph[x],args.visit))

    if args.benchmark:
        link_end_time = time.time_ns()
    if args.algorithm == "breath":
        possible_routes = graph.find_paths_breath_first(linked_graph[args.start],target_nodes,args.max_visits,args.fast_exit)
    if args.algorithm == "depth":
        possible_routes = graph.find_paths_depth_first(linked_graph[args.start],target_nodes,args.max_visits,args.fast_exit)

    if args.benchmark:
        path_find_end_time = time.time_ns()
        print(f'load:{load_end_time-start_time}ns')
        print(f'link:{link_end_time-load_end_time}ns')
        print(f'path_find:{path_find_end_time-link_end_time}ns')
        print(f'Total:{path_find_end_time-start_time}ns')

    if args.output == "text":
        sorted_possible_routes = sorted(possible_routes,key=len)
        for s in sorted_possible_routes[:10]:
            print(",".join(map(lambda x:x['id'],s)))
    if args.output == "graph":
        draw.draw_graph(linked_graph,possible_routes[0])
    if args.output == "stats":
        print(f'Total results:{len(possible_routes)}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Path find over railML')
    parser.add_argument('--level',help='Level to path find on',required=True)
    parser.add_argument('--start',help='Element to start on',required=True)
    parser.add_argument('--file',help='RailML file',type=argparse.FileType('r'),required=True)
    parser.add_argument('--visit', nargs='+',help='Elements to vist',required=True)
    parser.add_argument('--algorithm', help='Algorithm to use', choices=['breath', 'depth'],required=True)
    parser.add_argument('--fast_exit', help='Exit as soon as path found usefull for breath algorithm', action='store_true')
    parser.add_argument('--benchmark', help='Benchmark stats', action='store_true')
    parser.add_argument('--output', help='Output format', choices=['graph', 'text', 'stats'])
    parser.add_argument('--max_visits', help='Max number of times to visit each node', type=int,default=2)
    __main__(parser.parse_args())
