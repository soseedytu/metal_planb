from common_lib.models import MUser


class UserService(object):

    def validate_user_name(self, user_name, user_id):
        matching_courses = MUser.objects.filter(Username=user_name)

        matching_courses = matching_courses.exclude(pk=user_id)

        if matching_courses.exists():
            msg = u"User name: %s has already exist." % user_name
        else:
            msg = ""

        return msg