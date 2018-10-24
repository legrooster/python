import  os
class AAcount():
    def __init__(self, inter):
        self.inter = inter        

    def run(self):
        while True:
            filename, qFlag, name= self.inter.getInfo()
            if qFlag:
                break
                
            if os.path.exists(filename):  #comfirm whether the file exists
                pdb = open(filename, "r")
                
                #count each amino acids location
                GLY = []
                ALA = []
                PRO = []
                VAL = []
                LEU = []
                ILE = []
                TRP = []
                MET = []
                PHE = []
                SER = []
                THR = []
                TYR = []
                CYS = []
                LYS = []
                ARG = []
                HIS = []
                ASN = []
                GLN = []
                ASP = []
                GLU = []
                
                AA = {}  #amino acids dict
                seq = 0  #sequence document
                peptide = ""
                line = pdb.readline()  #buffer to read each line
                column = line.split()  #segregate the line into columns
                
                #count the sequence
                while line != "" and column[0] != "TER":
                    aa = column[3]
                    if seq != column[5]:
                        seq = column[5]
                        AA[aa] = AA.get(aa, 0) + 1
                        if aa == "GLY":
                            GLY.append(seq)
                            peptide += "G"
                        elif aa == "ALA":
                            ALA.append(seq)
                            peptide += "A"
                        elif aa == "PRO":
                            PRO.append(seq)
                            peptide += "P"
                        elif aa == "VAL":
                            VAL.append(seq)
                            peptide += "V"
                        elif aa == "LEU":
                            LEU.append(seq)
                            peptide += "L"
                        elif aa == "ILE":
                            ILE.append(seq)
                            peptide += "I"
                        elif aa == "TRP":
                            TRP.append(seq)
                            peptide += "W"
                        elif aa == "MET":
                            MET.append(seq)
                            peptide += "M"
                        elif aa == "PHE":
                            PHE.append(seq)
                            peptide += "F"
                        elif aa == "SER":
                            SER.append(seq)
                            peptide += "S"
                        elif aa == "THR":
                            THR.append(seq)
                            peptide += "T"
                        elif aa == "TYR":
                            TYR.append(seq)
                            peptide += "Y"
                        elif aa == "ASN":
                            ASN.append(seq)
                            peptide += "N"
                        elif aa == "GLN":
                            GLN.append(seq)
                            peptide += "Q"
                        elif aa == "CYS":
                            CYS.append(seq)
                            peptide += "C"
                        elif aa == "LYS":
                            LYS.append(seq)
                            peptide += "K"
                        elif aa == "ARG":
                            ARG.append(seq)
                            peptide += "R"
                        elif aa == "HIS":
                            HIS.append(seq)
                            peptide += "H"
                        elif aa == "ASP":
                            ASP.append(seq)
                            peptide += "D"
                        elif aa == "GLU":
                            GLU.append(seq)
                            peptide += "E"
                    line = pdb.readline()
                    column = line.split()
                pdb.close()
                
                if name != "":
                    aac = eval(name)
                else:
                    aac = "Please choose a amino acid."
                self.inter.showInfo( AA, aac, peptide )

