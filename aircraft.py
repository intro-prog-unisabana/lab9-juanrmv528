# FREEZE CODE BEGIN
class Aircraft:
    def __init__(self, model):
        self.model = model
        self.altitude = 0
 
    def ascend(self, feet):
        self.altitude = self.altitude + feet
 
    def descend(self, feet):
        self.altitude = self.altitude - feet
# FREEZE CODE END