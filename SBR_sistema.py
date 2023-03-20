from SBR_reglas import *

class sistema(KnowledgeEngine):
    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n1(self):
        print("Diagnostico: Salud estable")

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n2(self):
        print("Diagnostico: Alergía") 

    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n3(self):
        print("Diagnostico: Gripe común  ")

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n4(self):
        print("Diagnostico: Tos crónica")       

    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n5(self):
        print("Diagnostico: Disnea")

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n6(self):
        print("Diagnostico: Pleusería") 

    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n7(self):
        print("Diagnostico: Asma  ")

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n8(self):
        print("Diagnostico: Bronquitis aguda")  

    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n9(self):
        print("Diagnostico: Estrés emocional")

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n10(self):
        print("Diagnostico: Rinitis alergica") 
        
    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n11(self):
        print("Diagnostico: Resfriado común")         

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n12(self):
        print("Diagnostico: Influenza ")

    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n13(self):
        print("Diagnostico: Neumonía")       

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n14(self):
        print("Diagnostico: Virus respiratorio sinicial")

    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n15(self):
        print("Diagnostico: Gripe H1N1") 

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def n16(self):
        print("Diagnostico: COVID - 19  ")

    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n17(self):
        print("Diagnostico: Hemoptisis leve")

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n18(self):
        print("Diagnostico: Hemoptisis moderada") 

    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n19(self):
        print("Diagnostico: Bronquitis crónica  ")

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n20(self):
        print("Diagnostico: Bronquitis virica")       

    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n21(self):
        print("Diagnostico: Bronquiectasia")

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n22(self):
        print("Diagnostico: Bronquiectasia tipo 2" ) 

    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n23(self):
        print("Diagnostico: Vasculitis ")

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n24(self):
        print("Diagnostico: Vasculitis necrosante")  

    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n25(self):
        print("Diagnostico: Tuberculosis")

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n26(self):
        print("Diagnostico: Tuberculosis ganglionar") 
        
    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n27(self):
        print("Diagnostico: Resfriado y hemptisis moderado")         

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n28(self):
        print("Diagnostico: resfriado y hemoptisis avanzado ")

    @Rule(AND(NOT(reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n29(self):
        print("Diagnostico: Neumonía y hemoptisis leve")       

    @Rule(AND((reglas(estornudos="si"))),(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n30(self):
        print("Diagnostico: Neumonia y hempotisis moderada")

    @Rule(AND(NOT(reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n31(self):
        print("Diagnostico: Cancér de púlmon") 

    @Rule(AND((reglas(estornudos="si"))),((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def n32(self):
        print("Diagnostico: Cancér de pulmon avanzado ")
   