
class Investment:

    def __init__(self,number_of_assets = 5):
        self.assets = []
        for x in range(number_of_assets):
            self.assets.append(0)
        
    def maxValue(self,round):
        for x in range(round[0] - 1,round[1]):
            self.assets[x] = self.assets[x] + round[2]

    def show_assets(self):
        print(str(self.assets))


