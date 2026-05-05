from aircraft import Aircraft
 
print("Enter aircraft model:")
model = input()
 
plane = Aircraft(model)
 
while True:
    print("Enter command (A for ascent, D for descent, X to exit):")
    command = input()
 
    space = command.find(' ')
 
    if command == 'X':
        break
 
    elif command[0] == 'A':
        feet = int(command[space + 1:])
        plane.ascend(feet)
 
    elif command[0] == 'D':
        feet = int(command[space + 1:])
        plane.descend(feet)
 
print(f"Final altitude: {plane.altitude} feet")