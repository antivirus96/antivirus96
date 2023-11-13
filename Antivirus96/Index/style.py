class TextStyle:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def display_message(message, style=''):
    formatted_message = f"{style}{message}{TextStyle.ENDC}"
    print(formatted_message)

# Example usage:
display_message("This is a header", TextStyle.HEADER)
display_message("This is a success message", TextStyle.OKGREEN)
display_message("This is a warning", TextStyle.WARNING)
display_message("This is a failure message", TextStyle.FAIL)
display_message("This is bold and underlined", f"{TextStyle.BOLD}{TextStyle.UNDERLINE}")
