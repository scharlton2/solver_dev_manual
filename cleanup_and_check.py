"""
Sctipt to cleanup and check *.rst files under source folder.
"""

import os

def cleanup_and_check_file(filename):
    """Cleanup and check file"""
    (n, ext) = os.path.splitext(filename)
    if not ext == '.rst':
        return

    print('cleaning up ' + filename)
    f = open(filename, 'r', encoding='utf-8')
    input_lines = f.readlines()
    f.close()
    output_lines = []

    code_mode = False

    for line in input_lines:
        if not code_mode:
            if 'code-block' in line:
                # print('code-block found')
                # print(line)
                code_mode = True
        else:
            if len(line.strip()) != 0 and not line[0] == ' ':
                # print('code-block ended')
                # print(line)
                code_mode = False

        if not code_mode:
            line = line.replace('\\\\"', '"').replace('"', '\\\\"')

        output_lines.append(line)

    f = open(filename, 'w', encoding='utf-8')
    f.writelines(output_lines)
    f.close()

def cleanup_and_check_folder(folder):
    """Recursively cleanup and check files in the folder"""

    files = os.listdir(folder)
    for f in files:
        full_name = folder + '/' + f
        if os.path.isfile(full_name):
            cleanup_and_check_file(full_name)
        else:
            cleanup_and_check_folder(full_name)

cleanup_and_check_folder('source')
