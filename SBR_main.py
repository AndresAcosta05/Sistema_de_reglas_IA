
from random import choice
from SBR_sistema import *

engine = Sistema()
engine.reset()
v_estornudos = input("¿Tiene estornudos? \n  Si   No  ")
engine.declare(Reglas(estornudos=choice([str(v_estornudos)])))
v_tos_persistente = input("¿Tiene tos persistente? \n  Si   No  ")
engine.declare(Reglas(tos_persistente=choice([str(v_tos_persistente)])))
v_dolor_pecho = input("¿Tiene dolor en el pecho frecuente? \n  Si   No  ")
engine.declare(Reglas(dolor_pecho=choice([str(v_dolor_pecho)])))
v_df_respirar = input("¿Tiene dificultad al respirar? \n  Si   No  ")
engine.declare(Reglas(df_respirar=choice([str(v_df_respirar)])))
v_tos_sangre = input("¿Tiene tos con sangre? \n  Si   No  ")
engine.declare(Reglas(tos_sangre=choice([str(v_tos_sangre)])))

engine.run()