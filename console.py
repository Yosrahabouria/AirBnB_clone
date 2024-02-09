#!/usr/bin/python3
"""Defines the HBnB console."""

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
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        pass

    def default(self, arg):
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
            cls_name, method = parts[0], parts[1]
            match = re.search(r"\((.*?)\)", method)
            if match:
                command = method[:match.span()[0]].strip(), match.group()[1:-1]
                if command[0] in commands:
                    return commands[command[0]](cls_name + " " + command[1])
        print("*** Unknown syntax: {}".format(arg))

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print("")
        return True

    def do_create(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = self.classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objs:
                print("** no instance found **")
            else:
                print(objs[key])

    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objs:
                print("** no instance found **")
            else:
                del objs[key]
                storage.save()

    def do_all(self, arg):
        args = arg.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            if args:
                print([str(obj) for obj in objs.values() if isinstance(obj, self.classes[args[0]])])
            else:
                print([str(obj) for obj in objs.values()])

    def do_count(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            count = sum(1 for obj in storage.all().values() if isinstance(obj, self.classes[args[0]]))
            print(count)

    def do_update(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
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
    
