import os

def create_config_file():
    header = """#FIRST: OUTPUT PATH
#SECOND: NAME
#THIRD: MAINFILE
#AFTER: FUNCTIONFILES
"""
    with open('CompileCOBOL', 'w') as f:
        f.write(header)


def compile_from_file():
    print("RUNNING Z-COBOL-COMPILER")

    if not os.path.exists('CompileCOBOL'):
        create_config_file()
        print("Z-COBOL-COMPILER: CREATED CONFIG FILE \n - fill out config before running again")
        return




    extensions = input("(extensions) has -x -o: ")
    with open("CompileCOBOL", 'r') as f:
        lines = f.readlines()
    lines = [line for line in lines if not line.startswith('#') and not line.startswith(' ') and not line.startswith('\n')]
    
    print("Z-COBOL-COMPILER: LOADED CONFIG")

    

    #Define Variables From Config Array
    print(lines)
    output = lines[0]
    source = lines[1]
    name = lines[2]
    main_file = lines[3]
    secondary_files_exist = False
    secondary_files = lines[4:]
    if(len(secondary_files) > 0):
        secondary_files_exist = True

    print("Z-COBOL-COMPILER: STARTING FUNCTION COMPILATION")
    temp_file_path = "temp"

    if not os.path.exists(output[2:-2]):
        os.makedirs(output[:-1])

    if os.path.exists(temp_file_path):
        os.system('rm -r ./temp')

    os.makedirs(temp_file_path)
    for file in secondary_files:
        print(f"Z-COBOL-COMPILER: COMPILING {file[:-4]}")
        os.system(f"cobc -c -o ./temp/{file[:-4]}.o {source[:-1]}{file}")
        
    print("Z-COBOL-COMPILER: FINISHED FUNCTIONS COMPILATIONS")
    

    # Format Final Command
    final_gnucobol_command = f'cobc -x {extensions} -o {output}{name} {source[:-1]}{main_file}'
    for file in secondary_files:
        final_gnucobol_command += f' ./{temp_file_path}/{file[:-4]}.o'
    final_gnucobol_command = final_gnucobol_command.replace("\n", '')

    print("Z-COBOL-COMPILER: RUNNING FINAL COMPILE")
    os.system(final_gnucobol_command) # Exicute Final Compile Command

    print("Z-COBOL-COMPILER: COMPILATION COMPLETE")

    os.system('rm -r ./temp') # Clear ./temp/ folder
    
if __name__ == "__main__":
    compile_from_file()
    