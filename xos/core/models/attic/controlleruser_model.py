@staticmethod
def select_by_user(user):
    if user.is_admin:
        qs = ControllerUser.objects.all()
    else:
        users = User.select_by_user(user)
        qs = ControllerUser.objects.filter(user__in=users)
    return qs

def can_update(self, user):
    return user.can_update_root()    

