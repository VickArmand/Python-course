#!/usr/bin/python3
"""
The cmd module contains one public class, 
Cmd, designed to be used as a base class for command processors
such as interactive shells and other command interpreters.

The interpreter uses a loop to read all lines from its input, parse them,
and then dispatch the command to an appropriate command handler.
Input lines are parsed into two parts. The command, and any other text on the line.

All methods must be prefixed by "do_" or "complete_" or "help_" to indicate that they are command handlers
One can also override methods in the Cmd class
The command handlers(methods) must be prefixed by "do_" eg: if the command is greet the handler is do_greet
If the user enters a command "foo bar", and your class includes a method named do_foo(),
it is called with "bar" as the only argument.

The end-of-file marker is dispatched to do_EOF().
If a command handler returns a true value, the program will exit cleanly.
So to give a clean way to exit your interpreter, make sure to implement do_EOF() and have it return True.
Since do_EOF() returns True, typing Ctrl-D will drop us out of the interpreter.

help prints the documented and undocumented commands
By documented we mean the method has a docstring
help <command name> prints the docstring/ help text for the command
"""
import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, line):
        """Prints hello"""
        print ("hello")
    
    def do_EOF(self, line):
        """Exits the cmd when you use Ctrl + D or input EOF"""
        return True

if __name__ == '__main__':
    # run it interactively using:
    # python cmdx.py
    HelloWorld().cmdloop()