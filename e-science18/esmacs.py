# creating a customized ESMACS protocol
import htbac.protocols.Esmacs
esmacs_1 = Protocol(system = 'e255k')
sim = Simulation(name = 'minimization')
        ... # define simulation conditions 
sim.ensemble('replica', range(25))
# add simulation configurations to protocol
Esmacs.step0 = sim
esmacs_1.append(Esmacs.step0)
# assign resources, append protocol to Runner 
runner = Runner(resource = 'ncsa.blue_waters',
                walltime = 60) 
runner.add_protocol(protocol = esmacs_1)
# launch application
runner.run()