class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str,
                 ) -> None:
        self.clean_mark = clean_mark
        self.comfort_class = comfort_class
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income_counter = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income_counter += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income_counter, 1)

    def calculate_washing_price(self, cars: Car) -> float:
        price = (cars.comfort_class
                 * (self.clean_power - cars.clean_mark)
                 * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        general_rating = self.average_rating * self.count_of_ratings
        new_rating_count = self.count_of_ratings + 1
        self.average_rating = round((general_rating + rate)
                                    / new_rating_count, 1)
        self.count_of_ratings = new_rating_count
