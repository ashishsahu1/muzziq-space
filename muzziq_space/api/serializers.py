#this file will take the keys of model nd then turn ino strings and jsonify it to send 
from rest_framework import serializers
from .models import Room

class RoomSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','code','host','guest_can_pause','votes_to_skip','created_at')
