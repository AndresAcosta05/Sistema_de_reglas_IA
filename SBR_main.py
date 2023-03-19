
from random import choice
from SBR_sistema import *

engine = sistema()
engine.reset()
v_tos_persistente = input("¿Tiene tos persistente? \n  si   no ")
engine.declare(reglas(tos_persistente=choice([str(v_tos_persistente)])))
v_dolor_pecho = input("¿Tiene dolor en el pecho frecuente? \n  si   no ")
engine.declare(reglas(dolor_pecho=choice([str(v_dolor_pecho)])))
v_df_respirar = input("¿Tiene dificultad al respirar? \n  si   no ")
engine.declare(reglas(df_respirar=choice([str(v_df_respirar)])))
v_tos_sangre = input("¿Tiene tos con sangre? \n  si   no ")
engine.declare(reglas(tos_sangre=choice([str(v_tos_sangre)])))

engine.run()