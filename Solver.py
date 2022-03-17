from sys import modules
from numpy.lib.function_base import delete
import Core
import numpy as np
import logger


class Solver:
    # people count to be moved to factory container
    maxSteps = 1000 # roughly 4 weeks 
    stepCount = 0
    stepSize = 10 # in minutes
    modulesToBuild = np.array([])
    modulesInProgress = np.array([])
    modulesComplete = np.array([])
    scenario = Core.Scenario()
    #log = {'',[]}

    def __init__(self):
        pass


    def __init__(self,scenario,stepSize,modulesToBuild):
        self.scenario = scenario
        self.stepSize = stepSize
        self.modulesToBuild = modulesToBuild
        #logger.Logger.createCSV("solverLogger")
        #logger.Logger.openFile("solverLogger")
        #for station in self.scenario.stations:
            # add an entry to log
            #self.log.add()



    def solve(self):
        #do the buissssnness
        print("Solver begining")
        print(self.scenario.description)
        print("Modules to assemble : ", len(self.modulesToBuild))
        print("Station count : ",  str(len(self.scenario.stations)))
        self.stepCount = 0
        totalmoduleCount = len(self.modulesToBuild)
        while self.stepCount < self.maxSteps : # and len(self.modulesComplete) < totalmoduleCount
            self.step()
            self.stepCount += 1 # step count does not relate to step size for now
        self.export()
        print(" Solver finishing")

        

    def export(self):
        count = 1
        for station in self.scenario.stations:
            logger.Logger.createCSV('station_'+str(count) + '_Log',station.pLog)
            #print("station Log : ",station.pLog)
            count += 1

    def step(self):
        print("step taken : ", str(self.stepCount))
        # updated tasks to station
        for station in self.scenario.stations:
            # is station occupied?
            if station.activeTask.description == Core.Task.empty().description:
                print("Station ",station.description ," is Empty, will attempt to add new module")
                self.trySetNextModule(station)
            else:
                # Is station current task complete?
                self.trySetNextTask(station)
                print(str(station.module.type),str(station.activeTask.description),str(station.activeTask.state.name), " : ", str(station.activeTask.durationTaken), "/",str(station.activeTask.duration))
            
            # add step size onto all active task, could move it for loop above
            if station.activeTask.state == Core.taskState.Actived or station.activeTask.state == Core.taskState.NotStarted:
                station.activeTask.addDurationComplete(self.stepSize)
            station.log()
        #print(station.description, str(station.activeTask.state))

       # add step size onto all active task, could move it for loop above
        #for station in self.scenario.stations:
         #   if station.activeTask.state == Core.taskState.Actived or station.activeTask.state == Core.taskState.NotStarted:
         #       station.activeTask.addDurationComplete(self.stepSize)
         #   station.log()



    def trySetNextTask(self, station):
        if station.activeTask.state == Core.taskState.Complete:
            # set next task
            #print("task completed : ", str(station.activeTask.description))
            # find out what next task is
            newTask = station.module.getNextOrActiveTask()
            if newTask is None: # must be complete
                self.trySetNextModule(station)
            else:
                station.activeTask = newTask

    def isComplete(self, module):
        newTask = module.getNextOrActiveTask()
        if newTask is None: # must be complete
            return True
        return False

    def trySetNextModule(self, station):
        # pop next module and add to station
        # Ask if station can perfom task (look at available resources)
        # set task to station

        if(self.isComplete(station.module)):
            self.modulesComplete = np.append(self.modulesComplete,[station.module])


        # todo: check if modules exist
        if self.modulesToBuild.size == 0:
            return
        _newModule = self.modulesToBuild[0]
        try:
            _newModule
        except NameError:
            return
        #self.modulesToBuild.remove(_newModule
        self.modulesToBuild = np.delete(self.modulesToBuild,0)
        self.modulesInProgress = np.append(self.modulesInProgress,[_newModule])
        station.module = _newModule
        station.activeTask = _newModule.taskList[0]
        #print(" new module set :", _newModule.type)
        #print(" new active task set :", str(station.activeTask.index))



