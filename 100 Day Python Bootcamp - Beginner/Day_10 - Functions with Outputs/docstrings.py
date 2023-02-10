
# DocStrings

formated_name = "Daniel Booysen"

# Standard python functions with outputs
# e.g:

length = len(formated_name)

def format_name(f_name,l_name):
    """Take first and last name and format it to return the title case vesion of the name."""

    if f_name == "" or l_name == "":
        return "You didnt provide valid inputs."

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name("daNIeL", "booYsen"))
