import csv

def get_function_name(f):
    line = f.readline()
    if not line:
        return None
    fname = line.replace('\\_', '_').strip()
    # scrap line "~~~~~~~~"
    line = f.readline()
    return fname

def get_description(f):
    line = f.readline().strip()
    while not line:
        line = f.readline().strip()
    
    return line

def get_format(f):
    line = f.readline().strip()
    while not line == '【形式】':
        line = f.readline().strip()
    
    line = f.readline().strip()
    while not line:
        line = f.readline().strip()

    line = line.replace('\\_', '_').replace('**', '').replace('\\ ', '')
    return line

def _clean_frags(frags):
    ret = []
    for s in frags:
        s = s.strip()
        if s == '':
            continue
        s = s.replace('**', '')
        s = s.replace('\\*', '*')
        ret.append(s)
    if len(ret) < 4:
        return None
    reordered_ret = []
    reordered_ret.append(ret[1])
    reordered_ret.append(ret[0])
    reordered_ret.append(ret[2])
    reordered_ret.append(ret[3])

    return reordered_ret

def get_args(f):
    data = []
    line = f.readline().strip()
    while not line == '【引数】':
        line = f.readline().strip()

    line = f.readline().strip()
    
    line = f.readline().strip()
    while not line == '':
        if line[0] == '+':
            line = f.readline().strip()
            continue
        frags = line.split('|')
        cleaned_frags = _clean_frags(frags)
        if cleaned_frags is None:
            line = f.readline().strip()
            continue
        data.append(cleaned_frags)

        line = f.readline().strip()

    return data

fnames_f = open('ref.txt', 'w')

with open('reference.txt', 'r', encoding='utf-8') as f:
    while True:
        fname = get_function_name(f)
        if fname is None:
            exit()

        desc = get_description(f)
        format = get_format(f)
        args = get_args(f)

        print(fname)

        fnames_f.write('   ' + fname + '\n')

        with open('source/06/03/' + fname + '.rst', 'w', encoding='utf-8') as f2:
            f2.write(fname + '\n')
            f2.write('=' * len(fname) + '\n')
            f2.write('\n')

            f2.write(desc + '\n')
            f2.write('\n')

            f2.write('形式\n')
            f2.write('----\n')

            f2.write('.. code-block:: fortran\n')
            f2.write('\n')
            f2.write('   ' + format + '\n')
            f2.write('\n')

            f2.write('引数\n')
            f2.write('----\n')
            f2.write('\n')

            f2.write('.. csv-table:: ' + fname + ' の引数\n')
            f2.write('   :file: ' + fname + '_args.csv\n')
            f2.write('   :header-rows: 1\n')
            f2.write('\n')

        with open('source/06/03/' + fname + '_args.csv', 'w', encoding='utf-8') as f2:
            w = csv.writer(f2, lineterminator='\n')
            w.writerows(args)

fnames_f.close()
