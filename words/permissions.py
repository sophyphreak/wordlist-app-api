from rest_framework import permissions


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read and write permissions are only allowed 
        #  to the author of a word
        return obj.author == request.user