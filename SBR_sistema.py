from SBR_reglas import *

class Sistema(KnowledgeEngine):

    info = ''

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n1(self):
        self.info = "Diagnostico: Salud estable"

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n2(self):
        self.info = "Diagnostico: Alergía"

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n3(self):
        self.info = "Diagnostico: Gripe común  "

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n4(self):
        self.info = "Diagnostico: Tos crónica"       

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n5(self):
        self.info = "Diagnostico: Disnea"

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n6(self):
        self.info = "Diagnostico: Pleusería" 

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n7(self):
        self.info = "Diagnostico: Asma  "

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n8(self):
        self.info = "Diagnostico: Bronquitis aguda"  

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n9(self):
        self.info = "Diagnostico: Estrés emocional"
    
    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n10(self):
        self.info = "Diagnostico: Rinitis alergica" 
        
    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n11(self):
        self.info = "Diagnostico: Resfriado común"         

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n12(self):
        self.info = "Diagnostico: Influenza "

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n13(self):
        self.info = "Diagnostico: Neumonía"      

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n14(self):
        self.info = "Diagnostico: Virus respiratorio sinicial"

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n15(self):
        self.info = "Diagnostico: Gripe H1N1" 

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n16(self):
        self.info = "Diagnostico: COVID - 19  "

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n17(self):
        self.info = "Diagnostico: Hemoptisis leve"

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n18(self):
        self.info = "Diagnostico: Hemoptisis moderada" 

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n19(self):
        self.info = "Diagnostico: Bronquitis crónica  "
    
    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n20(self):
        self.info = "Diagnostico: Bronquitis virica"       

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n21(self):
        self.info = "Diagnostico: Bronquiectasia"

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n22(self):
        self.info = "Diagnostico: Bronquiectasia tipo 2"  

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n23(self):
        self.info = "Diagnostico: Vasculitis "

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n24(self):
        self.info = "Diagnostico: Vasculitis necrosante"  

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n25(self):
        self.info = "Diagnostico: Tuberculosis"

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n26(self):
        self.info = "Diagnostico: Tuberculosis ganglionar" 
        
    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n27(self):
        self.info = "Diagnostico: Resfriado y hemptisis moderado"         

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n28(self):
        self.info = "Diagnostico: resfriado y hemoptisis avanzado "

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n29(self):
        self.info = "Diagnostico: Neumonía y hemoptisis leve"       

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n30(self):
        self.info = "Diagnostico: Neumonia y hempotisis moderada"

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n31(self):
        self.info = "Diagnostico: Cancér de púlmon" 

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n32(self):
        self.info = "Diagnostico: Cancér de pulmon avanzado "

    def __str__(self):
        return self.info
   