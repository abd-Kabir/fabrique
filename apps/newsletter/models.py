from django.db import models

from config.models import BaseModel


class Newsletter(BaseModel):
    send_out_start = models.DateTimeField()
    send_out_end = models.DateTimeField()
    message = models.TextField()
    tag = models.CharField(max_length=100, blank=True, verbose_name="Tags")
    mobile_operator_code = models.CharField(max_length=3, blank=True, verbose_name="MobileOperatorCode")

    class Meta:
        db_table = 'Newsletter'


class Client(BaseModel):
    phone_number = models.CharField(max_length=17, blank=True, verbose_name='PhoneNumber')
    mobile_operator_code = models.CharField(max_length=3, blank=True, verbose_name='MobileOperatorCode')
    tag = models.CharField(max_length=200, blank=True, null=True, verbose_name='')
    timezone = models.CharField(max_length=30, blank=True, null=True, verbose_name='')

    class Meta:
        db_table = 'Client'


class Message(BaseModel):
    dispatch_time = models.DateTimeField(auto_now_add=True)
    dispatch_status = models.BooleanField(default=False)  # True = "Sent" | False = "Not Sent"

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        db_table = 'Message'
