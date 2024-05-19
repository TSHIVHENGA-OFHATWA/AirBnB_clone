#!/usr/bin/python3
"""Console for AirBnb clone """


import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
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
        """Prints the string representation of an instance"""
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
        """Deletes an instance based on the class name and id"""
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

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        try:
            if not arg:
                print([str(value) for value in storage.all().values()])
            else:
                class_name = arg.split()[0]
                if class_name not in globals():
                    print("** class doesn't exist **")
                    return
                print(
                        [str(value) for key,
                            value in storage.all().items()
                            if key.split('.')[0] == class_name]
                        )
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
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
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attr_value = args[3]
            instance = storage.all()[key]
            setattr(instance, attr_name, attr_value)
            instance.save()
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
