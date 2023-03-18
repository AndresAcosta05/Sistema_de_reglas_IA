from reglas import *

class sistema(KnowledgeEngine):
    @Rule(AND(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def s1(self):
        print("Salud estable")
        
    @Rule(AND((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def s2(self):
        print("Tos cronica")
        
    @Rule(AND(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def s3(self):
        print("Disnea")
        
    @Rule(AND((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def s4(self):
        print("Posible asma")
        
    @Rule(AND(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def s5(self):
        print("Estres emocional")
        
    @Rule(AND((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def s6(self):
        print("Resfriado")
        
    @Rule(AND(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def s7(self):
        print("Posible neumonia")
        
    @Rule(AND((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),(NOT(reglas(tos_sangre="si"))))
    def s8(self):
        print("Resfriado o posible neumonia")   
        
    @Rule(AND(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def s9(self):
        print("Hemoptisis")
        
    @Rule(AND((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def s10(self):
        print("Posible bronquitis")
        
    @Rule(AND(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def s11(self):
        print("Posible bronquiectasia")    
    
    @Rule(AND((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),(NOT(reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def s12(self):
        print("Posible vasculitis")
        
    @Rule(AND(NOT(reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def s13(self):
        print("Posible tuberculosis")
        
    @Rule(AND((reglas(tos_persistente="si"))),(NOT(reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def s14(self):
        print("Neumonia grave")               

    @Rule(AND(NOT(reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def s15(self):
        print("Posible Cancér de pulmón")
        
    @Rule(AND((reglas(tos_persistente="si"))),((reglas(dolor_pecho="si"))),((reglas(df_respirar="si"))),((reglas(tos_sangre="si"))))
    def s16(self):
        print("Cancér de pulmón")
        