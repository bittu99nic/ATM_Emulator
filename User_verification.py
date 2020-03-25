from Card_details import details


def user_input(cno, pin):
    uno = 0
    uno = details(cno, pin)
    if uno == 1:
        return 1
