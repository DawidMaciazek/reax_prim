#!/usr/bin/python3.4
from subprocess import Popen
import random
import sys
import os
import shutil

class Record:
    def __init__(self, record_str):
        sp = record_str.split()
        self.cat = int(sp[0])
        self.line = int(sp[1])
        self.entry = int(sp[2])
        self.incr = float(sp[3])
        self.min = float(sp[4])
        self.max = float(sp[5])
        self.comm = "".join(sp[6:]) if len(sp) >= 7 else '!nocomm'

    def get(self, r_incr=None, r_fork=None):
        incr = self.incr
        vmin = self.min
        vmax = self.max

        if r_incr and r_incr > 1.0:
            incr = incr*random.uniform(1.0, r_incr)

        if r_fork and r_fork > 0.0:
            vmin = vmin*random.uniform(1.0, r_fork)
            vmax = vmax*random.uniform(1.0, r_fork)
            if vmax < vmin:
                vmax = self.max
                vmin = self.min

        return '{:>3}{:>4}{:>5}   {:<5.4f}  {:<5.4f}  {:<5.4f}    {}\n'.format(
            self.cat, self.line, self.entry, incr, vmin, vmax, self.comm)
class Params:
    def __init__(self, param_name):
        records = []
        with open(param_name, 'r') as fp:
            for line in fp:
                record = Record(line)
                records.append(record)
        self.records = records

    def write(self, output, repetition, r_incr=None, r_frok=None):
        fp = open(output, 'w')
        records = self.records
        records_cnt = len(records)
        for rep in range(repetition):
            rand_record = random.randrange(0, records_cnt)
            fp.write(records[rand_record].get(r_incr,r_frok))

def create_folder(output, template):
    os.mkdir(output)
    file_list = os.listdir(template)
    file_list.remove('params')
    for file_name in file_list:
        full_file_name = os.path.join(template, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, output)


def main():
    arg = sys.argv[1:]
    arglen = len(arg)
    if arglen < 1:
        print('Need at least 1 arg!.... compro')
        sys.exit(1)

    if arg[0] == '-h':
        print('Usage:\n\t./reax_prim  out_folder  repetition  incr_ramp  fork_ramp')
        sys.exit(0)

    output_file = arg[0]
    if os.path.isdir(output_file):
        print('File {} exist! rm -r by your self'.format(output_file))
        sys.exit(1)

    template='template'
    if not os.path.isdir(template):
        print('Cant find {} file in current directory'.format(template))
        sys.exit(1)

    rep = 1000 if (arglen < 2) else int(arg[0])
    incr_ramp = 1 if (arglen < 3) else int(arg[1])
    fork_ramp = 1 if (arglen < 4) else int(arg[2])

    # create folder
    create_folder(output_file, template)
    params = Params('template/params')
    params_file = output_file + '/params'
    params.write(params_file, rep, incr_ramp, fork_ramp)

    # run scrip in backgroung
    os.chdir(output_file)
    exec_name = '../bash_process.sh'
    print("Process spawned for directory %s" % output_file)
    proc = Popen(["nohup", exec_name], stdout=open('/dev/null', 'w'),
                 stderr=open('logfile.log', 'a'))


if __name__ == '__main__':
    main()
