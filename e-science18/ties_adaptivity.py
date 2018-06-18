# we start with the same previous implementation
# provide runner with two flags 
runner.run(save_output = True, terminate = False)
# specify adaptivity script 
requested_lambdas = AdaptiveQuadrature()
sim1 = Simulation(name = 'production MD 2')
        ... 
sim1.ensemble('replica', range(5))
sim1.ensemble('additional lambdas', 
    requested_lambdas)
TIES.step1 = sim1
ties_1.append(TIES.step1)
runner.add_protocol(protocol = ties_1)
runner.run(terminate = True)