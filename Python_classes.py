
class Vehicle:
    model = 'Nismo'
    manufacturer = 'Nissan'
    engine = 'gasoline'
    fuel = 'Unleaded'

class Aircraft(Vehicle):
    vehicle_type = 'prop'
    speed = '300'
    altitude = '15,000 feet'

class Ship(Vehicle):
    vehicle_range = 'knots'
    propulsion = 'hydrojet'
