def can_update(self, user):
    return user.can_update_site(self, allow=['pi'])

@staticmethod
def select_by_user(user):
    if user.is_admin:
        qs = SitePrivilege.objects.all()
    else:
        sp_ids = [sp.id for sp in SitePrivilege.objects.filter(user=user)]
        qs = SitePrivilege.objects.filter(id__in=sp_ids)
    return qs

