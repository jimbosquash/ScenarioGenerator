import Core
import Solver
import numpy as np
class module_DB_Test:
    
    stations_test = np.array([])
    modules = np.array([])
    moduleTaskIndexs = np.array([
        [1,2,3,4,5,6,7,8,9,10,11,13,14],
        [1,2,3,4,5,10,11,14],
        [1,2,3,4,5,6,7,8,9,10,11,13,14],
        [1,2,3,4,5,6,7,8,9,10,11,14],
        [1,2,3,4,5,10,11,14],
        [1,2,3,4,5,6,7,8,9,14],
        [1,2,3,4,5,6,7,8,9,14],
        [1,2,3,4,5,12,14],
        [1,2,3,4,5,6,7,8,9,14],
        [1,2,3,4,5,14]
        ])

    # create tasks in creation method and use list index instead
    #defaultTask = Core.Task.default()
    emptyTask = Core.Task.empty() # keeps task count starting from 1
    task1 = Core.Task()
    task2 = Core.Task()
    task3 = Core.Task()
    task4 = Core.Task()
    task5 = Core.Task()
    task6 = Core.Task()
    task7 = Core.Task()
    task8 = Core.Task()
    task9 = Core.Task()
    task10 = Core.Task()
    task11 = Core.Task()
    task12 = Core.Task()
    task13 = Core.Task()
    task14 = Core.Task()
    tasks = [emptyTask,task1,task2,task3,task4,task5,task6,task7,task8,task9,task10,task11,task12,task13,task14]

    def __init__(self): 
        self.CreateDB()
        
    
    def CreateDB(self):
        print("module_DB test : getting set up")
        self.CreateTestTasks()
        #self.PrintTask()

        counter = 0
        for taskSet in self.moduleTaskIndexs:
            # create a set of tasks
            module = self.CreateModule(str(counter),taskSet,counter)
            self.modules = np.append(self.modules,[module])
            counter+=1
            
            
        self.CreateTest_Stations()

        print("module_DB test : Data Base created \n")

        
    def CreateModule(self,mType,taskIndexList,mId):
        
        #using task list array get tasks from tasks
        duplicatedTasks = np.array([])
        for index in taskIndexList:
            dupTask = self.tasks[index].duplicate()
            duplicatedTasks = np.append(duplicatedTasks,[dupTask])

        module = Core.Module(mType,duplicatedTasks)
        module.id = mId
        module.print()
        return module


    def PrintTask(self):
        for task in self.tasks:
            task.print()
        

    def CreateTestTasks(self):
        #print("module_DB test : creating tasks ")
        self.task1.index = 1
        self.task1.description = "Floor - structure, plates"
        self.task1.duration = 40
        self.task1.minimumPersonnel = 2
        self.task1.minimumSpace = 28
        self.task1.actualSpace = 37.6
        self.task1.actualDuration = 18

        self.task2.index = 2
        self.task2.description = "Floor - insulation, installations"
        self.task2.duration = 40
        self.task2.minimumPersonnel = 2
        self.task2.minimumSpace = 28
        self.task2.actualSpace = 29.5
        self.task2.actualDuration = 18

        self.task3.index = 3
        self.task3.description = "Ceiling - structure, plates"
        self.task3.duration = 40
        self.task3.minimumPersonnel = 2
        self.task3.minimumSpace = 28
        self.task3.actualSpace = 37.6    
        self.task3.actualDuration = 18

        self.task4.index = 4
        self.task4.description = "Ceiling - installations"
        self.task4.duration = 40
        self.task4.minimumPersonnel = 2
        self.task4.minimumSpace = 28
        self.task4.actualSpace = 30.25    
        self.task4.actualDuration = 18

        self.task5.index = 5
        self.task5.description = "Module - casco - floor ceiling, columns"
        self.task5.duration = 30
        self.task5.minimumPersonnel = 2
        self.task5.minimumSpace = 28
        self.task5.actualSpace = 32.8  
        self.task5.actualDuration = 14

        self.task6.index = 6
        self.task6.description = "Facade - Structure, plates"
        self.task6.duration = 120
        self.task6.minimumPersonnel = 2
        self.task6.minimumSpace = 28
        self.task6.actualSpace = 31.9    
        self.task6.actualDuration = 58

        self.task7.index = 7
        self.task7.description = "Facade - insulation, foil, electrics, HVAC"
        self.task7.duration = 180
        self.task7.minimumPersonnel = 1
        self.task7.minimumSpace = 28
        self.task7.actualSpace = 29.5    
        self.task7.actualDuration = 175

        self.task8.index = 8
        self.task8.description = "Facade - Windows"
        self.task8.duration = 60
        self.task8.minimumPersonnel = 2
        self.task8.minimumSpace = 28
        self.task8.actualSpace = 39.5
        self.task8.actualDuration = 29

        self.task9.index = 9
        self.task9.description = "Module - Add facades"
        self.task9.duration = 90
        self.task9.minimumPersonnel = 2
        self.task9.minimumSpace = 28
        self.task9.actualSpace = 28    
        self.task9.actualDuration = 43

        self.task10.index = 10
        self.task10.description = "Partition wall - Structure, plates"
        self.task10.duration = 120
        self.task10.minimumPersonnel = 2
        self.task10.minimumSpace = 28
        self.task10.actualSpace = 31.9    
        self.task10.actualDuration = 58

        self.task11.index = 11
        self.task11.description = "Module - Add partition walls, add doors"
        self.task11.duration = 180
        self.task11.minimumPersonnel = 2
        self.task11.minimumSpace = 28
        self.task11.actualSpace = 29.5    
        self.task11.actualDuration = 88

        self.task12.index = 12
        self.task12.description = "Module - Installations in tech space"
        self.task12.duration = 240
        self.task12.minimumPersonnel = 2
        self.task12.minimumSpace = 29.5
        self.task12.actualSpace = 30.25  
        self.task12.actualDuration = 115

        self.task13.index = 13
        self.task13.description = "Module - Tiling and wet cell furniture"
        self.task13.duration = 240
        self.task13.minimumPersonnel = 1
        self.task13.minimumSpace = 28
        self.task13.actualSpace = 333.25    
        self.task13.actualDuration = 240

        self.task14.index = 14
        self.task14.description = "Module - Put on transport"
        self.task14.duration = 30
        self.task14.minimumPersonnel = 1
        self.task14.minimumSpace = 28
        self.task14.actualSpace = 38    
        self.task14.actualDuration = 27
        print("module_DB test : created",str(len(self.tasks)), "task types \n")



    def CreateTest_Stations(self):
        allTaskIds = np.array([])
        for index in range(len(self.tasks)):
            allTaskIds = np.append(allTaskIds,[index])
        
        stationCount = 5

        for i in range(stationCount):
            station = Core.Station(allTaskIds)
            station.description = "complete station"
            station.id = i 
            self.stations_test = np.append(self.stations_test,[station])
        print("module_DB test : created",str(stationCount), "test stations \n")


    def launchTestSolver(self, dB_test):
        print("Test Solver launching")
        scenario = Core.Scenario()
        scenario.stations = dB_test.stations_test
        scenario.description = "Test Scenario with : " + str(len(dB_test.modules))
        solver = Solver.Solver(scenario,10,dB_test.modules)
        solver.solve()