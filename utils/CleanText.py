def clean_text(text):
    text = text.replace("+" , "")
    text = text.replace("*", "")
    text = text.replace("--", "")
    text = text.replace("[1]", "")
    text = text.replace("[2]", "")
    text = text.replace("[3]", "")
    text = text.replace("[4]", "")
    text = text.replace("[5]", "")
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("'", "")

    return text