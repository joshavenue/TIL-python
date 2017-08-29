def just_right(str):
    num =len(str)
    if  num < 5:
        return("Your string is too short")
    elif num > 5:
        return("Your string is too long")
    else:
        return True
