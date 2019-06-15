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
        for line in method_lines:
            line.replace('func ', '')
            line = "**" + line + "**" + " **(** "line[line.find("(")+1:line.find(")")] + "**)**"
            #Here we still need to write the table
        for line in signal_lines:
            line.replace('signal ', '')

    finally:
        output_file.close()
