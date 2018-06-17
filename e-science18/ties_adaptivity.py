# creating a customized adaptive TIES protocol 
import htbac.protocols.Rfe
ties_1 = Protocol(system = 'e255k')
        ...
sim = Simulation(name = 'production MD phase 1')
        ...  
sim.ensemble('replica', range(5))
sim.ensemble('lambda' , range(3))

Rfe.step3 = sim
ties_1.append(Rfe.step3)

runner = Runner() 
runner.add_protocol(protocol = ties_1)

# writes simulation output, 
# bypasses application termination
runner.run(save_output = True, terminate = False)

# adaptivity script 
requested_windows = AdaptiveQuadrature()
sim1 = Simulation(name = 'production MD phase 2')
        ... 
sim1.ensemble('replica', range(5))
sim1.ensemble('additional lambdas', requested_windows)

Rfe.step4 = sim1
ties_1.append(Rfe.step4)
runner.run(protocol = ties_1, terminate = True)

