#!/usr/bin/python
import os
import sys, getopt
extends = ""
keywords = ['signal', 'var', 'export', 'func', 'extends']

def print_subtitle(output_file, title):
    output_file.write("\n"+title+"\n")
    for letters in title:
        output_file.write("-")
    output_file.write("\n\n")

def delete_word(list, word):
    for index in range(0,len(list)):
        list[index] = list[index].replace(word, '')
    return list


def get_size_for(list):
    max = 0
    for elements in list:
        if len(elements)>max:
            max=len(elements)
    return max

def print_descriptions(output_file, tail, title, type, list):

    output_file.write("Method Descriptions\n-------------------\n\n")
    for line in list:
        output_file.write(".. _"+tail+"_"+type+"_"+line[0:line.find("(")]+":\n\n")
        line_to_write = "- :godot_class:`CHANGE THIS<object>` **" + line[0:line.find("(")]
        line_to_write = line_to_write + "** **(** "+line[line.find("(")+1:line.find(")")]+" **)**\n\n"
        output_file.write(line_to_write)
        output_file.write("!<FILL DESCRIPTION HERE>!\n\n")

def print_as_list(output_file, tail, title, type, list):

    print_subtitle(output_file, title)

# Here starts the signal formatting #
    for index in range(0,len(list)):
        list[index] = list[index].replace(type+" ", '')

    for line in list:
        if line.find("(")!=-1:
            line_to_write = "**" + line[0:line.find("(")].rstrip(' \n') + "**"
            line_to_write = line_to_write + " **(** " + line[line.find("(")+1:line.find(")")].rstrip(' \n') + " **)** "
            output_file.write(".. _"+tail+"_"+type+"_"+line[0:line.find("(")].rstrip(' \n')+":\n\n")
            output_file.write("- "+line_to_write+"\n\n")
        else:
            output_file.write(".. _"+tail+"_"+type+"_"+line.rstrip(' \n')+":\n\n")
            output_file.write("- **" + line.rstrip(' \n') + "** **(** **)**\n\n")
        output_file.write("!<FILL DESCRIPTION HERE>!\n\n")



def print_as_table(output_file, tail, title, type, list):

    print_subtitle(output_file, title)

    final_line_lenght = 55+2*get_size_for(list) # 55 is the longest godot class twice

# This code block will write the  table #

    for line in list:

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
        to_write = to_write + tail + "_"+type+"_"+line[0:line.find("(")]+">`"
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

def main(argv):
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
                    if not 'emit_signal' in line and not '_signal' in line:
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
                    else:
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
        output_file.write("**Inherits:** " + ":godot_class:`"+extends[1:len(extends)].rstrip(' \n')+" <"+extends[1:len(extends)].rstrip(' \n').lower()+">"+ "`\n\n")
        output_file.write("**Category:** <FILL THIS SPACE>\n\n")
        output_file.write("Brief Description\n-----------------\n")
        output_file.write("\n<FILL A BRIEF DESCRIPTION HERE>\n\n")

        if len(property_lines)>0:
            property_lines = delete_word(property_lines, 'var ')
            property_lines = delete_word(property_lines, 'export ')
            print_as_table(output_file, tail, "Properties", 'export', property_lines)

        if len(method_lines)>0:
            method_lines = delete_word(method_lines,'func ')
            print_as_table(output_file, tail,"Methods","method",method_lines)

        if len(remote_methods)>0:
            remote_methods = delete_word(remote_methods,'remote ')
            remote_methods = delete_word(remote_methods,'func ')
            print_as_table(output_file, tail,"Remote Methods","r_method",remote_methods)

        if len(signal_lines)>0:
            signal_lines = delete_word(signal_lines,'signal ')
            print_as_list(output_file, tail,"Signals","signal",signal_lines)

        output_file.write("Description\n-----------\n\n!<FILL DESCRIPTION HERE>!\n\n")

        if len(method_lines)>0:
            print_as_list(output_file, tail, "Methods Descriptions","method",method_lines)

        if len(remote_methods)>0:
            print_as_list(output_file, tail, "Remote Methods Descriptions","r_method",remote_methods)

if __name__ == "__main__":
   main(sys.argv[1:])
