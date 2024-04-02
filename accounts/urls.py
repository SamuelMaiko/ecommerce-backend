from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.user_registration, name='register'),
    path('login/',views.LoginWithToken.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('suppliers/',views.SuppliersView.as_view(),name="suppliers"),
    path('suppliers/<int:supplier_id>/',views.SupplierView.as_view(),name="specific-supplier"),
    path('popular-suppliers/',views.PopularSuppliersView.as_view(),name="popular-suppliers"),
    # path('send-reset-email/',views.SendResetEmail.as_view(),name="send-reset-email"),
    # path('password-reset/<str:uid>/<str:token>/',views.PasswordReset,name="password-reset"),
    # path('password-reset-done/',views.PasswordResetDone,name="password-reset-done"),
    # path('password-expired-token/',views.PasswordResetExpired,name="password-expired-token"),
    # path('change-details/', views.ChangeUserDetailsAPIView.as_view(), name='change_user_details_api'),
]

