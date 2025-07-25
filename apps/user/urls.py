from django.urls import path

from apps.user.views import UserListCreateView, BlockUser, DeblockUser, MakeUserAdmin, MakeUserNotAdmin

urlpatterns = [
    path("", UserListCreateView.as_view(), name="user_list_create"),
    path("/<int:pk>/block", BlockUser.as_view(), name="user_block"),
    path("/<int:pk>/deblock", DeblockUser.as_view(), name="user_deblock"),
    path("/<int:pk>/make_admin", MakeUserAdmin.as_view(), name="user_make_admin"),
    path("/<int:pk>/make_not_admin", MakeUserNotAdmin.as_view(), name="user_make_not_admin"),
]