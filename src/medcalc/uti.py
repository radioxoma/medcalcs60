#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement

from medcalc.geralclass import *


CATEGORY = _(u"UTI")


class OxygenContent(MedCalc):
    """Oxygen Content.

    http://www-users.med.cornell.edu/~spon/picu/calc/oxycont.htm
    """
    def __init__(self):
        super(OxygenContent, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Quantidade Oxigênio")
        self.data = [
            (_(u'Hemoglobina (g/dl)'), 'number', 0),
            (_(u'Sa02 (%)'), 'number', 0),
            (_(u'Pa02 (torr)'), 'number', 0)]

    def show(self):
        Hgb = self.getform()[0][2]
        SaO2 = self.getform()[1][2]
        PaO2 = self.getform()[2][2]
        CaO2 = 1.36 * Hgb * SaO2 / 100 + 0.0031 * PaO2
        appuifw.note(_(u"CaO2 = %.2f" % CaO2), "info")


class SatO2(MedCalc):
    """Oxygen Saturation.

    http://www-users.med.cornell.edu/~spon/picu/calc/o2satcal.htm
    """
    def __init__(self):
        super(SatO2, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Saturação Oxigênio")
        # pO2 = P * FiO2; P = 760 mmHg (air pressure), FiO2 = 0.21 (21 %) 
        # pO2 = 760 * 0.21 = 159.6 mmHg
        self.data = [(_(u'pO2 - Entrada'), 'number', 160)]

    def show(self):
        pO2 = self.getform()[0][2]
        print(pO2, self.getform())
        SO2 = 100 * (23400.0 * (pO2 ** 3 + 150 * pO2) ** -1 + 1) ** -1
        appuifw.note(_(u"SpO2 = %.2f %%" % SO2), "info")


class OsmSerica(MedCalc):
    """Serum Osmolality.

    http://www-users.med.cornell.edu/~spon/picu/calc/osmolal.htm
    """
    def __init__(self):
        super(OsmSerica, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Osmolaridade Sérica")
        self.data = [
            (u'Na (mEq/L)', 'number', 0),
            (u'Glucose (mg/dL)', 'number', 0),
            (u'BUN (mg/dL)', 'number', 0)]

    def show(self):
        Na = self.getform()[0][2]
        Glu = self.getform()[1][2]
        BUN = self.getform()[2][2]
        Osmolality = 2 * Na + Glu / 18 + BUN / 2.8
        appuifw.note(_(u"Osmolaridade Sérica = %.2f" % Osmolality), "info")


class VentIndex(MedCalc):
    """Ventilation Index.

    http://www-users.med.cornell.edu/~spon/picu/calc/ventindx.htm
    """
    def __init__(self):
        super(VentIndex, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Indíce de Ventilação")
        self.data = [
            (_(u'Ritmo Resp. Vent. (bpm)'), 'number', 0),
            (_(u'Pico Pressão Insp. (torr)'), 'number', 0),
            (_(u'PEEP (torr)'), 'number', 0),
            (_(u'PaCO2 (torr)'), 'number', 0)]

    def show(self):
        RR = self.getform()[0][2]
        PIP = self.getform()[1][2]
        PEEP = self.getform()[2][2]
        PaCO2 = self.getform()[3][2]
        VI = (RR * (PIP - PEEP) * PaCO2) / 1000.0
        appuifw.note(_(u"Indice Ventilação %.2f" % VI), 'info')


class AaGrad(MedCalc):
    """Alveolar-arterial Gradient.

    Input FiO2  decimal
    Input PaCO2 torr
    Input PaO2  torr
    http://www-users.med.cornell.edu/~spon/picu/calc/aagrad.htm
    """
    def __init__(self):
        super(AaGrad, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Gradiente Arterial Alveolar")
        self.data = [
            (_(u'In FiO2 (dec)'), 'number', 0),
            (_(u'In PaC02 (torr)'), 'number', 0),
            (_(u'In Pa02 (torr)'), 'number', 0)]

    def show(self):
        # 1 torr == 1/760 atm (standard atmosphere)
        PAO2 = self.getform()[0][2] * (760 - 47) - self.getform()[1][2] / 0.8
        PAO2 -= self.getform()[2][2]
        appuifw.note(_(u"Gradiente Arterial Alveolar = %.2f" % PAO2), "info")


class Bicarb(MedCalc):
    def __init__(self):
        super(Bicarb, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Bicarbonato e base excesso")
        self.data = [
            (_(u'pH'), 'number', 0),
            (_(u'PaC02'), 'number', 0)]

    def show(self):
        pH = self.getform()[0][2]
        pCO2 = self.getform()[1][2]
        HCO3 = 0.03 * pCO2 * 10 ** (pH - 6.1)
        BE = 0.02786 * pCO2 * 10 ** (pH - 6.1) + 13.77 * pH - 124.58
        appuifw.note(_(u"HCO3 = %(HCO3)s \nDesbalanceamento Base: %(BE)s" % {
            'HCO3': HCO3, 'BE': BE}), "info")
