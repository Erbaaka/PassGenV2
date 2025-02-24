import random
import string
import curses

def generate_password():
    length = random.randint(8, 16)
    characters = string.ascii_letters + string.digits + "_@"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    
    menu = ["Generate Password", "Change Password", "Exit"]
    current_selection = 0
    password = ""
    
    while True:
        stdscr.clear()
        stdscr.addstr(1, 10, "PassGenV2", curses.A_BOLD)
        
        for idx, item in enumerate(menu):
            if idx == current_selection:
                stdscr.addstr(3 + idx, 5, f"> {item} <", curses.A_REVERSE)
            else:
                stdscr.addstr(3 + idx, 5, item)
        
        if password:
            stdscr.addstr(7, 5, f"Generated Password: {password}")
        
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(menu) - 1:
            current_selection += 1
        elif key in [10, 13]:  # Enter key
            if current_selection == 0:  # Generate Password
                password = generate_password()
            elif current_selection == 1:  # Change Password (User Input)
                stdscr.clear()
                stdscr.addstr(1, 5, "Enter new password hint: ")
                stdscr.refresh()
                
                curses.echo()  # Aktifkan input tampilan
                user_input = stdscr.getstr(2, 5, 20).decode("utf-8")
                curses.noecho()
                
                if user_input.strip():
                    password = generate_password()
                else:
                    password = "Invalid input!"
            elif current_selection == 2:  # Exit
                break
        
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
