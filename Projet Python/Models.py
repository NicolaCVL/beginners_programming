class Models:
    
    def __init__(self, power, fuel, consumption)
        self.power = power
        self.fuel = fuel
        self.consumption = consumption

    def power():
        set_car_powers{
            car_powers_audi = [a, a1, a2, a3, a4];
            car_powers_bmw = [b, b1, b2, b3, b4];
            car_powers_mercedez = [m, m1, m2, m3, m4];
            car_powers_astonMartin = [aM, aM1, aM2, aM3, aM4]
        }
        return power()


    def fuel():
        set_different_fuels
        {
            car_fuels_benzine95 = "Essence SP95";
            car_fuels_benzine98 = "Essence SP98";
            car_fuels_diesel = "Diesel"
        }
        return fuel()

    def consumption():
        set_cars_consumption{
            cars_consumption_audi = [];
            car_consumption_bmw = [];
            car_consumption_mercedez = [];
            car_consumption_astonMartin = []
        }
        return consumption()


if __name__ == "__main__":

    set_Models = Models()
    
    set_car_Models = []

    for find_models in Models:
        set_car_Models.append(Models(set_Models["power"], set_Models["fuel"], set_Models["consumption"]))
