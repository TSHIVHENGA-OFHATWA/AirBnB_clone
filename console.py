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

    def do_create(self, arg):
        """Create a new instance of BaseModel.

        Args:
            arg (str): The name of the class to create an instance of.

        Raises:
            NameError: If the class name does not exist.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = arg.split()[0]
            instance = eval(class_name)()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance.

        Args:
            arg (str): The class name and id of the instance.

        Raises:
            NameError: If the class name does not exist.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[key])
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.

        Args:
            arg (str): The class name and id of the instance.

        Raises:
            NameError: If the class name does not exist.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[key]
            storage.save()
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
