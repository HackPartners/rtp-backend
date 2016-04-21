from peewee import *
from playhouse.postgres_ext import *

from datetime import datetime
import os

from models.database import db


STATION_MAX_LENGTH = 20


class RtpModel(Model):
    """A base model that will use our Postgres database"""
    class Meta:
        database = db

class PaymentDetails(RtpModel):
	paymentType 			= CharField()
	account_number 			= CharField()
	sort_code 				= CharField()

class ContactDetails(RtpModel):
	title 				= CharField()
	first_name 			= CharField()
	last_name 			= CharField()
	email 				= CharField()
	address				= CharField()
	post_code 			= CharField()

class Journey(RtpModel):
	from_station 			= CharField()
	to_station				= CharField()
	ticket_class			= CharField()
	ticket_type				= CharField()
	image_64				= TextField()
	from_date				= DateField()
	to_date					= DateField()
	cost					= DecimalField()
	journey_date 			= DateTimeField()
	created		 			= DateTimeField(default=datetime.now)

class DelayClaim(RtpModel):
	journey_identifier		= CharField()
	delay_length			= IntegerField()
	service_id				= CharField()
	total_refund			= DecimalField()
	status					= CharField()
	created		 			= DateTimeField(default=datetime.now)

class ClaimValidation(RtpModel):
	journey 				= ForeignKeyField(Journey, unique=True)
	delay_claim 			= ForeignKeyField(DelayClaim, unique=True)
	contact_details 		= ForeignKeyField(ContactDetails, unique=True)
	payment_details			= ForeignKeyField(PaymentDetails, unique=True)


