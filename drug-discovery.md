Binding free energy protocols like TIES, have the potential to replace parts of 
the current drug discovery pipeline in the pharmaceutical industry. Currently, 
execution of these protocols lacks the scale and turnaround time required for 
decision making in an industrial profit driven setting. For example, the lead 
optimization stage usually considers on the order of 10000 small molecules by 
calculating the binding affinity in vivo. While experiment automation reduces 
completion time, the in silico variant has the potential to cut time to 
completion and cost by an order of magnitude.

TIES requires around 25000 CPU core hours for 1 prediction, meaning a large 
scale study is on the order of a quarter billion core hours. Adaptivity in 
HTBAC can reduce this time by a factor of 10, still, the framework provided by 
the Radical is needed. Depending on the computational resources available, this 
is equivalent to a turnaround time of about 2 weeks.

- Quality adaptivity: changing the error threshold for faster turnaround times.
(task attribute adaptivity) Error as a function of candidate number?

- Adaptive quadrature: decrease the core hours requirements per prediction due 
to adaptivity (task count adaptivity, task attribute adaptivity)

- Overview: what is our throughput, i.e. how many leads can we run?
