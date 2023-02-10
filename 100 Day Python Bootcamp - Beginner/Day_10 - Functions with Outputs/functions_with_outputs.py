
# Functions with Outputs

def format_name(F_name, L_name):
    formated_f_name = F_name.title()
    formated_l_name = L_name.title()

    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("daNIel", "booYSEN")
print(formated_string)