from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Question , Out_questiom
#from projsite.admin_site import custom_admin_site

admin.site.register(Question )
admin.site.register(Out_questiom)

class SendAnswerAdmin(admin.ModelAdmin):
	def get_urls(self):
		urls = super(SendAnswerAdmin, self).get_urls()
		my_urls = [
			path('answer/',self.admin_site.admin_view(self.answer_get)),
			path('answer/create/', self.admin_site.admin_view(self.answer_out)),
		]
		return my_urls + urls
	def answer_get(self,request):
		question_list = Question.objects.order_by('date_time_create')
		return render(request,'admin/answer_admin_change.html')
	
	def answer_out(self,request):
		if request.method == "POST":
			answer_question = Question.objects.order_by('date_time_create')
			text_answer = request.POST.get("text_answer")
			send_mail('Ответ', text_answer, 'projectquessch@gmail.com',
				[answer_question.email], fail_silently=False)
			new_answer = Out_answer(
				email_answer = answer_question.email,
				name_person_answer = answer_question.name_person,
				theme_question_answer = answer_question.theme_question,
				full_text_answer = text_answer,
				full_text_answer_old = answer_question.full_text_answer,
				created_time_quest_old = answer_question.created_time_quest,
			)
			answer_question.delete()
			new_answer.save()



















