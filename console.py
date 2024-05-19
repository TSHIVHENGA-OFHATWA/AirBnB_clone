#!/usr/bin/python3
"""Console for AirBnb clone """

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program.

        Args:
            arg: The argument passed to the command (not used).

        Returns:
            bool: True to indicate that the command should exit.
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program.

        Args:
            arg: The argument passed to the command (not used).

        Returns:
            bool: True to indicate that the command should exit.
        """
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line.

        This method is called when an empty line is entered in
        response to the prompt.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
