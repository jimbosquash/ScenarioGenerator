from enum import Enum
import numpy as np
from numpy.core.fromnumeric import trace

class Module:
    # list of tasks
    id = 0
    type = "module Test"

    taskList = np.array([]) # should be read only or is it a reference to a dict?

    def __init__(self,iType, taskList):
        self.type = iType
        self.taskList = taskList

        def print(self):
            print(self.type)
            print(self.taskList.Count())

    def print(self):
        taskIdList = ", tasks : "
        for task in self.taskList:
            taskIdList += str( task.index) + " ,"
        print("Module -", self.type, taskIdList )

    def getType(self, new_type):
        self.type = new_type
    def getNextOrActiveTask(self):
        #complete = all(t for t in self.taskList if t.state == taskState.Complete)
        if all(self.testComplete(t) for t in self.taskList):            
            return None

        for task in self.taskList:
            if task.state == taskState.Complete:
                continue
            return task # should faile dbe returned?

    def testComplete(self, task):
        for task in self.taskList:
            if task.state != taskState.Complete:
                return False
        return True

    staticmethod
    def empty():
       module = Module("Empty",np.array([]))
       return module
              
        
class taskState(Enum):
    NotStarted = 0
    Actived = 1
    Paused = 2
    Complete = 3
    Failed = 4

class Task:

    index = 0
    description = "Set description"
    durationTaken = 0 # duration currently compelete
    duration = 0 # duration to complete task
    minimumPersonnel = 0
    minimumSpace = 0
    actualSpace = 0
    actualDuration = 0
    state = taskState.NotStarted

    staticmethod
    def default():
       dTask = Task()
       dTask.index = 0
       dTask.description = "Default task"
       return dTask


    staticmethod
    def empty():
       dTask = Task()
       dTask.index = 0
       dTask.description = "Empty"
       return dTask


    def _init_(self,index,description):
        self.index = index
        self.description = description

    def duplicate(self):
        dupTask = Task()
        dupTask.actualDuration = self.actualDuration
        dupTask.actualSpace = self.actualSpace
        dupTask.description = self.description
        dupTask.duration = self.duration
        dupTask.index = self.index
        dupTask.minimumPersonnel = self.minimumPersonnel
        dupTask.minimumSpace = self.minimumSpace
        return dupTask

    def print(self):
        index = ("task_" + str(self.index) + ":")
        print(index + " description : " + self.description)
        print(index + " State : " + self.state.name)
        print(index + " duration : " + str(self.duration))
        print(index + " minimumPersonnel : " + str(self.minimumPersonnel))
        print(index + " minimumSpace : " + str(self.minimumSpace))
        print(index + " actualSpace : " + str(self.actualSpace))
        print(index + " actualDuration : " + str(self.actualDuration))
        print()


    def GetTask(self, index):
        newTask = Task()
        newTask.index = index   
    def addDurationComplete(self, stepSize):
        self.durationTaken += stepSize
        # now check new state
        if self.durationTaken >= self.duration:
            self.state = taskState.Complete
            return
        if stepSize == 0:
            self.state = taskState.Paused
            return
        if self.durationTaken > 0:
            self.state = taskState.Actived




class Station:
    # station represents a space in an assembly hall where certain tasks are performed on a module or sub assembly
    id = 0
    minimumSpace = 0
    description = "Set description"
    module = Module.empty() # module currently being built
    tasksAvailable = np.array([]) # task id list
    activeTask = Task.empty()
    #Log = np.array(['Module number','task Number','total task time','time on task','task state'])# module number, task number, total time , time taken, station state
    Log = np.array(['Module number','task Number','total task time','time on task','task state'])# module number, task number, total time , time taken, station state
    pLog = [['M-id','Mod-type','Task-type','Total T-Time','Current T-time','T-state']]

    def __init__(self,taskIds):
        self.tasksAvailable = taskIds
        self.pLog = [['Mod-type','Task-type','Total T-Time','Current T-time','T-state']]


    def log(self):
        logInput = [self.module.id,self.module.type,self.activeTask.index , str(self.activeTask.duration) , str(self.activeTask.durationTaken) , str(self.activeTask.state)]
        self.Log = np.append(self.Log,logInput)
        self.pLog.append(logInput)
        #print(logInput)


class Scenario: # assembly hall scenario
    # could also be assembly hall
    people = 0
    stations = np.array([])
    description = "Description"


    def __init__(self,people,stations,description):
        self.people = people
        self.stations = stations
        self.description = description

    def __init__(self):
        self.description = "Empty Scenario"

        