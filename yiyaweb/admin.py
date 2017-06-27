# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
# Register your models here.

class ApplicationInline(admin.TabularInline):
	model = Application
	show_change_link = True

class StudentAdmin(admin.ModelAdmin):
	search_fields = ('current_school', )

	def name(self, obj):
		return obj

	list_display = ('name',)
	inlines = [
		ApplicationInline,
	]


class ConsultationAdmin(admin.ModelAdmin):
	search_fields = ('name', )

	list_display = ('name', 'email', 'status', )


admin.site.register(Student, StudentAdmin)

admin.site.register(Application)

admin.site.register(Consultation, ConsultationAdmin)