from SBR_reglas import *

class Sistema(KnowledgeEngine):
    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n1(self):
        return "Diagnostico: Salud estable"

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n2(self):
        return "Diagnostico: Alergía"

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n3(self):
        return "Diagnostico: Gripe común  "

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n4(self):
        return "Diagnostico: Tos crónica"       

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n5(self):
        return "Diagnostico: Disnea"

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n6(self):
        return "Diagnostico: Pleusería" 

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n7(self):
        return "Diagnostico: Asma  "

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n8(self):
        return "Diagnostico: Bronquitis aguda"  

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n9(self):
        return "Diagnostico: Estrés emocional"
    
    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n10(self):
        return "Diagnostico: Rinitis alergica" 
        
    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n11(self):
        return "Diagnostico: Resfriado común"         

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n12(self):
        return "Diagnostico: Influenza "

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n13(self):
        return "Diagnostico: Neumonía"      

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n14(self):
        return "Diagnostico: Virus respiratorio sinicial"

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n15(self):
        return "Diagnostico: Gripe H1N1" 

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),(NOT(Reglas(tos_sangre="si"))))
    def n16(self):
        return "Diagnostico: COVID - 19  "

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n17(self):
        return "Diagnostico: Hemoptisis leve"

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n18(self):
        return "Diagnostico: Hemoptisis moderada" 

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n19(self):
        return "Diagnostico: Bronquitis crónica  "
    
    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n20(self):
        return "Diagnostico: Bronquitis virica"       

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n21(self):
        return "Diagnostico: Bronquiectasia"

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n22(self):
        return "Diagnostico: Bronquiectasia tipo 2"  

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n23(self):
        return "Diagnostico: Vasculitis "

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),(NOT(Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n24(self):
        return "Diagnostico: Vasculitis necrosante"  

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n25(self):
        return "Diagnostico: Tuberculosis"

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n26(self):
        return "Diagnostico: Tuberculosis ganglionar" 
        
    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n27(self):
        return "Diagnostico: Resfriado y hemptisis moderado"         

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),(NOT(Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n28(self):
        return "Diagnostico: resfriado y hemoptisis avanzado "

    @Rule(AND(NOT(Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n29(self):
        return "Diagnostico: Neumonía y hemoptisis leve"       

    @Rule(AND((Reglas(estornudos="si"))),(NOT(Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n30(self):
        return "Diagnostico: Neumonia y hempotisis moderada"

    @Rule(AND(NOT(Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n31(self):
        return "Diagnostico: Cancér de púlmon" 

    @Rule(AND((Reglas(estornudos="si"))),((Reglas(tos_persistente="si"))),((Reglas(dolor_pecho="si"))),((Reglas(df_respirar="si"))),((Reglas(tos_sangre="si"))))
    def n32(self):
        return "Diagnostico: Cancér de pulmon avanzado "
   