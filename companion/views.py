from .models import Country, City, User, Driver, Passenger, Trip, Booking, DriverRating, Route, Event, Payment, TripLog, Message
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CountryListView(ListView):
    model = Country
    template_name = 'country_list.html'
    context_object_name = 'countries'

class CountryDetailView(DetailView):
    model = Country
    template_name = 'country_detail.html'
    context_object_name = 'country'

class CountryCreateView(CreateView):
    model = Country
    template_name = 'country_form.html'
    fields = ['name']
    success_url = reverse_lazy('city_list')

class CountryUpdateView(UpdateView):
    model = Country
    template_name = 'country_form.html'
    fields = ['name']
    success_url = reverse_lazy('city_list')

class CountryDeleteView(DeleteView):
    model = Country
    template_name = 'country_confirm_delete.html'
    success_url = reverse_lazy('city_list')

class CityListView(ListView):
    model = City
    template_name = 'city_list.html'
    context_object_name = 'cities'

class CityDetailView(DetailView):
    model = City
    template_name = 'city_detail.html'
    context_object_name = 'city'

class CityCreateView(CreateView):
    model = City
    template_name = 'city_form.html'
    fields = ['country', 'name']
    success_url = reverse_lazy('user_list')

class CityUpdateView(UpdateView):
    model = City
    template_name = 'city_form.html'
    fields = ['country', 'name']
    success_url = reverse_lazy('user_list')

class CityDeleteView(DeleteView):
    model = City
    template_name = 'city_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = User
    template_name = 'user_form.html'
    fields = ['first_name', 'last_name', 'username', 'age', 'phone_number', 'email', 'image', 'country', 'city', 'is_driver', 'is_passenger']
    success_url = reverse_lazy('trip_list')

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_form.html'
    fields = ['first_name', 'last_name', 'username', 'age', 'phone_number', 'email', 'image', 'country', 'city', 'is_driver', 'is_passenger']
    success_url = reverse_lazy('trip_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('trip_list')

class DriverListView(ListView):
    model = Driver
    template_name = 'driver_list.html'
    context_object_name = 'drivers'

class DriverDetailView(DetailView):
    model = Driver
    template_name = 'driver_detail.html'
    context_object_name = 'driver'

class DriverCreateView(CreateView):
    model = Driver
    template_name = 'driver_form.html'
    fields = ['user', 'car_model', 'car_number']
    success_url = reverse_lazy('passenger_list')

class DriverUpdateView(UpdateView):
    model = Driver
    template_name = 'driver_form.html'
    fields = ['user', 'car_model', 'car_number']
    success_url = reverse_lazy('passenger_list')

class DriverDeleteView(DeleteView):
    model = Driver
    template_name = 'driver_confirm_delete.html'
    success_url = reverse_lazy('passenger_list')

class PassengerListView(ListView):
    model = Passenger
    template_name = 'passenger_list.html'
    context_object_name = 'passengers'

class PassengerDetailView(DetailView):
    model = Passenger
    template_name = 'passenger_detail.html'
    context_object_name = 'passenger'

class PassengerCreateView(CreateView):
    model = Passenger
    template_name = 'passenger_form.html'
    fields = ['user', 'rating']
    success_url = reverse_lazy('route_list')

class PassengerUpdateView(UpdateView):
    model = Passenger
    template_name = 'passenger_form.html'
    fields = ['user', 'rating']
    success_url = reverse_lazy('route_list')

class PassengerDeleteView(DeleteView):
    model = Passenger
    template_name = 'passenger_confirm_delete.html'
    success_url = reverse_lazy('route_list')

class TripListView(ListView):
    model = Trip
    template_name = 'trip_list.html'
    context_object_name = 'trips'

class TripDetailView(DetailView):
    model = Trip
    template_name = 'trip_detail.html'
    context_object_name = 'trip'

class TripCreateView(CreateView):
    model = Trip
    template_name = 'trip_form.html'
    fields = ['driver', 'destination', 'start_time', 'available_seats', 'price_per_seat']
    success_url = reverse_lazy('booking_list')

class TripUpdateView(UpdateView):
    model = Trip
    template_name = 'trip_form.html'
    fields = ['driver', 'destination', 'start_time', 'available_seats', 'price_per_seat']
    success_url = reverse_lazy('booking_list')

class TripDeleteView(DeleteView):
    model = Trip
    template_name = 'trip_confirm_delete.html'
    success_url = reverse_lazy('booking_list')

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'
    context_object_name = 'booking'

class BookingCreateView(CreateView):
    model = Booking
    template_name = 'booking_form.html'
    fields = ['trip', 'passenger', 'seats_reserved']
    success_url = reverse_lazy('driver_list')

class BookingUpdateView(UpdateView):
    model = Booking
    template_name = 'booking_form.html'
    fields = ['trip', 'passenger', 'seats_reserved']
    success_url = reverse_lazy('driver_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('driver_list')

class DriverRatingListView(ListView):
    model = DriverRating
    template_name = 'driverrating_list.html'
    context_object_name = 'driver_ratings'

class DriverRatingDetailView(DetailView):
    model = DriverRating
    template_name = 'driverrating_detail.html'
    context_object_name = 'driver_rating'

class DriverRatingCreateView(CreateView):
    model = DriverRating
    template_name = 'driverrating_form.html'
    fields = ['trip', 'passenger', 'rating', 'review']
    success_url = reverse_lazy('event_list')

class DriverRatingUpdateView(UpdateView):
    model = DriverRating
    template_name = 'driverrating_form.html'
    fields = ['trip', 'passenger', 'rating', 'review']
    success_url = reverse_lazy('event_list')

class DriverRatingDeleteView(DeleteView):
    model = DriverRating
    template_name = 'driverrating_confirm_delete.html'
    success_url = reverse_lazy('event_list')

class RouteListView(ListView):
    model = Route
    template_name = 'route_list.html'
    context_object_name = 'routes'

class RouteDetailView(DetailView):
    model = Route
    template_name = 'route_detail.html'
    context_object_name = 'route'

class RouteCreateView(CreateView):
    model = Route
    template_name = 'route_form.html'
    fields = ['trip', 'start_point', 'end_point', 'distance_km']
    success_url = reverse_lazy('event_list')

class RouteUpdateView(UpdateView):
    model = Route
    template_name = 'route_form.html'
    fields = ['trip', 'start_point', 'end_point', 'distance_km']
    success_url = reverse_lazy('event_list')

class RouteDeleteView(DeleteView):
    model = Route
    template_name = 'route_confirm_delete.html'
    success_url = reverse_lazy('event_list')

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    template_name = 'event_form.html'
    fields = ['title', 'description', 'start_time', 'end_time', 'location', 'driver']
    success_url = reverse_lazy('payment_list')

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'event_form.html'
    fields = ['title', 'description', 'start_time', 'end_time', 'location', 'driver']
    success_url = reverse_lazy('payment_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('payment_list')

class PaymentListView(ListView):
    model = Payment
    template_name = 'payment_list.html'
    context_object_name = 'payments'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment_detail.html'
    context_object_name = 'payment'

class PaymentCreateView(CreateView):
    model = Payment
    template_name = 'payment_form.html'
    fields = ['trip', 'passenger', 'amount']
    success_url = reverse_lazy('trip_log_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    template_name = 'payment_form.html'
    fields = ['trip', 'passenger', 'amount']
    success_url = reverse_lazy('trip_log_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('trip_log_list')

class TripLogListView(ListView):
    model = TripLog
    template_name = 'triplog_list.html'
    context_object_name = 'trip_logs'

class TripLogDetailView(DetailView):
    model = TripLog
    template_name = 'triplog_detail.html'
    context_object_name = 'trip_log'

class TripLogCreateView(CreateView):
    model = TripLog
    template_name = 'triplog_form.html'
    fields = ['trip', 'log_message']
    success_url = reverse_lazy('message_list')

class TripLogUpdateView(UpdateView):
    model = TripLog
    template_name = 'triplog_form.html'
    fields = ['trip', 'log_message']
    success_url = reverse_lazy('message_list')

class TripLogDeleteView(DeleteView):
    model = TripLog
    template_name = 'triplog_confirm_delete.html'
    success_url = reverse_lazy('message_list')

class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'

class MessageCreateView(CreateView):
    model = Message
    template_name = 'message_form.html'
    fields = ['sender', 'receiver', 'content']
    success_url = reverse_lazy('country_list')

class MessageUpdateView(UpdateView):
    model = Message
    template_name = 'message_form.html'
    fields = ['sender', 'receiver', 'content']
    success_url = reverse_lazy('country_list')

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy('country_list')
