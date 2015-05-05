#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement
# ###########################################################
#                        Teste Geral                        #
# ###########################################################

from medcalc.geralclass import *


CATEGORY = _(u"Geral")


class BMI(MedCalc):
    """Body mass index.

    http://www.medcalc.com/body.html
    http://www-users.med.cornell.edu/~spon/picu/calc/bmicalc.htm
    """
    def __init__(self):
        super(BMI, self).__init__()
        self.category = CATEGORY
        self.name = _(u"BMI")
        self.data = [
            (_(u'Peso (kg)'), 'number', 60),
            (_(u'Altura (cm)'), 'number', 170)]

    def show(self):
        W = self.getform()[0][2]
        H = self.getform()[1][2] / 100.0
        appuifw.note(_(u"IMC = %f" % (W / H ** 2)), "info")


class BSA(MedCalc):
    """Human body surface area.

    BSA = (W ** 0.425 * H ** 0.725) * 0.007184
    http://www-users.med.cornell.edu/~spon/picu/calc/bsacalc.htm
    """
    def __init__(self):
        super(BSA, self).__init__()
        self.category = CATEGORY
        self.name = _(u"BSA")
        self.data = [
            (_(u"Peso (kg)"), 'number', 60),
            (_(u"Altura (cm)"), 'number', 170)]

    def show(self):
        W = self.getform()[0][2]
        H = self.getform()[1][2]
        data = (W ** 0.425 * H ** 0.725) * 0.007184
        appuifw.note(_(u"BSA = %f" % data), "info")


class BEE(MedCalc):
    """Basal energy expenditure.

    http://www-users.med.cornell.edu/~spon/picu/calc/beecalc.htm
    """
    def __init__(self):
        super(BEE, self).__init__()
        self.category = CATEGORY
        self.name = _(u"BEE")
        # Issue: activity is not used for calculation
        act = [
            _(u'Repouso'),  # Rest?
            _(u'Deambulando')]  # Walking?
        sexo = [_(u'Homem'), _(u'Mulher')]
        self.data = [
            (_(u'Sexo'), 'combo', (sexo, 0)),
            (_(u"Peso (kg)"), 'number', 0),
            (_(u'Altura (cm)'), 'number', 0),
            (_(u"Idade"), 'number', 0),
            (_(u"Atividade"), "combo", (act, 0))]

    def show(self):
        W = self.getform()[1][2]
        H = self.getform()[2][2]
        A = self.getform()[3][2]
        if (self.getform()[0][2][1] == 0):
            bee = 66.5 + (13.75 * W) + (5.003 * H) - (6.775 * A)
        else:
            bee = 655.1 + (9.563 * W) + (1.850 * H) - (4.676 * A)
        appuifw.note(_(u"Gasto de Energia Basal = %.0f kcal" % bee), "info")


# class AnestesiaRisk(MedCalcList):
#     def __init__(self):
#         super(AnestesiaRisk, self).__init__()
#         self.category = CATEGORY
#         self.name = _(u"Risco Cirúrgico")
#         self.data = [
#             _(u'Hipertensão arterial controlada '),
#             _(u'Diabetes controlada'),
#             _(u'Doença vascular periférica controlada'),
#             _(u'Doença pulm. obstr. crônica controlada'),
#             _(u'Doença Sistemica Controlada'),
#             _(u'Angina inst. c/ hep EV ou nitrog.'),
#             _(u'Balão pré-op. intra-aórt'),
#             _(u'Insuficiência cardíaca c/ edema pulm. ou perif.'),
#             _(u'Hipertensão não controlada'),
#             _(u'Insufic. renal (creatinina sérica> 140µmol / L'),
#             _(u'Outros debilitante doença sistêmica'),
#             _(u'Reoperation'),
#             _(u'Valvula e cirurg. coronaria'),
#             _(u'Multiplas valvulas'),
#             _(u'Ventricular aneurisma esq.'),
#             _(u'Reparo de defeito septo ventricular após IM'),
#             _(u'Bypass de vasos difusos ou calcificados')]
# 
#     def show(self):
#         soma = 0
#         print(self._f)
