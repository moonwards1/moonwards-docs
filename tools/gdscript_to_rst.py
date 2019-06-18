#!/usr/bin/python
import os
import sys, getopt
signal_lines = []
property_lines = []
method_lines = []
variable_lines = []
remote_methods =[]
puppet_methods = []
master_methods = []
remote_variables = []
puppet_variables = []
master_varaibles = []
extends = ""
keywords = ['signal', 'var', 'export', 'func', 'extends']

def get_size_for(list):
    max = 0
    for elements in list:
        if len(elements)>max:
            max=len(elements)
    return max


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'gdscript_to_rst.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    head, tail = os.path.split(inputfile)
    tail = tail[0:-3]
    with open(inputfile,"r") as input_file:
        print("Input file open!!")
        line = input_file.readline()
        while line != '':
            if line.find("#")!=-1:
                line=line[0:line.find("#")]
            if any(keyword in line for keyword in keywords):

                if 'extends ' in line:
                    extends = line.replace('extends', '')
                    #continue
                if 'signal ' in line:
                    if not 'emit_signal' in line:
                        signal_lines.append(line)
                        #continue
                if 'var ' in line:
                    variable_lines.append(line)
                #    continue
                if 'export ' in line:
                    property_lines.append(line)
                #    continue
                if 'func ' in line:
                    if 'remote ' in line:
                        remote_methods.append(line)
                    method_lines.append(line)
                #    continue
            line = input_file.readline()
        method_lines.sort()
        signal_lines.sort()
        property_lines.sort()
        variable_lines.sort()

    with open(outputfile,"w+") as output_file:
        print("Output File opened!!")
        output_file.write(tail+"\n")
        for i in range(0,len(tail)):
            output_file.write("=")
        output_file.write("\n\n")
        output_file.write("**Inherits:**" + ":godot_class:`"+extends.rstrip(' \n')+ "`\n\n")
        output_file.write("**Category:** <FILL THIS SPACE>\n\n")
        output_file.write("Brief Description\n-----------------\n")
        output_file.write("\n<FILL A BRIEF DESCRIPTION HERE>\n\n")
        output_file.write("Methods\n-------\n")

# This block of code will format the methods #

        for index in range(0,len(method_lines)):
            method_lines[index] = method_lines[index].replace('func ', '')
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
            output_file.write(" | ")
            to_write = ":ref:`" + line[0:line.find("(")] + "<"
            to_write = to_write + tail + "_method_"+line[0:line.find("(")]+">`"
            to_write = to_write + " **(** " + line[line.find("(")+1:line.find(")")] + " **)** "
            output_file.write(to_write) #Writes a reference to descriptions

            for times in range(0,final_line_lenght-len(to_write)-1):
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

        output_file.write("\nSignals\n-------\n\n")

# Here starts the signal formatting #
        for index in range(0,len(signal_lines)):
            signal_lines[index] = signal_lines[index].replace('signal ', '')

        for line in signal_lines:
            if line.find("(")!=-1:
                line_to_write = "**" + line[0:line.find("(")].rstrip(' \n') + "**"
                line_to_write = line_to_write + " **(** " + line[line.find("(")+1:line.find(")")].rstrip(' \n') + " **)** "
                output_file.write(".. _"+tail+"_signal_"+line[0:line.find("(")].rstrip(' \n')+":\n\n")
                output_file.write("- "+line_to_write+"\n\n")
            else:
                output_file.write(".. _"+tail+"_signal_"+line.rstrip(' \n')+":\n\n")
                output_file.write("- **" + line.rstrip(' \n') + "** **(** **)**\n\n")
            output_file.write("!<FILL DESCRIPTION HERE>!\n\n")

        output_file.write("Description\n-----------\n\n!<FILL DESCRIPTION HERE>!\n\n")
        output_file.write("Method Descriptions\n-------------------\n\n")

        for line in method_lines:
            output_file.write(".. _"+tail+"_method_"+line[0:line.find("(")]+":\n\n")
            line_to_write = "- :godot_class:`Title <FILL>` **" + line[0:line.find("(")]
            line_to_write = line_to_write + "** **(** "+line[line.find("(")+1:line.find(")")]+" **)**\n\n"
            output_file.write(line_to_write)
            output_file.write("!<FILL DESCRIPTION HERE>!\n\n")

if __name__ == "__main__":
   main(sys.argv[1:])
