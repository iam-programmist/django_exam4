from django.db import models

class Country(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class City(models.Model):
    country = models.ForeignKey(Country, on_delete = models.CASCADE, related_name = 'cities')
    name = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.country} - {self.name}'

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15, unique = True)
    email = models.EmailField(max_length = 100, unique=True)
    image = models.ImageField(upload_to = 'static/images', null = True, blank = True)
    country = models.ForeignKey(Country, on_delete = models.CASCADE, related_name = 'user_country')
    city = models.ForeignKey(City, on_delete = models.CASCADE, related_name = 'user_city')
    is_driver = models.BooleanField(default = False)
    is_passenger = models.BooleanField(default = False)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.username} - {self.age} - {self.phone_number} - {self.email} - {self.country} - {self.city} - {self.is_driver} - {self.is_passenger}'

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    car_model = models.CharField(max_length=100)
    car_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.user} - {self.car_model} - {self.car_number}'

class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger')
    rating = models.FloatField(default=0)

    def __str__(self):
        return f'{self.user} - {self.rating}'

class Trip(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='trips')
    destination = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    available_seats = models.IntegerField()
    price_per_seat = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.driver} - {self.destination} - {self.start_time} - {self.available_seats} - {self.price_per_seat}'

class Booking(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='bookings')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='bookings')
    seats_reserved = models.IntegerField()

    def __str__(self):
        return f'{self.trip} - {self.passenger} - {self.seats_reserved}'

class DriverRating(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='ratings')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.trip} - {self.passenger} - {self.rating} - {self.review}'

class Route(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='routes')
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    distance_km = models.IntegerField()

    def __str__(self):
        return f'{self.start_point} - {self.end_point} - {self.distance_km}'

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return f'{self.title} - {self.description} - {self.start_time} - {self.end_time} - {self.location} - {self.driver}'

class Payment(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='payments')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.trip} - {self.passenger} - {self.amount} - {self.paid_at}'

class TripLog(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='logs')
    log_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.trip} - {self.log_message} - {self.created_at}'

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} - {self.receiver} - {self.content} - {self.sent_at}'
