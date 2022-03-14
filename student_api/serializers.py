from django.forms import CharField
from django.utils.timezone import now
from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length = 30)
#     last_name = serializers.CharField(max_length =30)
#     number = serializers.IntegerField(required = False)
    
#     #* we will need to define operations explicitly
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance
    
    

class StudentSerializer(serializers.ModelSerializer):
    #*instead adding another column in db
    days_since_joined = serializers.SerializerMethodField()
    #*to get __str__ method
    path = serializers.StringRelatedField()
    
    class Meta:
        model = Student
        fields = ["id", "first_name", 'path',"last_name", "number",'days_since_joined']
        # fields = '__all__'
        # exclude = ['number']
        
        
    def get_days_since_joined(self,obj):
        return (now()-obj.register_date).days
        
    def validate(self, attrs):
        #*check firstname and lastname is equal
        
        
        if attrs['first_name'] == attrs['last_name']:
            raise serializers.ValidationError('names are same')
        return attrs
    
    def validate_number(self, attrs):
        
        if attrs >100 :
            raise serializers.ValidationError('Bigger than 100')
        return attrs
    
    #* Write same name as field name
    def validate_first_name(self, attrs):
        
        if attrs == 'Mehmet':
            raise serializers.ValidationError('Mehmet')
        return attrs