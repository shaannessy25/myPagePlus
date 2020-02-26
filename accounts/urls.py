from django.urls import path, include


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='templates-signup-page'),
    path('accounts/', include('django.contrib.auth.urls')),
]
