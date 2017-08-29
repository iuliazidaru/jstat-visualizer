**Visualize Offline `jstat` output**

Tool used to visualize JStat output from a file. It is useful when a multiday output has to be analyzed, in contrast to realtime data.

**Example output**



**Execution**

Run jstat with -gcutil option, add timestamp and redirect the output to a file.

`jstat -gcutil  8944 10s | ./addDate.sh >> jstatEclipse.log
`

Create the graphs:

`python jstat-graph.py gcutilSY-wrongGCopt.log`

