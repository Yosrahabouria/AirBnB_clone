#!/usr/bin/python3
"""Definition of the HBnB console."""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    model_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """empty inputline method"""
        pass

    def default(self, arg):
        """Handling default command method"""
        commands = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match:
            parts = arg.split(".")
            class_name, method = parts[0], parts[1]
            match = re.search(r"\((.*?)\)", method)
            if match:
                command = method[:match.span()[0]].strip(), match.group()[1:-1]
                if command[0] in commands:
                    return commands[command[0]](class_name + " " + command[1])
        print("*** Unknown syntax: {}".format(arg))

    def do_quit(self, arg):
        """Exit method"""
        return True

    def do_EOF(self, arg):
        """Handle End-of-File method"""
        print("")
        return True

    def do_create(self, arg):
        """Creation of a new instance method"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.model_classes:
            print("** class doesn't exist **")
        else:
            instance = self.model_classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Show the string method"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.model_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, arg):
        """Delete an instance method"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.model_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_all(self, arg):
        """Print string method"""
        args = arg.split()
        if args and args[0] not in self.model_classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            if args:
                print([str(obj) for obj in objects.values() if isinstance(obj, self.model_classes[args[0]])])
            else:
                print([str(obj) for obj in objects.values()])

    def do_count(self, arg):
        """Count method"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.model_classes:
            print("** class doesn't exist **")
        else:
            count = sum(1 for obj in storage.all().values() if isinstance(obj, self.model_classes[args[0]]))
            print(count)

    def do_update(self, arg):
        """Update method"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.model_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            obj = storage.all()["{}.{}".format(args[0], args[1])]
            setattr(obj, args[2], args[3])
            obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
