class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.space_dict = {
            1: big,
            2: medium,
            3: small,
        }


    def addCar(self, carType: int) -> bool:
        self.space_dict[carType] -= 1
        if self.space_dict[carType]<0:
            return False
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)