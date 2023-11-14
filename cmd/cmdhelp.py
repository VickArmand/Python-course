#!/usr/bin/python3
import cmd
"""
help handlers can be created by implementing a method named in the following way:
help_<command_name> eg: for the command greet the help handler will be the help_greet method
"""
class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, person):
        if person:
            print ("hi,", person)
        else:
            print ('hi')
    
    def help_greet(self):
        print ('\n'.join([ 'greet [person]',
                           'Greet the named person',
                           ]))
    
    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()
