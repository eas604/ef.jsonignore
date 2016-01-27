#!/usr/bin/env python2
# vim: set fileencoding=utf-8 :
"""
Add [Newtonsoft.Json.JsonIgnore] to EF navigation properties
so they serialize correctly
"""

import os

for root, dirs, files in os.walk(os.getcwd()):
    files[:] = [f for f in files if f[-3:].lower() == '.cs']

    for f in files:
        print('File {0}'.format(f))

        write = ''
        modified = False

        with open('{0}\\{1}'.format(root, f), 'r') as f_open:
            for line in  f_open.readlines():
                if line.strip() == '[Newtonsoft.Json.JsonIgnore]':
                    line = ''
                    modified= True
                elif line.strip().startswith('public virtual') and line.strip().endswith('{ get; set; }'):
                    print('Old line: {0}'.format(line))
                    line = '        [Newtonsoft.Json.JsonIgnore]\n{0}'.format(line)
                    print('New line: {0}'.format(line))
                    modified = True
                write += '{0}\n'.format(line.rstrip())

        if modified:
            with open(f, 'w') as f_open:
                f_open.write(write)

        del write

print('Done.')
