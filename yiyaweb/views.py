# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django import forms

from django.core.mail import send_mail

import json

# Create your views herei.


from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
from django.core.validators import validate_email
from captcha.fields import CaptchaField

import os
from django.conf import settings
import shutil


class register_form(forms.Form):

	numeric = RegexValidator(r'^[0-9]*$', '请输入正确的电话号码。')
	oninvalid_message = "setCustomValidity('请输入正确的信息。')"
	oninput_message = "setCustomValidity('')" 

	r_captcha = CaptchaField()
	r_email = forms.EmailField(max_length=100, error_messages={'invalid': '请输入正确的邮箱。'}, widget=forms.EmailInput(attrs={'placeholder': '邮箱', 'class': 'form-control' , 'oninvalid' : oninvalid_message, 'oninput': oninput_message}))
	r_password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder': '密码', 'class': 'form-control', 'oninvalid' : oninvalid_message, 'oninput': oninput_message}))
	r_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': '姓名', 'class': 'form-control', 'oninvalid' : oninvalid_message, 'oninput': oninput_message}))
	r_phone = forms.CharField(required=False, max_length=30,validators=[numeric], widget=forms.TextInput(attrs={'placeholder': '电话(可选)', 'class': 'form-control number' , 'maxlength':'15'}))


class selfi_form(ModelForm):

	class Meta:
		numeric = RegexValidator(r'^[0-9]*$', '请输入正确的电话号码。')
		oninvalid_message = "setCustomValidity('请输入正确的信息。')"
		oninput_message = "setCustomValidity('')" 

		model = Student
		fields = ['email', 'name', 'phone', 'address', 'city', 'post_code', 'state']
		widgets = {
			'email': forms.EmailInput(attrs={'placeholder': '邮箱', 'class': 'form-control', 'readonly':'true'}),
			'name': forms.TextInput(attrs={'placeholder': '姓名', 'class': 'form-control', 'oninvalid' : oninvalid_message, 'oninput': oninput_message}),
			'phone': forms.TextInput(attrs={'placeholder': '电话', 'class': 'form-control number'}),
			'address': forms.TextInput(attrs={'placeholder': '住址', 'class': 'form-control'}),
			'city': forms.TextInput(attrs={'placeholder': '城市', 'class': 'form-control'}),
			'state': forms.TextInput(attrs={'placeholder': '州／省', 'class': 'form-control'}),
			'post_code': forms.TextInput(attrs={'placeholder': '邮编', 'class': 'form-control number'}),
		 }


class search_form(forms.Form):
	last_name = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	name = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(required=False, max_length=100, error_messages={'invalid': '请输入正确的邮箱。'}, widget=forms.EmailInput(attrs={'class': 'form-control' }))
	


class application_form(ModelForm):

	class Meta:

		numeric = RegexValidator(r'^[0-9]*$', '请输入正确的电话号码。')
		oninvalid_message = "setCustomValidity('请输入正确的信息。')"
		oninput_message = "setCustomValidity('')" 


		model = Application
		exclude = ['student', 'stage', 'application_name', 'application_type', 'fee']
		widgets = {
			'application_email': forms.EmailInput(attrs={'placeholder': '邮箱', 'class': 'form-control' , 'oninvalid' : oninvalid_message, 'oninput': oninput_message}),
			'US_tel': forms.TextInput(attrs={ 'class': 'form-control number' , 'maxlength':'15'}),
			'CHINA_tel': forms.TextInput(attrs={ 'class': 'form-control number' , 'maxlength':'15'}),
			'date_of_birth': forms.DateInput(attrs={ 'class': 'form-control date_picker', 'readonly' : 'true'}),
			'gender': forms.RadioSelect(),
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
			'father_name': forms.TextInput(attrs={'class': 'form-control'}),
			'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
			'birth_country': forms.TextInput(attrs={'class': 'form-control'}),
			'birth_province': forms.TextInput(attrs={'class': 'form-control'}),
			'birth_city': forms.TextInput(attrs={'class': 'form-control'}),
			'US_address': forms.TextInput(attrs={'class': 'form-control'}),
			'CHINA_address': forms.TextInput(attrs={'class': 'form-control'}),
			'high_school': forms.TextInput(attrs={'class': 'form-control'}),
			'high_school_start': forms.DateInput(attrs={ 'class': 'form-control date_picker' , 'readonly' : 'true'}),
			'high_school_end': forms.DateInput(attrs={ 'class': 'form-control date_picker', 'readonly' : 'true'}),
			'current_school': forms.TextInput(attrs={'class': 'form-control'}),
			'current_school_start': forms.DateInput(attrs={ 'class': 'form-control date_picker' , 'readonly' : 'true'}),
			'current_school_end': forms.DateInput(attrs={ 'class': 'form-control date_picker', 'readonly' : 'true'}),
			'language_score': forms.NumberInput(attrs={ 'class': 'form-control'}),
			'language_test': forms.Select(attrs={ 'class': 'form-control none-radius'}),
			'current_visa_status': forms.Select(attrs={ 'class': 'form-control none-radius'}),
			'passport_number': forms.TextInput(attrs={'class': 'form-control'}),
			'applying_college': forms.TextInput(attrs={'class': 'form-control'}),
			'applying_major': forms.TextInput(attrs={'class': 'form-control'}),
			'applying_quater': forms.Select(attrs={ 'class': 'form-control none-radius'}),
			'visa_file': forms.FileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'current_score_file': forms.FileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'I20_file': forms.FileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'previous_score_file': forms.FileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'language_test_file': forms.FileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'bank_statement_file': forms.FileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'other_file': forms.FileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'passport_file': forms.FileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),

		}

class  admin_application_form(ModelForm):
	class Meta:

		numeric = RegexValidator(r'^[0-9]*$', '请输入正确的电话号码。')
		oninvalid_message = "setCustomValidity('请输入正确的信息。')"
		oninput_message = "setCustomValidity('')" 

		model = Application
		exclude = ['student']
		widgets = {
			'application_email': forms.EmailInput(attrs={'placeholder': '邮箱', 'class': 'form-control' , 'oninvalid' : oninvalid_message, 'oninput': oninput_message}),'application_name': forms.TextInput(attrs={'class': 'form-control'}),
			'application_type': forms.Select(attrs={ 'class': 'form-control none-radius'}),
			'stage': forms.Select(attrs={ 'class': 'form-control none-radius'}),
			'fee': forms.NumberInput(attrs={ 'class': 'form-control'}),
			'US_tel': forms.TextInput(attrs={ 'class': 'form-control number' , 'maxlength':'15'}),
			'CHINA_tel': forms.TextInput(attrs={ 'class': 'form-control number' , 'maxlength':'15'}),
			'date_of_birth': forms.DateInput(attrs={ 'class': 'form-control date_picker', 'readonly' : 'true'}),
			'gender': forms.RadioSelect(),
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
			'father_name': forms.TextInput(attrs={'class': 'form-control'}),
			'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
			'birth_country': forms.TextInput(attrs={'class': 'form-control'}),
			'birth_province': forms.TextInput(attrs={'class': 'form-control'}),
			'birth_city': forms.TextInput(attrs={'class': 'form-control'}),
			'US_address': forms.TextInput(attrs={'class': 'form-control'}),
			'CHINA_address': forms.TextInput(attrs={'class': 'form-control'}),
			'current_school': forms.TextInput(attrs={'class': 'form-control'}),
			'current_school_start': forms.DateInput(attrs={ 'class': 'form-control date_picker' , 'readonly' : 'true'}),
			'current_school_end': forms.DateInput(attrs={ 'class': 'form-control date_picker', 'readonly' : 'true'}),
			'high_school': forms.TextInput(attrs={'class': 'form-control'}),
			'high_school_start': forms.DateInput(attrs={ 'class': 'form-control date_picker' , 'readonly' : 'true'}),
			'high_school_end': forms.DateInput(attrs={ 'class': 'form-control date_picker', 'readonly' : 'true'}),
			'language_score': forms.NumberInput(attrs={ 'class': 'form-control'}),
			'language_test': forms.Select(attrs={ 'class': 'form-control none-radius'}),
			'current_visa_status': forms.Select(attrs={ 'class': 'form-control none-radius'}),
			'passport_number': forms.TextInput(attrs={'class': 'form-control'}),
			'applying_college': forms.TextInput(attrs={'class': 'form-control'}),
			'applying_major': forms.TextInput(attrs={'class': 'form-control'}),
			'applying_quater': forms.Select(attrs={ 'class': 'form-control none-radius'}),

			'visa_file': forms.ClearableFileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'current_score_file': forms.ClearableFileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'I20_file': forms.ClearableFileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'previous_score_file': forms.ClearableFileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'language_test_file': forms.ClearableFileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'bank_statement_file': forms.ClearableFileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'other_file': forms.ClearableFileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),
			'passport_file': forms.ClearableFileInput(attrs = { 'accept' : '.pdf,.doc,.docx,image/*'}),

		}

class  admin_application_create_form(ModelForm):
	class Meta:

		numeric = RegexValidator(r'^[0-9]*$', '请输入正确的电话号码。')
		oninvalid_message = "setCustomValidity('请输入正确的信息。')"
		oninput_message = "setCustomValidity('')" 

		model = Application
		fields = ['application_name', 'application_type', 'stage', 'fee', 'application_email']
		widgets = {
			'application_email': forms.TextInput(attrs={'placeholder': '邮箱', 'class': 'form-control' , 'oninvalid' : oninvalid_message, 'oninput': oninput_message}),'application_name': forms.TextInput(attrs={'class': 'form-control'}),
			'application_type': forms.Select(attrs={ 'class': 'form-control none-radius'}),
			'stage': forms.Select(attrs={ 'class': 'form-control none-radius'}),
			'fee': forms.NumberInput(attrs={ 'class': 'form-control'}),
		}



class login_form(forms.Form):
	oninvalid_message = "setCustomValidity('请输入正确的信息。')"
	oninput_message = "setCustomValidity('')" 
	username = forms.EmailField(max_length=100, error_messages={'invalid': '请输入正确的邮箱。'}, widget=forms.EmailInput(attrs={'placeholder': '邮箱', 'class': 'form-control' , 'oninvalid' : oninvalid_message, 'oninput': oninput_message}))
	password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder': '密码', 'class': 'form-control', 'oninvalid' : oninvalid_message, 'oninput': oninput_message}))


def index(request):

	context = {'student': ''}
	if request.user.is_authenticated():
		student = Student.objects.filter(user = request.user)
		if student:
			context = {
				'student': student[0],
			}
		
	return render(request, 'index.html', context)

def application_view(request, id):


	applications = Application.objects.filter(id = id)
	if not applications:
		return HttpResponseRedirect('/')
	else:
		application = applications[0]

	if not application:
		return HttpResponseRedirect('/')


	if not request.method == 'POST':
		aform = application_form(instance = application)
		context = {
			'aform': aform,
			'application': application,
			'success': False,
		}

	if request.method == 'POST':
		aform = application_form(request.POST, request.FILES, instance = application)
		if aform.is_valid():
			

			filelist = {'passport', 'visa', 'current_score', 'I20', 'previous_score', 'language_test', 'bank_statement', 'other' }
			for dirname in filelist:
				if request.FILES and request.FILES.get(dirname + '_file', False):
					ext = os.path.splitext(request.FILES[dirname + '_file'].name)[1] 
					print ext
					valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png']
					if not ext.lower() in valid_extensions:
						raise ValidationError(u'Unsupported file extension.')
					file_path = os.path.join(settings.MEDIA_ROOT, (dirname + '_{0}').format(application.id))
					if os.path.isdir(file_path):
						shutil.rmtree(file_path)
			aform.save()

			gemail = aform.cleaned_data['application_email']
			if application.student is None:
				if gemail:
					students = Student.objects.filter(email = gemail)
					if students:
						student=students[0]
						application.student = student
						application.save()

			success = True
		context = {
			'aform': aform,
			'application': application,
			'success': success,
		}

	if application.application_type == 'U':
		return render(request, 'application_u.html', context)
	if application.application_type == 'C':
		return render(request, 'application_c.html', context)
	if application.application_type == 'H':
		return render(request, 'application_h.html', context)
	return render(request, 'application.html', context)



def selfi_view(request):

	if request.user.is_authenticated():
		students = Student.objects.filter(user = request.user)
		if not students:
			return HttpResponseRedirect('/')

		student = Student.objects.filter(user = request.user)[0]
		user = request.user;
	else:
		return HttpResponseRedirect('/')
	s_form = selfi_form(instance = student)

	success = False

	if request.method == 'POST':
		eStudent = selfi_form(request.POST, instance = student)
		if eStudent.is_valid():
			s_form = eStudent
			eStudent.save()
			success = True

	applications = Application.objects.filter(student = student)

	context = {
		's_form': s_form,
		'applications': applications,
		'student': student,
		'success': success,
	}
	return render(request, 'selfi.html', context)
	


def register_view(request):
	if request.method == 'POST':
		r_form = register_form(request.POST)
		if r_form.is_valid():
			new_user = User()
			if User.objects.filter(username = r_form.cleaned_data['r_email']).exists():
				r_form.add_error('r_email', '该邮箱已经注册过了。')
			else:
				new_student = Student()
				new_user.username = r_form.cleaned_data['r_email']
				new_user.set_password(r_form.cleaned_data['r_password'])
				new_user.first_name = r_form.cleaned_data['r_name']
				new_user.save()
				new_student.user = new_user
				new_student.name = r_form.cleaned_data['r_name']
				new_student.email = r_form.cleaned_data['r_email']
				if r_form.cleaned_data['r_phone']:
					new_student.phone = r_form.cleaned_data['r_phone']
				new_student.save()
				applications = Application.objects.filter(application_email = new_user.username)
				if applications:
					for application in applications:
						if application.student is None:
							application.student = new_student
							application.save()
				send_mail(
					'欢迎使用络雅留学咨询',
					'美国络雅教育总部位于华盛顿州西雅图，主营业务集美国初/高中 留学申请 及转学、紧急学术应对、美国本科/研究生申请和转学、学术辅导、美国寄宿家庭服务。\n联系邮箱：service@loyaeducation.com',
					'system@loyaeducation.com',
					[new_student.email],
					fail_silently=False,
				)
							
				login(request, new_user)
				return HttpResponseRedirect('/')
	else:
		r_form = register_form()

	context = {
		'r_form': r_form,
	}
	return render(request, 'register.html', context)



def login_view(request):
	if request.method == 'POST':
		l_form = login_form(request.POST)
		if l_form.is_valid():
			username = l_form.cleaned_data['username']
			password = l_form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					l_form.add_error('username', '该账号已被封禁，请联系管理员。')
			else:
				l_form.add_error('username', '邮箱或密码不正确。')
	else:
		l_form = login_form()

	context = {
		'l_form': l_form,
	}

	return render(request, 'login.html', context)

@login_required
def logout_view(request):
	 logout(request)
	 return HttpResponseRedirect('/')


def consultation_submit(request):
	if request.method == 'POST':
		email = request.POST['email']
		try:
			validate_email(email)
			valid_email = True
		except ValidationError:
			valid_email = False


		if valid_email:
			new_consultation = Consultation()
			new_consultation.name = request.POST['name'];
			new_consultation.email = request.POST['email'];
			new_consultation.service = request.POST['service'];
			new_consultation.phone = request.POST['phone'];
			new_consultation.description = request.POST['description'];
			new_consultation.save()
			send_mail(
			'新的咨询【' + new_consultation.email + '】',
				'姓名：' + new_consultation.name + 
				'\n邮箱：' + new_consultation.email + 
				'\n电话：' + new_consultation.phone +
				'\n服务：' + new_consultation.service +
				'\n描述：' + new_consultation.description, 
				'system@loyaeducation.com',
				['michelle@loyaeducation.com',],
				fail_silently=False,
			)
			return HttpResponse(json.dumps({'message': 'success'}), content_type='application/json')
	return HttpResponse(json.dumps({'message': 'fail'}), content_type='application/json')

def forget_password_submit(request):
	if request.method == 'POST':
		email = request.POST['email']
		try:
			validate_email(email)
			valid_email = True
		except ValidationError:
			valid_email = False
		if valid_email:
			users = User.objects.filter(username = email)
			if users:
				user = users[0]
			new_password = get_random_string(length=10)
			user.set_password(new_password)
			user.save()

			send_mail(
				'络雅咨询【密码找回】',
				'\n邮箱：' + email + 
				'\n新密码：' + new_password +
				'\n请登陆后尽快重设您的密码！！' ,
				'system@loyaeducation.com',
				[email,],
				fail_silently=False,
			)
			return HttpResponse(json.dumps({'message': 'success'}), content_type='application/json')
	return HttpResponse(json.dumps({'message': 'fail'}), content_type='application/json')

@login_required
def new_password_submit(request):
	if request.method == 'POST':
		old_password = request.POST['old_password']
		new_password = request.POST['new_password']
		user = request.user
		if user.check_password(old_password):
			user.set_password(new_password)
			user.save();
			return HttpResponse(json.dumps({'message': 'success'}), content_type='application/json')
	return HttpResponse(json.dumps({'message': 'fail'}), content_type='application/json')	


def admin_console(request):
	if not request.user.is_staff:
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		aform = search_form(request.POST)
		context = {'aform' : aform,
				'addform': admin_application_create_form()}
		applications = None
		students = None
		if aform.is_valid():
			if aform.cleaned_data['first_name'] and aform.cleaned_data['last_name']:
				applications = Application.objects.filter(first_name = aform.cleaned_data['first_name'], last_name = aform.cleaned_data['last_name'])
			elif aform.cleaned_data['first_name']:
				applications = Application.objects.filter(first_name = aform.cleaned_data['first_name'])
			elif aform.cleaned_data['last_name']:
				applications = Application.objects.filter(last_name = aform.cleaned_data['last_name'])

			if applications:
				context['applications'] = applications

			if aform.cleaned_data['email']:
				students = Student.objects.filter(email = aform.cleaned_data['email'])
			elif aform.cleaned_data['name']:
				students = Student.objects.filter(name = aform.cleaned_data['name'])

			if students:
				context['students']= students

			if not applications and not students:
				context['message'] = '没有找到符合条件的申请。'

				return render(request, 'admin_console.html', context)

			return render(request, 'admin_console.html', context)

	if not request.method == 'POST':
		aform = search_form()
		context = {'aform' : aform,
				'addform': admin_application_create_form()}
		return render(request, 'admin_console.html', context)

def application_create_submit(request):
	if not request.user.is_staff:
		return HttpResponseRedirect('/')
	if request.method == 'POST':

		student_id = request.POST.get('student_id', None)
		application_email= request.POST.get('application_email', None)
		new_application = admin_application_create_form(request.POST)
		if new_application.is_valid():
			new_application_instance = Application()
			new_application_instance.application_name = new_application.cleaned_data['application_name']
			new_application_instance.application_type = new_application.cleaned_data['application_type']
			new_application_instance.stage = new_application.cleaned_data['stage']
			new_application_instance.fee = new_application.cleaned_data['fee']
			new_application_instance.application_email = new_application.cleaned_data['application_email']

			if student_id is not None:
				students = Student.objects.filter(id = student_id)
				if students:
					student = students[0]
					new_application_instance.student = student
			elif application_email is not None:
				students = Student.objects.filter(email = application_email)
				if students:
					student=students[0]
					new_application_instance.student = student
			
			new_application_instance.save()
		return HttpResponse(json.dumps({'message': 'success', 'url': 'http://www.loyaeducation.com/admin_application/'+ str(new_application_instance
			.id)}), content_type='application/json')
	return HttpResponse(json.dumps({'message': 'fail', 'errors': new_application.errors}), content_type='application/json')

def admin_application_view(request, id):

	if not request.user.is_staff:
		return HttpResponseRedirect('/application/'+id)

	applications = Application.objects.filter(id = id)
	if not applications:
		return HttpResponseRedirect('/admin_console')
	else:
		application = applications[0]

	if not application:
		return HttpResponseRedirect('/admin_console')


	if not request.method == 'POST':
		aform = admin_application_form(instance = application)
		context = {
			'aform': aform,
			'application': application,
			'success': False,
		}

	if request.method == 'POST':
		aform = admin_application_form(request.POST, request.FILES, instance = application)
		if aform.is_valid():
			filelist = {'passport', 'visa', 'current_score', 'I20', 'previous_score', 'language_test', 'bank_statement', 'other' }
			for dirname in filelist:
				if request.FILES and request.FILES.get(dirname + '_file', False):
					ext = os.path.splitext(request.FILES[dirname + '_file'].name)[1] 
					print ext
					valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png']
					if not ext.lower() in valid_extensions:
						raise ValidationError(u'Unsupported file extension.')
					file_path = os.path.join(settings.MEDIA_ROOT, (dirname + '_{0}').format(application.id))
					if os.path.isdir(file_path):
						shutil.rmtree(file_path)
			aform.save()
			success = True
		context = {
			'aform': aform,
			'application': application,
			'success': success,
		}

	return render(request, 'admin_application.html', context)

def admin_student_view(request,  id):

	if not request.user.is_staff:
		return HttpResponseRedirect('/')
	students = Student.objects.filter(id = id)

	if not students:
		return HttpResponseRedirect('/admin_console')

	student = students[0]

	if not student:
		return HttpResponseRedirect('/admin_console')

	s_form = selfi_form(instance = student)
	success = False

	if request.method == 'POST':
		eStudent = selfi_form(request.POST, instance = student)
		if eStudent.is_valid():
			s_form = eStudent
			eStudent.save()
			success = True

	applications = Application.objects.filter(student = student)

	context = {
		's_form': s_form,
		'applications': applications,
		'student': student,
		'success': success,
		'addform': admin_application_create_form(),
	}
	return render(request, 'admin_student.html', context)






