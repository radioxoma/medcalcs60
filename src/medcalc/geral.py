#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement
# ###########################################################
#                        Teste Geral                        #
# ###########################################################


import datetime
from medcalc.geralclass import *


CATEGORY = _(u"General")


class BMI(MedCalc):
    """Body mass index.

    http://www.medcalc.com/body.html
    http://www-users.med.cornell.edu/~spon/picu/calc/bmicalc.htm
    """
    def __init__(self):
        super(BMI, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Body mass index")
        self.data = [
            (_(u'Body mass (kg)'), 'number', 60),
            (_(u'Height (cm)'), 'number', 170)]

    def show(self):
        W = self.getform()[0][2]
        H = self.getform()[1][2] / 100.0
        self.notify(_(u"%.2f") % (W / H ** 2))


class BSA(MedCalc):
    """Human body surface area.

    BSA = (W ** 0.425 * H ** 0.725) * 0.007184
    http://www-users.med.cornell.edu/~spon/picu/calc/bsacalc.htm
    """
    def __init__(self):
        super(BSA, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Body surface area")
        self.data = [
            (_(u"Body mass (kg)"), 'number', 60),
            (_(u"Height (cm)"), 'number', 170)]

    def show(self):
        W = self.getform()[0][2]
        H = self.getform()[1][2]
        data = (W ** 0.425 * H ** 0.725) * 0.007184
        self.notify(_(u"%.2f m2 (square meters)") % data)


class BEE(MedCalc):
    """Basal energy expenditure (Harris-Benedict equation).

    http://www-users.med.cornell.edu/~spon/picu/calc/beecalc.htm
    https://en.wikipedia.org/wiki/Harris%E2%80%93Benedict_equation
    https://en.wikipedia.org/wiki/Basal_metabolic_rate
    """
    def __init__(self):
        super(BEE, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Basal energy expenditure")
        # Issue: activity is not used for calculation
        # act = [
        #     _(u'Bedrest'),
        #     _(u'Ambulating')]
        sexo = [_(u'Male'), _(u'Female')]
        self.data = [
            (_(u'Sex'), 'combo', (sexo, 0)),
            (_(u"Body mass (kg)"), 'number', 0),
            (_(u'Height (cm)'), 'number', 0),
            (_(u"Age"), 'number', 0)]
            # (_(u"Activity"), "combo", (act, 0))

    def show(self):
        weight = self.getform()[1][2]
        height = self.getform()[2][2]
        age = self.getform()[3][2]
        if (self.getform()[0][2][1] == 0):
            bee = 66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)
        else:
            bee = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
        self.notify(_(u"%.1f kcal") % bee)


class CurrentAge(MedCalc):
    """Calculate current age by date of birth.

    Impossible estimate exact number of month, days without access to leap
    years data on symbian phone.
    """
    def __init__(self):
        super(CurrentAge, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Current age")
        self.data = [(_(u"Date of birth"), 'date', 0.0)]

    def show(self):
        dob = datetime.datetime.utcfromtimestamp(self.getform()[0][2])
        delta = datetime.datetime.now() - dob
        self.notify(_(u"%.2f years") % (delta.days / 365.2425))


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
