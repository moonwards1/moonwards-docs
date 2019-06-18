#!/usr/bin/python
import os
import sys, getopt
signal_lines = []
property_lines = []
method_lines = []
variable_lines = []
extends = ""
keywords = ['signal', 'var', 'export', 'func', 'extends']

def get_size_for(list):
    max = 0
    for elements in list:
        if elements.len()>max:
            max=elements.len()
    return max


def main(argv):
    head, tail = os.path.split(argv[1])
    with open(argv[1],r) as input_file:
        line = reader.readline()
        while line != '':
            if any(keyword in line for keyword in keywords):
                if keyword == 'extends':
                    extends = line
                if keyword == 'signal':
                    signal_lines.append(line)
                if keyword == 'var':
                    variable_lines.append(line)
                if keyword == 'export':
                    property_lines.append(line)
                if keyword == 'func':
                    method_lines.append(line)
            line = input_file.readline()

    with open(argv[2],rw) as output_file:
        output_file.write(tail+"\n")
        for i in range(0,tail.len()):
            output_file.write("=")
        output_file.write("\n")
        extends.replace('extends, '')
        output_file.write("**Inherits:**" + ":godot_class:`"+extends + "`\n")
        output_file.write("**Category:** <FILL THIS SPACE>\n")
        output_file.write("Brief Description\n-----------------\n")
        output_file.write("\n<FILL A BRIEF DESCRIPTION HERE>\n")
        output_file.write("Methods\n-------\n")

# This block of code will format the methods #

        for line in method_lines:
            line.replace('func ', '')
            #line = "**" + line + "**" + " **(** "+ line[line.find("(")+1:line.find(")")] + "**)**"

# Ends the method formatting

        final_line_lenght = 55+2*get_size_for(method_lines) # 55 is the longest godot class twice

# This code block will write the methods table #

        for line in method_lines:

            output_file.write("+")
            for times in range(0,55):
                output_file.write("-")
            output_file.write("+")
            for times in range(0,final_line_lenght):
                output_file.write("-")
            output_file.write("+\n|")
            for times in range(0,54):
                output_file.write(" ")
            output_file.write("| ")
            to_write = ":ref:`" + line[0:line.find("(")-1] + "<"
            to_write = to_write + tail + "_method_"+line[0:line.find("(")-1]+">`"
            to_write = to_write + " **(** " + line[line.find("(")+1:line.find(")")-1] + " **)** "
            output_file.write(to_write) #Writes a reference to descriptions

            for times in range(0,final_line_lenght-to_write.len()-1):
                output_file.write(" ")
            output_file.write("|\n")

# Here ends the contents of the table #

        output_file.write("+")
        for times in range(0,55):
            output_file.write("-")
        output_file.write("+")
        for times in range(0,final_line_lenght):
            output_file.write("-")
        output_file.write("+\n")

# At this point the table has been completely written

        output_file.write("Signals\n-------\n\n")

# Here starts the signal formatting #
        for line in signal_lines:
            line.replace('signal ', '')

        for line in signal_lines:
            if line.find("(")!=-1:
                line_to_write = "**" + line + "**"
                line_to_write = line_to_write + " **(** " + line[line.find("(")+1:line.find(")")-1] + " **)** "
                output_file.write(".. _"+tail+"_signal_"+line[0:line.find("(")]+":\n\n")
                output_file.write("- "+line_to_write+"\n\n")
            else:
                output_file.write(".. _"+tail+"_signal_"+line+":\n\n")
                output_file.write("- **" + line + "** **(** **)**\n\n")
            output_file.write("!<FILL DESCRIPTION HERE>!\n\n")

        output_file.write("Description\n-----------\n\n!<FILL DESCRIPTION HERE>!\n\n")
        output_file.write("Method Descriptions\n-------------------\n\n")

        for line in method_lines:
            output_file.write(".. _"+tail+"_method_"+line[0:line.find("(")-1]+":\n\n")
            line_to_write = "- :godot_class:`Title <FILL>` **" + line[0:line.find("(")-1]
            line_to_write = line_to_write + "** **(** "+line[line.find("("):line.find(")")]+" **)**\n\n"
            output_file.write(line_to_write)
            output_file.write("!<FILL DESCRIPTION HERE>!\n\n")


    finally:
        output_file.close()
