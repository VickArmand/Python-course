#!/usr/bin/python3
import cmd
"""
In addition to the methods described above, there are several attributes for controlling command interpreters.
prompt can be set to a string to be printed each time the user is asked for a new command.
intro is the “welcome” message printed at the start of the program. cmdloop() takes an argument for this value, or you can set it on the class directly.
When printing help, the doc_header, misc_header, undoc_header, and ruler attributes are used to format the output.
"""
class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    prompt = 'prompt: '
    intro = "Simple command processor example."

    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'
    
    ruler = '-'
    
    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()