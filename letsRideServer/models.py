from django.db import models

# Create your models here.
class Requests(models.Model):
    LAPTOP = 'Laptop'
    TRAVEL_BAG = 'TravelBag'
    PACKAGE = 'Package'
    NORMAL = 'Normal'
    SENSITIVE = 'Sensitive'
    HIGHLY_SENSITIVE = 'Highly Sensitive'
    PENDING = 'Pending'
    EXPIRED = 'Expired'
    STATUS = [
        (PENDING,'Pending'),
        (EXPIRED,'Expired'),
    ]
    ASSET_SENSITIVE = [
        (NORMAL, 'Normal'),
        (SENSITIVE, 'Sensitive'),
        (HIGHLY_SENSITIVE, 'Highly Sensitive'),
    ]
    ASSET_TYPE = [
        (LAPTOP, 'Laptop'),
        (TRAVEL_BAG, 'Travel Bag'),
        (PACKAGE, 'Package'),
    ]
    RequestId=models.AutoField(primary_key=True)
    RequesterEmailid=models.EmailField()
    From=models.CharField(max_length=25)
    To=models.CharField(max_length=25)
    RequesterDate = models.IntegerField(default=10)
    FlexibleDate=models.BooleanField(default=False)
    TotalAssets=models.IntegerField()
    Assettype = models.CharField(max_length=25, choices=ASSET_TYPE, default=LAPTOP)
    Assetsensitivity = models.CharField(max_length=25, choices=ASSET_SENSITIVE, default=NORMAL)
    Status = models.CharField(max_length=10,choices=STATUS,default=PENDING)
    DeliveryContact=models.IntegerField()


class Riders(models.Model):
    BUS = 'Bus'
    CAR = 'Car'
    TRAIN = 'Train'
    MEDIUM = [
        (BUS,'Bus'),
        (CAR,'Car'),
        (TRAIN,'Train'),
    ]
    RiderId=models.AutoField(primary_key=True)
    RiderEmailid=models.EmailField()
    RiderContact=models.IntegerField()
    From=models.CharField(max_length=25)
    To=models.CharField(max_length=25)
    RiderDate = models.IntegerField(default=10)
    FlexibleDate=models.BooleanField(default=False)
    Medium=models.CharField(max_length=5,choices=MEDIUM)
    TotalAssets=models.IntegerField()

