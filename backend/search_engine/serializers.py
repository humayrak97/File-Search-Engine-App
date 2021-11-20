from rest_framework import serializers
from search_engine.models import People 
#serializers take the python model and turn it into JSON

# People Serializer works on the people database 
class PeopleSerializer(serializers.ModelSerializer):
  class Meta:
    model = People
    #every field from the database is fetched 
    fields = '__all__'
