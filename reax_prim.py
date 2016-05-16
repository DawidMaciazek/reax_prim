import random
from collections import OrderedDict


class Potential:
    def __init__(self, input):
        # check if inup instance or file

        # input is file
        self.read(input)

    def __getitem__(self, key):
        s = key[0]-1  # section
        r = key[1]-1  # record
        if s != 0:
            f = key[2]-1  # field

        if s == 0:
            return self.general_record[r]
        elif s == 1:
            return self.atomic_record[r][f]
        elif s == 2:
            return self.bond_record[r][f]
        elif s == 3:
            return self.odiagonal_record[r][f]
        elif s == 4:
            return self.angle_record[r][f]
        elif s == 5:
            return self.torsion_record[r][f]
        elif s == 6:
            return self.hbond_record[r][f]
        else:
            None

    def __setitem__(self, key, value):
        s = key[0]-1  # section
        r = key[1]-1  # record
        if s != 0:
            f = key[2]-1  # field

        if s == 0:
            self.general_record[r] = value
        elif s == 1:
            self.atomic_record[r][f] = value
        elif s == 2:
            self.bond_record[r][f] = value
        elif s == 3:
            self.odiagonal_record[r][f] = value
        elif s == 4:
            self.angle_record[r][f] = value
        elif s == 5:
            self.torsion_record[r][f] = value
        elif s == 6:
            self.hbond_record[r][f] = value

    def read(self, input_name):
        self.input_file = open(input_name, 'r')
        self._read_general()
        self._read_atomic()
        self._read_bond()
        self._read_off_diagonal()
        self._read_angle()
        self._read_torsion()
        self._read_hbond()

        self.input_file.close()

    def _read_general(self):
        input_file = self.input_file
        # header comment
        self.general_comment = input_file.readline()

        line = input_file.readline()
        general_count = int(line.split()[0])
        self.general_count = general_count

        general_record = []
        general_record_comment = []
        for record in range(general_count):
            line = input_file.readline()
            sp = line.split()

            general_record.append(float(sp[0]))
            general_record_comment.append(' '.join(sp[1:]))

        self.general_record = general_record
        self.general_record_comment = general_record_comment

    def _read_atomic(self):
        input_file = self.input_file

        # process comment lines
        # 1st line of comment
        line = input_file.readline()
        sp = line.split()
        atomic_count = int(sp[0])
        self.atomic_count = atomic_count

        atomic_comment = []
        atomic_comment.append(' '.join(sp[1:]))

        # 2nd 3rd 4th comment line
        for i in range(3):
            line = input_file.readline()
            sp = line.split()
            atomic_comment.append(' '.join(sp))

        self.atomic_comment = atomic_comment

        # loop over all specified atoms
        atomic_element = []
        atomic_record = []
        for singel_atom in range(atomic_count):
            # 1st line with element symbol
            atomic_record_part = []
            line = input_file.readline()
            sp = line.split()
            atomic_element.append(sp[0])

            for record_index in range(8):
                atomic_record_part.append(float(sp[record_index + 1]))

            # 2nd 3rd 4th line have 8 records each
            for single_line in range(3):
                line = input_file.readline()
                sp = line.split()

                for record_index in range(8):
                    atomic_record_part.append(float(sp[record_index]))

            atomic_record.append(atomic_record_part)

        self.atomic_element = atomic_element
        self.atomic_record = atomic_record

    def _read_bond(self):
        input_file = self.input_file
        line = input_file.readline()
        sp = line.split()

        # process 1st line with atom types
        bond_count = int(sp[0])
        self.bond_count = bond_count
        bond_comment = [' '.join(sp[1:])]

        # process 2nd comment line
        line = input_file.readline()
        sp = line.split()
        bond_comment.append(' '.join(sp))
        self.bond_comment = bond_comment

        bond_atom = []
        bond_record = []
        for record in range(bond_count):
            line = input_file.readline()
            sp = line.split()

            # atom types
            bond_atom_part = [int(sp[0]), int(sp[1])]

            # 1st records line
            bond_record_part = []
            for index_record in range(8):
                bond_record_part.append(float(sp[index_record + 2]))

            # 2nd records line
            line = input_file.readline()
            sp = line.split()
            for index_record in range(8):
                bond_record_part.append(float(sp[index_record]))

            bond_atom.append(bond_atom_part)
            bond_record.append(bond_record_part)

        self.bond_atom = bond_atom
        self.bond_record = bond_record

    def _read_off_diagonal(self):
        input_file = self.input_file
        line = input_file.readline()
        sp = line.split()

        # comment line
        odiagonal_count = int(sp[0])
        self.odiagonal_count = odiagonal_count

        odiagonal_comment = ' '.join(sp[1:])
        self.odiagonal_comment = odiagonal_comment

        odiagonal_atom = []
        odiagonal_record = []
        for record in range(odiagonal_count):
            input_file = self.input_file
            line = input_file.readline()
            sp = line.split()

            odiagonal_atom.append([int(sp[0]), int(sp[1])])

            odiagonal_record_part = []
            for index_odiagonal in range(6):
                odiagonal_record_part.append(float(sp[index_odiagonal + 2]))

            odiagonal_record.append(odiagonal_record_part)

        self.odiagonal_atom = odiagonal_atom
        self.odiagonal_record = odiagonal_record

    def _read_angle(self):
        input_file = self.input_file
        line = input_file.readline()
        sp = line.split()

        # comment line
        angle_count = int(sp[0])
        self.angle_count = angle_count

        angle_comment = ' '.join(sp[1:])
        self.angle_comment = angle_comment

        angle_atom = []
        angle_record = []
        for record in range(angle_count):
            input_file = self.input_file
            line = input_file.readline()
            sp = line.split()

            # atom index
            angle_atom.append([int(sp[0]), int(sp[1]), int(sp[2])])

            # records
            angle_record_part = []
            for index_atom in range(7):
                angle_record_part.append(float(sp[index_atom+3]))

            angle_record.append(angle_record_part)

        self.angle_atom = angle_atom
        self.angle_record = angle_record

    def _read_torsion(self):
        input_file = self.input_file
        line = input_file.readline()
        sp = line.split()

        # comment line
        torsion_count = int(sp[0])
        self.torsion_count = torsion_count

        torsion_comment = ' '.join(sp[1:])
        self.torsion_comment = torsion_comment

        torsion_atom = []
        torsion_record = []
        for record in range(torsion_count):
            input_file = self.input_file
            line = input_file.readline()
            sp = line.split()

            # atom index
            torsion_atom.append([int(sp[0]), int(sp[1]),
                                 int(sp[2]), int(sp[3])])

            # records
            torsion_record_part = []
            for index_atom in range(7):
                torsion_record_part.append(float(sp[index_atom+4]))

            torsion_record.append(torsion_record_part)

        self.torsion_atom = torsion_atom
        self.torsion_record = torsion_record

    def _read_hbond(self):
        input_file = self.input_file
        line = input_file.readline()
        sp = line.split()

        # comment line
        hbond_count = int(sp[0])
        self.hbond_count = hbond_count

        hbond_comment = ' '.join(sp[1:])
        self.hbond_comment = hbond_comment

        hbond_atom = []
        hbond_record = []
        for record in range(hbond_count):
            input_file = self.input_file
            line = input_file.readline()
            sp = line.split()

            # atom index
            hbond_atom.append([int(sp[0]), int(sp[1]), int(sp[2])])

            # records
            hbond_record_part = []
            for index_atom in range(4):
                hbond_record_part.append(float(sp[index_atom+3]))

            hbond_record.append(hbond_record_part)

        self.hbond_atom = hbond_atom
        self.hbond_record = hbond_record

    def write(self, output_name):
        self.output_file = open(output_name, 'w')
        self._write_general()
        self._write_atomic()
        self._write_bond()
        self._write_off_diagonal()
        self._write_angle()
        self._write_torsion()
        self._write_hbond()

        self.output_file.close()

    def _write_general(self):
        output_file = self.output_file

        # comment
        if '\n' in self.general_comment:
            line = self.general_comment
        else:
            line = self.general_comment + '\n'

        output_file.write(line)

        line = '{:>3}{:>7}{}\n'.format(self.general_count,
                                       '', '! Number of general parameters')
        output_file.write(line)

        # all general reocrd
        #for record in range(self.general_count):
        general_record = self.general_record
        general_record_comment = self.general_record_comment
        for record in range(self.general_count):
            line = '{:>10.4f} {}\n'.format(general_record[record],
                                           general_record_comment[record])
            output_file.write(line)

    def _write_atomic(self):
        output_file = self.output_file
        atomic_count = self.atomic_count

        # comment line
        line = '{:>3}{:>4}{}\n'.format(atomic_count, '',
                                       self.atomic_comment[0])
        output_file.write(line)

        for i in range(3):
            line = '{:>12}{}\n'.format('', self.atomic_comment[i+1])
            output_file.write(line)

        # single atom
        for atom in range(atomic_count):
            atomic_record = self.atomic_record[atom]
            line = ' {:<2} '.format(self.atomic_element[atom])

            cr = 0
            for i in range(8):
                line += '{:>8.4f}'.format(atomic_record[cr])
                cr += 1

            line += '{:>5}\n{:>3}'.format('', '')
            for i in range(8):
                line += '{:>9.4f}'.format(atomic_record[cr])
                cr += 1

            line += '{:>5}\n{:>3}'.format('', '')
            for i in range(8):
                line += '{:>9.4f}'.format(atomic_record[cr])
                cr += 1

            line += '{:>5}\n{:>3}'.format('', '')
            for i in range(8):
                line += '{:>9.4f}'.format(atomic_record[cr])
                cr += 1

            line += '{:>5}\n'.format('')

            output_file.write(line)

    def _write_bond(self):
        output_file = self.output_file
        bond_count = self.bond_count

        # comment line
        line = '{:>3}{:>6}{}\n'.format(bond_count, '',
                                       self.bond_comment[0])
        line += '{:>22}{}\n'.format('', self.bond_comment[1])
        output_file.write(line)

        # bonds
        for bond in range(bond_count):
            bond_record = self.bond_record[bond]
            bond_atom = self.bond_atom[bond]
            line = '{:>3}{:>3}'.format(bond_atom[0], bond_atom[1])

            cr = 0
            for i in range(8):
                line += '{:>9.4f}'.format(bond_record[cr])
                cr += 1

            line += '{:>2}\n{:>6}'.format('', '')
            for i in range(8):
                line += '{:>9.4f}'.format(bond_record[cr])
                cr += 1

            line += '{:>2}\n'.format('')
            output_file.write(line)

    def _write_off_diagonal(self):
        output_file = self.output_file
        odiagonal_count = self.odiagonal_count

        # comment line
        line = '{:>3}{:>4}{}\n'.format(odiagonal_count, '',
                                       self.odiagonal_comment)

        output_file.write(line)

        # off diagonal
        for odiagonal in range(odiagonal_count):
            odiagonal_atom = self.odiagonal_atom[odiagonal]
            odiagonal_record = self.odiagonal_record[odiagonal]
            line = '{:>3}{:>3}'.format(odiagonal_atom[0], odiagonal_atom[1])

            for i in range(6):
                line += '{:>9.4f}'.format(odiagonal_record[i])

            line += '{:>20}\n'.format('')
            output_file.write(line)

    def _write_angle(self):
        output_file = self.output_file
        angle_count = self.angle_count

        # comment line
        line = '{:>3}{:>4}{}\n'.format(angle_count, '',
                                       self.angle_comment)

        output_file.write(line)

        # off diagonal
        for angle in range(angle_count):
            angle_atom = self.angle_atom[angle]
            angle_record = self.angle_record[angle]
            line = '{:>3}{:>3}{:>3}'.format(angle_atom[0], angle_atom[1],
                                       angle_atom[2])

            for i in range(7):
                line += '{:>9.4f}'.format(angle_record[i])

            line += '{:>8}\n'.format('')
            output_file.write(line)

    def _write_torsion(self):
        output_file = self.output_file
        torsion_count = self.torsion_count

        # comment line
        line = '{:>3}{:>4}{}\n'.format(torsion_count, '',
                                       self.torsion_comment)

        output_file.write(line)

        # off diagonal
        for torsion in range(torsion_count):
            torsion_atom = self.torsion_atom[torsion]
            torsion_record = self.torsion_record[torsion]
            line = '{:>3}{:>3}{:>3}{:>3}'.format(torsion_atom[0],
                                                 torsion_atom[1],
                                                 torsion_atom[2],
                                                 torsion_atom[3])
            for i in range(7):
                line += '{:>9.4f}'.format(torsion_record[i])

            line += '{:>5}\n'.format('')
            output_file.write(line)

    def _write_hbond(self):
        output_file = self.output_file
        hbond_count = self.hbond_count

        # comment line
        line = '{:>3}{:>4}{}\n'.format(hbond_count, '',
                                       self.hbond_comment)

        output_file.write(line)

        # off diagonal
        for hbond in range(hbond_count):
            hbond_atom = self.hbond_atom[hbond]
            hbond_record = self.hbond_record[hbond]
            line = '{:>3}{:>3}{:>3}'.format(hbond_atom[0],  hbond_atom[1],
                                            hbond_atom[2])
            for i in range(4):
                line += '{:>9.4f}'.format(hbond_record[i])

            line += '{:>35}\n'.format('')
            output_file.write(line)

    def set_random(self, param, range_min, range_max):
        self[(param)] = random.uniform(range_min, range_max)


class Param:
    def __init__(self, input=None):
        self.params = OrderedDict()
        if input:
            self.read(input)

    def read(self, input_name):
        input_file = open(input_name, 'r')

        for line in input_file:
            sp = line.split()
            if len(sp) < 7:
                comment = None
            else:
                comment = ' '.join(sp[6:])

            self.add((int(sp[0]), int(sp[1]), int(sp[2])), float(sp[3]),
                     float(sp[4]), float(sp[5]), comment)

        input_file.close()

    def add(self, key, step, value_min, value_max, comment=None):
        if not comment:
            comment = "!no-comment"
        if '!' not in comment:
            comment = '!' + comment
        if '\n' in comment:
            comment = comment.rstrip()

        if len(key) == 2:
            key = (key[0], key[1], 1)

        key_string = '{0}-{1}-{2}'.format(*key)
        self.params[key_string] = [[key[0], key[1], key[2]],
                                   step, value_min, value_max, comment]

    def write_seq(self, output_name, repeat):
        output_file = open(output_name, 'w')

        params = self.params
        repeat_line = ''
        for key in params.keys():
            par = params[key]
            line = '{:>3}{:>3}{:>3}{:>8.4f}{:>10.4f}{:>10.4f}{:<4}{}\n'.format(
                par[0][0], par[0][1], par[0][2], par[1], par[2], par[3], '',
                par[4])

            repeat_line += line

        for rep in range(repeat):
            output_file.write(repeat_line)

        output_file.close()

    def write_random_order(self, output_name, repeat):
        params = self.params

        output_file = open(output_name, 'w')
        for i in range(repeat):
            par = random.choice(list(params.values()))
            line = '{:>3}{:>3}{:>3}{:>8.4f}{:>10.4f}{:>10.4f}{:<4}{}\n'.format(
                par[0][0], par[0][1], par[0][2], par[1], par[2], par[3], '',
                par[4])

            output_file.write(line)
