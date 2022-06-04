# #Functions with outputs
#
# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
#
# format_name("walter", "ciriello")
#
#
# def format_name(f_name, l_name):
#     formated_f_name = (f_name.title())
#     formated_l_name = (l_name.title())
#
#     print(f"{formated_f_name} {formated_l_name}")
#
# format_name("WAltEr", "cIRieLlo")

def format_name(f_name, l_name):
    """Take a first and last name and format it to return title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didin't provide valid inputs."
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

format_name()
