class lldparking:
   def __init__(self,four,tri,two):
      self.maxlimit = [four,tri,two]
      self.slot=[0,0,0]
   def addvehicle(self):
      print("0.four wheeler")
      print("1.tri wheeler")
      print("2.two wheeler")
      vehicleType=int(input())
      if(self.slot[vehicleType]<self.maxlimit[vehicleType]):
         self.slot[vehicleType] += 1
         return print("vehicle parked")
      return print("no space for parking")
   def remvehicle(self):
      if(max(self.slot)==0):
        return print("No vehicle in the parking zone") 
      print("0.four wheeler")
      print("1.tri wheeler")
      print("2.two wheeler")
      vehicleType=int(input())
      if(self.slot[vehicleType]>0):
        self.slot[vehicleType] -= 1
        return print("vehicle departured") 
      return print("no such vehicle's parked")  
totalspace = lldparking(1, 2, 3)
while(1):
    print("select an option:")    
    print("1.parking your vehicle?",end='   ')
    print("2.departing your vehicle?",end='   ')  
    print("3.No one's in the parking Zone !!")    
    opt=int(input())
    if(opt==1):
        totalspace.addvehicle()
    elif(opt==2):
        totalspace.remvehicle()
    elif(opt==3):
        break;
    else:
        print("select valid option")
    
        
    
    
    