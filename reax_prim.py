class Potential:
    def __init__(self, input):
        # check if inup instance or file

        # input is file
        self.read(input)

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
        print(atomic_comment)

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
                odiagonal_record_part.append(sp[index_odiagonal + 2])

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

        self.output_file.close()

    def _write_general(self):
        output_file = self.output_file

        # comment
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
            line = '{:>2} '.format(self.atomic_element[atom])

            cr = 0
            for i in range(8):
                line += '{:>9.4f}'.format(atomic_record[cr])
                cr += 1

            line += '\n{:>3}'.format('')
            for i in range(8):
                line += '{:>9.4f}'.format(atomic_record[cr])
                cr += 1

            line += '\n{:>3}'.format('')
            for i in range(8):
                line += '{:>9.4f}'.format(atomic_record[cr])
                cr += 1

            line += '\n{:>3}'.format('')
            for i in range(8):
                line += '{:>9.4f}'.format(atomic_record[cr])
                cr += 1

            line += '\n'

            output_file.write(line)

    def _write_bond(self):
        pass
