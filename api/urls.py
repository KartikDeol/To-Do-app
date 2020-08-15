from django.urls import path
from . import views

# in this we are defining the URL's with respect to /api/views.py
urlpatterns = [

	# name is the name of URL
	#views.'' is the function that we defined in /api/views.py

	#url for api overview
	path('', views.apiOverview, name="api-overview"),

	#url for showing the task list
	path('task-list/', views.taskList, name="task-list"),

	#url for showing the task details
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),

	#url for showing the task create where we can create new task
	path('task-create/', views.taskCreate, name="task-create"),



	#url for updating task
	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),

	#url for deleting the task
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
