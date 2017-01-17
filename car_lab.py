class Car(object):
    name = 'General'
    model = 'GM'
    car_type = 'saloon'
    speed = 0
  
  def __init__(self, n = 'General', m = 'GM', t = 'saloon'):
    self.name = n
    self.model = m
    self.car_type = t
    self.num_of_doors = 2 if(n is 'Koenigsegg' or n is 'Porshe') else 4
    self.num_of_wheels = 8 if(t is 'trailer') else 4
    self.speed = 0
    
  def is_saloon(self):
    return self.car_type is 'saloon'
  
  def drive(self, gear):
    self.speed = 11*gear if(self.car_type is 'trailer') else int(round(333.333*gear))
    return self
