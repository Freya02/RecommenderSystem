camera={"camera","camera-quality","camera quality","picture quality","picture-quality"}
battery={"battery life","battery","power","standby"}
performance={"processor","performance","speed","power"}
overall={"overall","all in all","all-in-all"}
display={"display","screen"}
value_for_money={"value for money","price","value"}

def getNoun(word):
    if word in camera:
        return "camera"
    elif word in battery:
        return "battery"
    elif word in performance:
        return "performance"
    elif word in overall:
        return "overall"
    elif word in display:
        return "display"
    elif word in value_for_money:
        return "value_for_money"
    else:
        return "misc"
