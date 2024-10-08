from rest_framework import serializers

from .models import *


class ShipSerializer(serializers.ModelSerializer):
    def get_image(self, ship):
        return ship.image.url.replace("minio", "localhost", 1)

    class Meta:
        model = Ship
        fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
    ships = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    moderator = serializers.SerializerMethodField()

    def get_owner(self, flight):
        return flight.owner.username

    def get_moderator(self, flight):
        if flight.moderator:
            return flight.moderator.username
            
    def get_ships(self, flight):
        items = ShipFlight.objects.filter(flight=flight)
        serializer = ShipSerializer([item.ship for item in items], many=True)
        return serializer.data

    class Meta:
        model = Flight
        fields = '__all__'


class FlightsSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    moderator = serializers.SerializerMethodField()

    def get_owner(self, flight):
        return flight.owner.username

    def get_moderator(self, flight):
        if flight.moderator:
            return flight.moderator.username

    class Meta:
        model = Flight
        fields = "__all__"


class ShipFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipFlight
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'date_joined', 'password', 'username')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)