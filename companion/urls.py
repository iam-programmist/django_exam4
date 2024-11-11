from django.urls import path
from .views import *

urlpatterns = [
    path('', CountryListView.as_view(), name='country_list'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='country_detail'),
    path('countries/create/', CountryCreateView.as_view(), name='country_create'),
    path('countries/<int:pk>/update/', CountryUpdateView.as_view(), name='country_update'),
    path('countries/<int:pk>/delete/', CountryDeleteView.as_view(), name='country_delete'),

    path('cities/', CityListView.as_view(), name='city_list'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path('cities/create/', CityCreateView.as_view(), name='city_create'),
    path('cities/<int:pk>/update/', CityUpdateView.as_view(), name='city_update'),
    path('cities/<int:pk>/delete/', CityDeleteView.as_view(), name='city_delete'),

    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    path('drivers/', DriverListView.as_view(), name='driver_list'),
    path('drivers/<int:pk>/', DriverDetailView.as_view(), name='driver_detail'),
    path('drivers/create/', DriverCreateView.as_view(), name='driver_create'),
    path('drivers/<int:pk>/update/', DriverUpdateView.as_view(), name='driver_update'),
    path('drivers/<int:pk>/delete/', DriverDeleteView.as_view(), name='driver_delete'),

    path('passengers/', PassengerListView.as_view(), name='passenger_list'),
    path('passengers/<int:pk>/', PassengerDetailView.as_view(), name='passenger_detail'),
    path('passengers/create/', PassengerCreateView.as_view(), name='passenger_create'),
    path('passengers/<int:pk>/update/', PassengerUpdateView.as_view(), name='passenger_update'),
    path('passengers/<int:pk>/delete/', PassengerDeleteView.as_view(), name='passenger_delete'),

    path('trips/', TripListView.as_view(), name='trip_list'),
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip_detail'),
    path('trips/create/', TripCreateView.as_view(), name='trip_create'),
    path('trips/<int:pk>/update/', TripUpdateView.as_view(), name='trip_update'),
    path('trips/<int:pk>/delete/', TripDeleteView.as_view(), name='trip_delete'),

    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking_create'),
    path('bookings/<int:pk>/update/', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),

    path('driver-ratings/', DriverRatingListView.as_view(), name='driverrating_list'),
    path('driver-ratings/<int:pk>/', DriverRatingDetailView.as_view(), name='driverrating_detail'),
    path('driver-ratings/create/', DriverRatingCreateView.as_view(), name='driverrating_create'),
    path('driver-ratings/<int:pk>/update/', DriverRatingUpdateView.as_view(), name='driverrating_update'),
    path('driver-ratings/<int:pk>/delete/', DriverRatingDeleteView.as_view(), name='driverrating_delete'),

    path('routes/', RouteListView.as_view(), name='route_list'),
    path('routes/<int:pk>/', RouteDetailView.as_view(), name='route_detail'),
    path('routes/create/', RouteCreateView.as_view(), name='route_create'),
    path('routes/<int:pk>/update/', RouteUpdateView.as_view(), name='route_update'),
    path('routes/<int:pk>/delete/', RouteDeleteView.as_view(), name='route_delete'),

    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),

    path('payments/', PaymentListView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
    path('payments/create/', PaymentCreateView.as_view(), name='payment_create'),
    path('payments/<int:pk>/update/', PaymentUpdateView.as_view(), name='payment_update'),
    path('payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment_delete'),

    path('trip-logs/', TripLogListView.as_view(), name='triplog_list'),
    path('trip-logs/<int:pk>/', TripLogDetailView.as_view(), name='triplog_detail'),
    path('trip-logs/create/', TripLogCreateView.as_view(), name='triplog_create'),
    path('trip-logs/<int:pk>/update/', TripLogUpdateView.as_view(), name='triplog_update'),
    path('trip-logs/<int:pk>/delete/', TripLogDeleteView.as_view(), name='triplog_delete'),

    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]
