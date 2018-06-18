import htbac.protocols.TIES
ties_1 = Protocol(system = 'brd4-1')
sim = Simulation(name = 'Production MD')
        ... # define simulation conditions 
sim.ensemble('replica', range(5))
sim.ensemble('lambda', range(13))
# add simulation configurations to protocol
TIES.step0 = sim
ties_1.append(TIES.step0)
# assign resources, append protocol to Runner 
runner = Runner(resource = 'ncsa.blue_waters',
                walltime = 60) 
runner.add_protocol(protocol = ties_1)
# launch application
runner.run()