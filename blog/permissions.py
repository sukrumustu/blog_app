from rest_framework  import permissions


# class IsOwner(permissions.BasePermission):
#     message = "You must be the owner of this post"

#     def has_object_permission(self, request, obj):
#         return obj.user == request.user
    

# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.user == request.user