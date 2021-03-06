# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

import pilas
from pilas.actores import Animacion
import math


class NaveKids(Animacion):
    "Representa una nave que puede disparar."

    def __init__(self, x=0, y=0, velocidad=2):
        self.velocidad = velocidad
        grilla = pilas.imagenes.cargar_grilla("spacekids.png", 2)
        Animacion.__init__(self, grilla, ciclica=True, x=x, y=y)
        self.radio_de_colision = 20
        self.aprender(pilas.habilidades.PuedeExplotar)

        self.aprender(pilas.habilidades.MoverseConElTeclado,
                      velocidad_maxima=self.velocidad,
                      aceleracion=1,
                      deceleracion=0.04,
                      con_rotacion=False,
                      velocidad_rotacion=0,
                      marcha_atras=True)

    def actualizar(self):
        Animacion.actualizar(self)