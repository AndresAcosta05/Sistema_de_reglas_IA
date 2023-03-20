from SBR_reglas import *

class sistema(KnowledgeEngine):
    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n1(self):
        print("Salud estable")

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n2(self):
        print("Alergía") 

    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n3(self):
        print("Gripe común  ")

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n4(self):
        print("Tos crónica")       

    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n5(self):
        print("Disnea")

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n6(self):
        print("Pleusería") 

    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n7(self):
        print("Asma  ")

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n8(self):
        print("Bronquitis aguda")  

    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n9(self):
        print("Estrés emocional")

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n10(self):
        print("Rinitis alergica") 

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n11(self):
        print("Influenza ")

    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n12(self):
        print("Neumonía")       

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n13(self):
        print("Virus respiratorio sinicial")

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n14(self):
        print("Pleusería") 

    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n15(self):
        print("Asma  ")

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n16(self):
        print("Bronquitis aguda") 