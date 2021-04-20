def is_staff(user):
    return user.groups.filter(name='Staff').exists()


def is_student(user):
    return user.groups.filter(name='Student').exists()
