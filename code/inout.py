import readline

def coloured(text, colour, bold=False):
    # Blue is main UI
    # Yellow is for warnings
    # Green/red for correct/incorrect answers
    # Cyan is for quizes
    # Magenta is word storage related
    reset = '\u001b[0m'
    if not bold: # Not bold will be info
        if colour == 'black':
            return '\u001b[30m' + text + reset
        elif colour == 'red':
            return '\u001b[31m' + text + reset
        elif colour == 'green':
            return '\u001b[32m' + text + reset
        elif colour == 'yellow':
            return '\u001b[33m' + text + reset
        elif colour == 'blue':
            return '\u001b[34m' + text + reset
        elif colour == 'magenta':
            return '\u001b[35m' + text + reset
        elif colour == 'cyan':
            return '\u001b[36m' + text + reset
        elif colour == 'white':
            return '\u001b[37m' + text + reset
    else: # Bold will be questions/require input
        if colour == 'black':
            return '\u001b[30;1m' + text + reset
        elif colour == 'red':
            return '\u001b[31;1m' + text + reset
        elif colour == 'green':
            return '\u001b[32;1m' + text + reset
        elif colour == 'yellow':
            return '\u001b[33;1m' + text + reset
        elif colour == 'blue':
            return '\u001b[34;1m' + text + reset
        elif colour == 'magenta':
            return '\u001b[35;1m' + text + reset
        elif colour == 'cyan':
            return '\u001b[36;1m' + text + reset
        elif colour == 'white':
            return '\u001b[37;1m' + text + reset

def remove_history_items(num):
    """
    Call after input to be removed.
    """
    for i in range(num):
        readline.remove_history_item(readline.get_current_history_length() - 1)

#NOTE add question function here
