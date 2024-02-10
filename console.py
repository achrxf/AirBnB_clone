#!/usr/bin/python3
"""The console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def func(arg):
    curly = re.search(r"\{(.*?)\}", arg)
    brak = re.search(r"\[(.*?)\]", arg)
    if curly is None:
        if brak is None:
            return [i.strip(",") for i in split(arg)]
        else:
            ses = split(arg[:brak.span()[0]])
            ese = [i.strip(",") for i in ses]
            ese.append(brak.group())
            return ese
    else:
        ses = split(arg[:curly.span()[0]])
        ese = [i.strip(",") for i in ses]
        ese.append(curly.group())
        return ese


class HBNBCommand(cmd.Cmd):
    """The HolbertonBnB command interpreter."""
    prompt = "(hbnb) "
    clss = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Emptyline."""
        pass

    def default(self, arg):
        """Default behavior."""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_l = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_l[1])
            if match is not None:
                cmmd = [arg_l[1][:match.span()[0]], match.group()[1:-1]]
                if cmmd[0] in arg_dict.keys():
                    call = "{} {}".format(arg_l[0], cmmd[1])
                    return arg_dict[cmmd[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """To exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance."""
        arg_l = func(arg)
        if len(arg_l) == 0:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
        else:
            print(eval(arg_l[0])().id)
            storage.save()

    def do_show(self, arg):
        """Display the string."""
        arg_l = func(arg)
        ob_dict = storage.all()
        if len(arg_l) == 0:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
        elif len(arg_l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_l[0], arg_l[1]) not in ob_dict:
            print("** no instance found **")
        else:
            print(ob_dict["{}.{}".format(arg_l[0], arg_l[1])])

    def do_destroy(self, arg):
        """Delete a class instance."""
        arg_l = func(arg)
        ob_dict = storage.all()
        if len(arg_l) == 0:
            print("** class name missing **")
        elif arg_l[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
        elif len(arg_l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_l[0], arg_l[1]) not in ob_dict.keys():
            print("** no instance found **")
        else:
            del ob_dict["{}.{}".format(arg_l[0], arg_l[1])]
            storage.save()

    def do_all(self, arg):
        """Display string."""
        arg_l = func(arg)
        if len(arg_l) == 0 or arg_l[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
            return

        obj_l = []
        for obj in storage.all().values():
            if len(arg_l) == 0 or arg_l[0] == obj.__class__.__name__:
                obj_l.append(obj.__str__())
        print(obj_l)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        arg_l = func(arg)
        cnt = 0
        for obj in storage.all().values():
            if arg_l[0] == obj.__class__.__name__:
                cnt += 1
        print(cnt)

    def do_update(self, arg):
        """Update a class instance."""
        arg_l = func(arg)
        ob_dict = storage.all()

        if len(arg_l) == 0:
            print("** class name missing **")
            return False
        if arg_l[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
            return False
        if len(arg_l) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_l[0], arg_l[1]) not in ob_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_l) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_l) == 3:
            try:
                type(eval(arg_l[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_l) == 4:
            obj = ob_dict["{}.{}".format(arg_l[0], arg_l[1])]
            if arg_l[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_l[2]])
                obj.__dict__[arg_l[2]] = valtype(arg_l[3])
            else:
                obj.__dict__[arg_l[2]] = arg_l[3]
        elif type(eval(arg_l[2])) == dict:
            obj = ob_dict["{}.{}".format(arg_l[0], arg_l[1])]
            for keyy, val in eval(arg_l[2]).items():
                if (keyy in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[keyy]) in
                        {str, int, float}):
                    valtype = type(obj.__class__.__dict__[keyy])
                    obj.__dict__[keyy] = valtype(val)
                else:
                    obj.__dict__[keyy] = val
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
