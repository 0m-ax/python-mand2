# RailML path finding

Path find over a rail network described in railML format

## Run

python main.py --file DATA/050419_railML_SimpleExample_v11/src/railML_SimpleExample_v11_railML3-1_04.xml --start ne_a01 --level lv0 --visit ne_b01 ne_b05 --algorithm breath --output graph --fast_exit

## Help
```
usage: main.py [-h] --level LEVEL --start START --file FILE --visit VISIT [VISIT ...] --algorithm {breath,depth} [--fast_exit] [--benchmark]
               [--output {graph,text,stats}] [--max_visits MAX_VISITS]

Path find over railML

optional arguments:
  -h, --help            show this help message and exit
  --level LEVEL         Level to path find on
  --start START         Element to start on
  --file FILE           RailML file
  --visit VISIT [VISIT ...]
                        Elements to vist
  --algorithm {breath,depth}
                        Algorithm to use
  --fast_exit           Exit as soon as path found usefull for breath algorithm
  --benchmark           Benchmark stats
  --output {graph,text,stats}
                        Output format
  --max_visits MAX_VISITS
                        Max number of times to visit each node
```