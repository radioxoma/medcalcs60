#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import with_statement

from medcalc.geralclass import *


CATEGORY = _(u"ICU")


class OxygenContent(MedCalc):
    """Oxygen Content.

    http://www-users.med.cornell.edu/~spon/picu/calc/oxycont.htm
    """
    def __init__(self):
        super(OxygenContent, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Oxygen content")
        self.data = [
            (_(u'Hb (g/dl)'), 'number', 0),
            (_(u'SaO2 (%)'), 'number', 0),
            (_(u'PaO2 (mmHg)'), 'number', 0)]

    def show(self):
        Hgb = self.getform()[0][2]
        SaO2 = self.getform()[1][2]
        PaO2 = self.getform()[2][2]
        CaO2 = 1.36 * Hgb * SaO2 / 100 + 0.0031 * PaO2
        self.notify(_(u"CaO2 %.2f") % CaO2)


class SatO2(MedCalc):
    """Oxygen Saturation.

    http://www-users.med.cornell.edu/~spon/picu/calc/o2satcal.htm
    """
    def __init__(self):
        super(SatO2, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Oxygen saturation")
        # pO2 = P * FiO2; P = 760 mmHg (air pressure), FiO2 = 0.21 (21 %) 
        # pO2 = 760 * 0.21 = 159.6 mmHg
        self.data = [(_(u"Insp. pO2"), 'number', 160)]

    def show(self):
        pO2 = self.getform()[0][2]
        SO2 = 100 * (23400.0 * (pO2 ** 3 + 150 * pO2) ** -1 + 1) ** -1
        self.notify(_(u"SpO2 %.2f %%") % SO2)


class OsmSerica(MedCalc):
    """Serum Osmolality.

    http://www-users.med.cornell.edu/~spon/picu/calc/osmolal.htm
    """
    def __init__(self):
        super(OsmSerica, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Serum osmolality")
        self.data = [
            (u'Na (mEq/L)', 'number', 0),
            (u'Glucose (mg/dL)', 'number', 0),
            (u'BUN (mg/dL)', 'number', 0)]

    def show(self):
        Na = self.getform()[0][2]
        Glu = self.getform()[1][2]
        BUN = self.getform()[2][2]
        osmolality = 2 * Na + Glu / 18 + BUN / 2.8
        self.notify(_(u"%.2f mOsm/kg") % osmolality)


class VentIndex(MedCalc):
    """Ventilation Index.

    http://www-users.med.cornell.edu/~spon/picu/calc/ventindx.htm
    """
    def __init__(self):
        super(VentIndex, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Ventilation index")
        self.data = [
            (_(u'Respiratory rate (bpm)'), 'number', 0),
            (_(u'Peak insp. pressure (mmHg)'), 'number', 0),
            (_(u'PEEP (mmHg)'), 'number', 0),
            (_(u'PaCO2 (mmHg)'), 'number', 0)]

    def show(self):
        RR = self.getform()[0][2]
        PIP = self.getform()[1][2]
        PEEP = self.getform()[2][2]
        PaCO2 = self.getform()[3][2]
        VI = (RR * (PIP - PEEP) * PaCO2) / 1000.0
        self.notify(_(u"%.2f") % VI)


class AaGrad(MedCalc):
    """Alveolar-arterial Gradient.

    Input FiO2  decimal
    Input PaCO2 torr
    Input PaO2  torr
    http://www-users.med.cornell.edu/~spon/picu/calc/aagrad.htm
    https://en.wikipedia.org/wiki/Alveolar%E2%80%93arterial_gradient
    """
    def __init__(self):
        super(AaGrad, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Alveolar-arterial gradient")
        self.data = [
            (_(u'In FiO2 (%)'), 'number', 0),
            (_(u'In PaCO2 (mmHg)'), 'number', 0),
            (_(u'In PaO2 (mmHg)'), 'number', 0)]

    def show(self):
        # 1 torr == 1/760 atm (standard atmosphere) == 1 mmHg
        PAO2 = self.getform()[0][2] * (760 - 47) - self.getform()[1][2] / 0.8
        PAO2 -= self.getform()[2][2]
        self.notify(_(u"%.2f") % PAO2)


class Bicarb(MedCalc):
    """Base Excess & Calculated Bicarbonate.
    
    http://www-users.med.cornell.edu/~spon/picu/calc/basecalc.htm
    """
    def __init__(self):
        super(Bicarb, self).__init__()
        self.category = CATEGORY
        self.name = _(u"Bicarbonate & base excess")
        self.data = [
            (_(u'pH'), 'float', 7.4),
            (_(u'PaCO2'), 'number', 40)]

    def show(self):
        pH = self.getform()[0][2]
        pCO2 = self.getform()[1][2]
        HCO3 = 0.03 * pCO2 * 10 ** (pH - 6.1)
        BE = 0.02786 * pCO2 * 10 ** (pH - 6.1) + 13.77 * pH - 124.58
        self.notify(
            _(u"HCO3\t%(HCO3).2f\tmEq/L (22-26)\nBE\t%(BE).2f\tmEq/L (±2)") % {
            'HCO3': HCO3, 'BE': BE})
