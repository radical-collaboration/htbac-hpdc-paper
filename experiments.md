# List of experiments

## Adaptive experiments

These are experiments concerning adaptivity. Adaptivity can mean a number of concepts, but in general the idea is that the workflow is dynamically altered at runtime based on decision points. This is implemented in `Abigail` to do adaptive thermodynamic integration, inter protocol adaptivity and more.

###  Adaptive thermodynamic integration

1. **Benchmark / base line (including non-adaptive)**: in order to compare the adaptive vs non-adaptive integration algorithm, we have to have an accurate description of the integrated function. Therefore as the base-line we will run a very detailed (_129_ equally spaced lambda windows) experiment for every investigated system. There is no other way to compare adapt and non-adapt results. Running this fine grained simulation also produces the non-adaptive results (which is _9 or 17_ equally spaced lambda windows). Usually we ran 5 replicas to get a good error estimate on the individual windows. Depending on how well converged the results are we might want to run even more. _These window numbers (129, 17, 9) come from the fact that we are using the bisection method._

2. **Adaptive:** using the adpative quadrature algorithm we run 1 ns simulations, evaluate and add more windows where required. 

#### Systems

We are going to run on a wide range of protein and ligand combinations to validate our results. Namely proteins mcl1, ptp1b and tyk2 each with two different ligand tranformation.

#### Measure of "betterness"

I can think of at least two measures. _dG_t_ is calculated from the very fine integration. _dG_adapt_ and _dG_non-adapt_ are self explanatory. e_adapt = |dG_t - dG_adapt|

1. e_adapt < e_non-adapt,  i.e. the error is smaller give the same amount of lambda windows (more accurate).
2. e_adapt ~= e_non-adapt, but with less lamda windows (more efficient), i.e. we reach the error tolerance with less lambda windows. 

We could show both in the paper.

### _Inter_ protocol adaptivity:

Jumana is currently testing hybdrid ESMACS/TIES runs on BW, which is step 1 to implementing this type of adaptivity.
