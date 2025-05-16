#!/usr/bin/python3
"""
Command Interpreter Module for HBNB Project
"""
import cmd
from models.base_model import BaseModel
from models import storage

MODELS = ["BaseModel"]


def validate_args(args_list):
    """
    Validates command arguments to ensure they meet requirements.
    """
    if not args_list:
        print("** class name missing **")
        return False

    class_name = args_list[0]
    if class_name not in MODELS:
        print("** class doesn't exist **")
        return False

    if len(args_list) < 2:
        print("** instance id missing **")
        return False

    return True


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles EOF to exit the program (Ctrl+D)."""
        return True

    def do_create(self, cls_name):
        """Creates an instance of a Model"""
        if not cls_name:
            print("** class name missing **")
            return
        if cls_name not in MODELS:
            print("** class doesn't exist **")
            return

        new_model = BaseModel()
        new_model.save()

    def do_show(self, args):
        """
        Prints the string representation of an instance
        Use: show <class name> <id>
        """
        args_list = str.split(args)

        if not validate_args(args_list):
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance\nUse: destroy <class name> <id>"""
        args_list = str.split(args)
        if not validate_args(args_list):
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
