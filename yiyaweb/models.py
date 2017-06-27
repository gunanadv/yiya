# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.conf import settings
import uuid


# Create your models here.
class Student(models.Model):

	numeric = RegexValidator(r'^[0-9]*$', '请输入正确的电话号码。')

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, null=True, blank=True)
	email = models.CharField(unique=True, null=False, blank=False, max_length=50)
	name = models.CharField(max_length=40)
	address = models.CharField(blank=True, max_length=100)
	phone = models.CharField(blank=True ,max_length=50, validators=[numeric])
	city = models.CharField(blank=True, max_length=30)
	state = models.CharField(blank=True, max_length=10)
	post_code = models.CharField(blank=True, max_length=30, validators=[numeric])
	
	def __unicode__(self):
		return self.name

def passport_path(instance, filename):
	return 'passport_{0}/{1}'.format(instance.id, filename)

def visa_path(instance, filename):
	return 'visa_{0}/{1}'.format(instance.id, filename)

def current_score_path(instance, filename):
	return 'current_score_{0}/{1}'.format(instance.id, filename)

def I20_path(instance, filename):
	return 'I20_{0}/{1}'.format(instance.id, filename)

def previous_score_path(instance, filename):
	return 'previous_score_{0}/{1}'.format(instance.id, filename)

def language_test_path(instance, filename):
	return 'language_test_{0}/{1}'.format(instance.id, filename)

def bank_statement_path(instance, filename):
	return 'bank_statement_{0}/{1}'.format(instance.id, filename)
		
def other_path(instance, filename):
	return 'bank_statement_{0}/{1}'.format(instance.id, filename)	

class Application(models.Model):

	STAGE_CHOICE = (
		('W', '等待付款'),
		('Y', '已付款'),
		('T', '等待填表'),
		('P', '准备中'),
		('I', '正在申请'),
		('F', '已完成'),
	)

	TYPE_CHOICE = (
		('G', '普通申请'),
		('U', '大学申请'),
		('C', '社区学院申请'),
		('H', '高中申请'),
	)

	VISA_CHOICE = (
		('N', '无'),
		('F1I', 'F1就读'),
		('F1O', 'F1开除'),
		('B', 'B1/B2'),
		('O', '其他'),
	)

	GENDER_CHOICE = (
		('M', '男'),
		('F', '女'),
	)

	QUATER_CHOICE = (
		('Sprint', '春季学期'),
		('Summer', '夏季学期'),
		('Autumn', '秋季学期'),
		('Winter', '冬季学期'),
	)

	TEST_CHOICE = (
		('Y', '雅思'),
		('T', '托福'),
		('C', 'College ENG101'),
		('N', '无'),
	)

	numeric = RegexValidator(r'^[0-9]*$', '请输入正确的电话号码。')

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
	application_name = models.CharField(max_length=50)
	application_type = models.CharField(blank=False, max_length=1, choices=TYPE_CHOICE, default = 'G')
	stage = models.CharField(max_length=1, choices=STAGE_CHOICE, default = 'W')
	fee = models.FloatField(null=True, blank= True)
	
	first_name = models.CharField(null=True, blank = True, max_length=20)
	last_name = models.CharField(null=True, blank=True, max_length=20)
	birth_city = models.CharField(blank=True, max_length=50)
	birth_province = models.CharField(blank=True, max_length=50)
	birth_country = models.CharField(blank=True, max_length=50)
	date_of_birth = models.DateField(null=True, blank=True)
	gender = models.CharField(blank=True, max_length=1, choices=GENDER_CHOICE)
	passport_number = models.CharField(blank=True, max_length=50)
	application_email = models.CharField(null=True, blank=True, max_length=50)

	father_name = models.CharField(blank=True, max_length=50)
	mother_name = models.CharField(blank=True, max_length=50)
	US_tel = models.CharField(blank=True ,max_length=50, validators=[numeric])
	CHINA_tel = models.CharField(blank=True, max_length=50, validators=[numeric])
	US_address = models.CharField(blank=True, max_length=100)
	CHINA_address = models.CharField(blank=True, max_length=100)

	
	high_school = models.CharField(blank=True, max_length=100)
	high_school_start = models.DateField(null=True, blank=True)
	high_school_end = models.DateField(null=True, blank=True)
	current_school = models.CharField(blank=True, max_length=100)
	current_school_start = models.DateField(null=True, blank=True)
	current_school_end = models.DateField(null=True, blank=True)
	current_visa_status =  models.CharField(max_length=5, choices=VISA_CHOICE, default = 'N')
	language_test = models.CharField(max_length=1, choices=TEST_CHOICE, default = 'N')
	language_score = models.FloatField(null=True, blank= True)

	applying_college = models.CharField(blank=True, max_length=50)
	applying_quater = models.CharField(max_length=8, choices=QUATER_CHOICE, default = 'Spring')
	applying_major = models.CharField(blank=True, max_length=50)
	

	passport_file = models.FileField(blank=True, null= True, upload_to = passport_path)
	visa_file = models.FileField(blank=True, null= True, upload_to = visa_path)
	current_score_file = models.FileField(blank=True, null= True, upload_to = current_score_path)
	I20_file = models.FileField(blank=True, null= True, upload_to = I20_path)
	previous_score_file = models.FileField(blank=True, null= True, upload_to = previous_score_path)
	language_test_file = models.FileField(blank=True, null= True, upload_to = language_test_path)
	bank_statement_file = models.FileField(blank=True, null= True, upload_to = bank_statement_path)
	other_file =  models.FileField(blank=True, null= True, upload_to = other_path)
	
	
	
	def __unicode__(self):              # __unicode__ on Python 2
		return self.application_name



class Consultation(models.Model):

	numeric = RegexValidator(r'^[0-9]*$', '请输入正确的电话号码。')

	STATUS_CHOICE = (
		('R', 'Received'),
		('P', 'Responsed'),
		('C', 'Complete'),
    )

	name = models.CharField(blank=False, max_length=50)
	email = models.CharField(blank=False, max_length=50)
	service = models.CharField(blank=False, max_length=50)
	phone = models.CharField(blank=True, max_length=50, validators=[numeric])
	description = models.CharField(blank=True, max_length=300)
	status = models.CharField(max_length=1, choices=STATUS_CHOICE, default = 'R')


	def __unicode__(self):              # __unicode__ on Python 2
		return self.name


	