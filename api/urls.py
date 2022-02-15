from django.urls import include, path
from . import views
'''from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
'''
urlpatterns = [
    path('',views.ApiOverview, name="api-overview"),
    path('task-list/',views.tasklist, name="task-list"),
    path('task-detail/<str:pk>/',views.taskDetail, name="task-detail"),
    path('task-create/',views.taskCreate, name="task-create"),
    path('task-update/<str:pk>/',views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/',views.taskDelete, name="task-delete"),
    

]

