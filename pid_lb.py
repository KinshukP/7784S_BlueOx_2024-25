from vex import *
# test
# Begin project code
LbStates = [0, 50, 125]
CurrentStateIndex = 0
def Next_State():
    global CurrentStateIndex, LbStates
    CurrentStateIndex +=1;
    if (CurrentStateIndex == 3):
        CurrentStateIndex = 0
    lb.spin_to_position(LbStates[CurrentStateIndex, DEGREES,wait=False)
def Lift_Control():
    kp = 1
    error = LbStates[CurrentStateIndex] - RotationSensor.position(DEGREES)
    Velocity = kp * error
    lb.velocity(Velocity)
if controller_1.buttonL2.pressing():
    Next_State()
while true:
    Lift_Control():


    
LbStates = [0, 250, 125]
CurrentStateIndex = 0
def Next_State():
    global CurrentStateIndex, LbStates
    CurrentStateIndex += 1;
    if (CurrentStateIndex == 3):
        CurrentStateIndex = 0
    kp = 1
    error = LbStates[CurrentStateIndex] - RotationSensor.position(DEGREES)
    while error == 0:
        correctedDegreesToMove = kp * error
        lb.spin_to_position(correctedDegreesToMove,DEGREES)
        error = LbStates[CurrentStateIndex] - RotationSensor.position(DEGREES)
        print(error)
