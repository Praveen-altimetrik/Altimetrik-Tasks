class Vehicle:
    
    __name = "pulsar"

    def display():
        print(Vehicle.__name)

class Bike(Vehicle):
    
    def display():
        print(Vehicle.__name)
    
def main():
    Vehicle.display()
    Bike.display()

if __name__ == "__main__":
    main()