class Temperature:
    def __init__(self, val, scale):
        self.val = val
        self.scale = scale
    def getCelsius(self):
        if self.scale == 'C':
            return self.val
        else:
            return 5 * (self.val - 32) / 9
    def getFarenheit(self):
        if self.scale == 'F':
            return self.val
        else:
            return ((9*self.val)/5) + 32

t = Temperature(100, 'F')
print(t.getCelsius())
print(t.getFarenheit())