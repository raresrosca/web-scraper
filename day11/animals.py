class Animal:
    noise = 'Rrrr' #noise is a property of class Animal
    def make_noise(self):
        print(f"{self.noise}")

    def set_noise(self, new_noise):
        self.noise = new_noise

class Wolf(Animal):
    noise = 'Grrr'